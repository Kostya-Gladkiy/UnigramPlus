import ast
from pathlib import Path
import sys
from types import SimpleNamespace
import warnings


sys.path.insert(0, str(Path(__file__).parents[1] / "addon" / "appModules"))

from rich_message import (  # noqa: E402
	extract_message_text,
	extract_rich_message_text,
	find_rich_message_root,
	merge_message_text_and_rich_text,
)


class Node:
	def __init__(self, *, name="", class_name="", automation_id="", children=None):
		self.name = name
		self.UIAClassName = class_name
		self.UIAAutomationId = automation_id
		self.children = children or []


def test_finds_namespaced_instant_content_below_message():
	rich = Node(
		class_name="Telegram.Controls.Messages.Content.InstantContent",
		children=[Node(automation_id="LayoutRoot", children=[Node(name="Rich block")])],
	)
	message = Node(name="Rich block, Received at 18:17", children=[Node(children=[rich])])

	assert find_rich_message_root(message) is rich


def test_rejects_instant_content_alongside_a_plain_caption():
	rich = Node(
		class_name="InstantContent",
		children=[Node(automation_id="LayoutRoot", children=[Node(name="Rich block")])],
	)
	message = Node(
		name="Caption, Rich block, Received at 18:17",
		children=[Node(name="Caption", automation_id="TextBlock"), rich],
	)

	assert find_rich_message_root(message) is None


def test_rejects_empty_rich_content_that_has_no_official_readable_text():
	rich = Node(
		class_name="InstantContent",
		children=[Node(automation_id="LayoutRoot")],
	)
	message = Node(
		name="Sophie ✨\r\n, Administrator.\r\nReply to Ken.\r\n, Received at 18:17",
		children=[Node(name="", automation_id="Message"), rich],
	)

	assert find_rich_message_root(message) is None


def test_uses_unigrams_official_rich_summary_as_direct_message_text():
	rich = Node(
		class_name="InstantContent",
		children=[Node(automation_id="LayoutRoot", children=[Node(name="Official rich text")])],
	)
	message = Node(
		name="Official rich text, Received at 18:17",
		children=[Node(name="Official rich text", automation_id="Message"), rich],
	)

	assert find_rich_message_root(message) is None
	assert extract_message_text(message) == "Official rich text"


def test_rejects_empty_recycled_rich_content_on_replied_media_summary():
	stale_rich = Node(class_name="InstantContent", children=[Node(automation_id="LayoutRoot")])
	message = Node(
		name="😀 Sticker\r\nReply to Ken.\r\n, Received at 18:17",
		children=[stale_rich],
	)

	assert find_rich_message_root(message) is None


def test_rejects_recycled_rich_content_on_a_sticker_or_animated_emoji():
	stale_rich = Node(
		class_name="InstantContent",
		children=[Node(automation_id="LayoutRoot", children=[Node(name="Old rich block")])],
	)
	message = Node(
		name="😀 Sticker, Received at 18:17",
		children=[Node(class_name="Telegram.Controls.Messages.Content.StickerContent"), stale_rich],
	)

	assert find_rich_message_root(message) is None


def test_rejects_recycled_rich_content_that_is_not_in_the_current_message_summary():
	stale_rich = Node(
		class_name="InstantContent",
		children=[Node(automation_id="LayoutRoot", children=[Node(name="Old rich block")])],
	)
	message = Node(
		name="😀, Received at 18:17",
		children=[Node(name="😀", automation_id="TextBlock"), stale_rich],
	)

	assert find_rich_message_root(message) is None


def test_does_not_misclassify_an_unrelated_layout_root():
	message = Node(children=[Node(automation_id="LayoutRoot", children=[Node(name="ordinary message")])])

	assert find_rich_message_root(message) is None


def test_finds_and_extracts_instant_content_from_raw_uia_view(monkeypatch):
	class UiaConstants:
		UIA_NamePropertyId = 1
		UIA_ClassNamePropertyId = 2
		UIA_AutomationIdPropertyId = 3
		UIA_IsOffscreenPropertyId = 5

	class Element:
		def __init__(
			self,
			*,
			name="",
			class_name="",
			automation_id="",
			text_pattern_text=None,
			children=None,
		):
			self.properties = {1: name, 2: class_name, 3: automation_id}
			self.text_pattern_text = text_pattern_text
			self.children = children or []

		def GetCurrentPropertyValueEx(self, property_id, ignore_default):
			return self.properties.get(property_id, "")

		def findFirst(self, scope, condition):
			assert scope == "descendants"
			self.find_condition = condition
			return self.find_result

		def GetCurrentPattern(self, pattern_id):
			assert pattern_id == 4
			if self.text_pattern_text is None:
				raise RuntimeError("TextPattern unavailable")
			return Pattern(self.text_pattern_text)

	class Pattern:
		def __init__(self, text):
			self.DocumentRange = SimpleNamespace(GetText=lambda max_length: text)

		def QueryInterface(self, interface):
			assert interface == "IUIAutomationTextPattern"
			return self

	class Walker:
		def GetFirstChildElement(self, element):
			return element.children[0] if element.children else None

		def GetNextSiblingElement(self, element):
			return siblings.get(id(element))

		def GetParentElement(self, element):
			return parents.get(id(element))

	first_text = Element(text_pattern_text="First raw block")
	second_text = Element(text_pattern_text="Second raw block")
	layout = Element(automation_id="LayoutRoot", children=[first_text, second_text])
	rich = Element(class_name="InstantContent", children=[layout])
	media = Element(children=[rich])
	media.properties[3] = "Media"
	panel = Element(automation_id="Panel", children=[media])
	siblings = {id(first_text): second_text}
	parents = {id(rich): media, id(media): panel}
	client = SimpleNamespace(
		RawViewWalker=Walker(),
		CreatePropertyCondition=lambda property_id, value: (property_id, value),
		createAndConditionFromArray=lambda conditions: tuple(conditions),
		CompareElements=lambda first, second: first is second,
	)
	fake_uia_handler = SimpleNamespace(
		handler=SimpleNamespace(clientObject=client),
		UIA=UiaConstants,
		UIA_TextPatternId=4,
		IUIAutomationTextPattern="IUIAutomationTextPattern",
		TreeScope_Descendants="descendants",
	)
	monkeypatch.setitem(sys.modules, "UIAHandler", fake_uia_handler)
	message_element = Element(children=[panel])
	message_element.find_result = rich
	message = SimpleNamespace(UIAElement=message_element)

	root = find_rich_message_root(message)

	assert root.UIAClassName == "InstantContent"
	assert extract_rich_message_text(root) == "First raw block\n\nSecond raw block"

	# Message and Media are siblings in MessageBubble.xaml. A populated main
	# Message control proves a matching InstantContent is stale, even when NVDA's
	# control-view children do not expose the plain text node.
	stale_text = Element(text_pattern_text="Ordinary raw text")
	stale_layout = Element(automation_id="LayoutRoot", children=[stale_text])
	stale_rich = Element(class_name="InstantContent", children=[stale_layout])
	plain_text = Element(automation_id="Message", text_pattern_text="Ordinary raw text")
	media.children = [stale_rich]
	panel.children = [plain_text, media]
	siblings[id(plain_text)] = media
	parents[id(plain_text)] = panel
	parents[id(stale_rich)] = media
	message_element.find_result = stale_rich
	plain = SimpleNamespace(
		name="Ordinary raw text, Sent at 18:17",
		children=[],
		UIAElement=message_element,
	)
	assert find_rich_message_root(plain) is None

	media.children = [rich]
	panel.children = [media]
	message_element.find_result = rich
	mixed = SimpleNamespace(
		name="Caption, First raw block, Second raw block, Sent at 18:17",
		children=[Node(name="Caption", automation_id="TextBlock")],
		UIAElement=message_element,
	)
	assert find_rich_message_root(mixed) is None

	ordinary = SimpleNamespace(
		name="Ordinary text, Sent at 18:17",
		children=[Node(name="Ordinary text", automation_id="TextBlock")],
		UIAElement=message_element,
	)
	assert find_rich_message_root(ordinary) is None

	sticker_content = Element(class_name="StickerContent")
	media.children = [sticker_content, rich]
	siblings[id(sticker_content)] = rich
	parents[id(sticker_content)] = media
	sticker = SimpleNamespace(
		name="😀 Sticker, Sent at 18:17",
		children=[],
		UIAElement=message_element,
	)
	assert find_rich_message_root(sticker) is None

	matching_sticker = SimpleNamespace(
		name="First raw block, Second raw block, Sent at 18:17",
		children=[],
		UIAElement=message_element,
	)
	assert find_rich_message_root(matching_sticker) is None


def test_collects_all_flattened_message_text_controls():
	message = Node(
		children=[
			Node(name="First paragraph", automation_id="TextBlock"),
			Node(name="Second paragraph", automation_id="TextBlock"),
			Node(name="recognized", automation_id="RecognizedText"),
			Node(name="18:17", automation_id="Footer"),
		]
	)

	assert extract_message_text(message) == "First paragraph\n\nSecond paragraph\n\nrecognized"


def test_merges_plain_and_rich_text_for_the_classic_window_without_duplication():
	assert merge_message_text_and_rich_text("Caption", "Rich text") == "Caption\n\nRich text"
	assert merge_message_text_and_rich_text("Caption and rich text", "rich text") == ("Caption and rich text")
	assert merge_message_text_and_rich_text("rich text", "Caption and rich text") == ("Caption and rich text")


def test_extracts_layout_children_as_separate_markdown_blocks():
	layout = Node(
		automation_id="LayoutRoot",
		children=[
			Node(name="Heading"),
			Node(children=[Node(name="First paragraph"), Node(name="linked text")]),
			Node(name="Second paragraph\r\ncontinues"),
		],
	)
	rich = Node(class_name="InstantContent", children=[layout])

	assert extract_rich_message_text(rich) == (
		"Heading\n\nFirst paragraph\nlinked text\n\nSecond paragraph\ncontinues"
	)


def test_prefers_a_block_name_over_duplicate_descendant_names():
	block = Node(name="A sentence with a link", children=[Node(name="a link")])
	rich = Node(class_name="InstantContent", children=[Node(automation_id="LayoutRoot", children=[block])])

	assert extract_rich_message_text(rich) == "A sentence with a link"


def test_cyclic_uia_tree_is_bounded_and_safe():
	first = Node()
	second = Node()
	first.children = [second]
	second.children = [first]

	assert find_rich_message_root(first) is None
	assert extract_rich_message_text(first) == ""


def test_text_info_fallback_handles_flattened_provider():
	class TextInfo:
		text = "Fallback rich text"

	class FlatRichNode(Node):
		def makeTextInfo(self, position):
			assert position == "all"
			return TextInfo()

	rich = FlatRichNode(class_name="InstantContent")

	assert extract_rich_message_text(rich, "all") == "Fallback rich text"


def test_alt_c_always_uses_the_classic_wx_window():
	"""Exercise the actual Alt+C method body without importing NVDA."""
	source = (Path(__file__).parents[1] / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8")
	with warnings.catch_warnings():
		# unigram.py contains legacy replacement strings such as "\g<1>" outside
		# this method. Parsing the full module can warn about those unrelated lines.
		warnings.simplefilter("ignore", SyntaxWarning)
		module = ast.parse(source)
	message_class = next(node for node in module.body if isinstance(node, ast.ClassDef) and node.name == "Message_list_item")
	method = next(
		node
		for node in message_class.body
		if isinstance(node, ast.FunctionDef) and node.name == "script_show_text_message"
	)
	method.decorator_list = []

	message_item = SimpleNamespace(
		children=[
			SimpleNamespace(UIAAutomationId="TextBlock", name="Ordinary text"),
			SimpleNamespace(UIAAutomationId="RecognizedText", name="Recognized text"),
		]
	)
	for rich_root in (None, object()):
		opened = []
		namespace = {
			"find_rich_message_root": lambda obj, result=rich_root: result,
			"extract_rich_message_text": lambda root, position: "Distinct rich text" if root else "",
			"extract_message_text": extract_message_text,
			"merge_message_text_and_rich_text": merge_message_text_and_rich_text,
			"textInfos": SimpleNamespace(POSITION_ALL="all"),
			"TextWindow": lambda *args, **kwargs: opened.append(("classic", args, kwargs)),
			"message": lambda text: opened.append(("message", text)),
			"conf": SimpleNamespace(get=lambda key: True),
			"_": lambda text: text,
		}
		exec(compile(ast.Module(body=[method], type_ignores=[]), "unigram.py", "exec"), namespace)

		namespace["script_show_text_message"](message_item, None)

		title = "Rich message" if rich_root else "message text"
		text = "Ordinary text\n\nRecognized text"
		if rich_root:
			text += "\n\nDistinct rich text"
		assert opened == [("classic", (text, title), {"readOnly": False})]


def test_obsolete_empty_comma_detection_and_focus_hint_are_removed():
	source = (Path(__file__).parents[1] / "addon" / "appModules" / "unigram.py").read_text(encoding="utf-8")
	rich_source = (Path(__file__).parents[1] / "addon" / "appModules" / "rich_message.py").read_text(
		encoding="utf-8"
	)

	assert "Rich message. Press Alt+C to browse" not in source
	assert "has_empty_rich_message_summary" not in source + rich_source
	assert "is_rich_message" not in source + rich_source
