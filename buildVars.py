# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _
import changelog

# Add-on information variables
addon_info = AddonInfo(
	# add-on Name/identifier, internal for NVDA
	addon_name="unigramPlus",
	# Add-on summary/title, usually the user visible name of the add-on
	# Translators: Summary/title for this add-on
	# to be shown on installation and add-on information found in add-on store.
	addon_summary=_("UnigramPlus"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-on store.
	addon_description=_(
		"""This add-on adds a lot of hotkeys for quick navigation through the main elements of the Unigram application, convenient interaction with Chat messages, and also adds many small improvements that make working in Unigram much easier""",
	),
	# version
	addon_version="5.8.6",
	# Brief changelog for this version
	# Translators: what's new content for the add-on version to be shown in the add-on store.
	# Note: Edit changelog.py instead of this.
	addon_changelog=changelog.value,
	# Author(s)
	addon_author="Kostya Gladkiy<gladkiy.kostya@gmail.com>",
	# URL for the add-on documentation support
	addon_url="https://github.com/Kostya-Gladkiy/UnigramPlus",
	# URL for the add-on repository where the source code can be found
	addon_sourceURL="https://github.com/Kostya-Gladkiy/UnigramPlus",
	# Documentation file name
	addon_docFileName="readme.html",
	# Minimum NVDA version supported (e.g. "2019.3.0", minor version is optional)
	addon_minimumNVDAVersion="2021.2.0",
	# Last NVDA version supported/tested (e.g. "2024.4.0", ideally more recent than minimum version)
	addon_lastTestedNVDAVersion="2026.3.0",
	# Add-on update channel (default is None, denoting stable releases,
	# and for development releases, use "dev".)
	# Do not change unless you know what you are doing!
	addon_updateChannel=None,
	# Add-on license such as GPL 2
	addon_license="GPL 2",
	# URL for the license document the add-on is licensed under
	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

# Define the python files that are the sources of your add-on.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions.
# For example to include all files with a ".py" extension from the "globalPlugins" dir of your add-on
# the list can be written as follows:
# pythonSources = ["addon/globalPlugins/*.py"]
# For more information on SCons Glob expressions please take a look at:
# https://scons.org/doc/production/HTML/scons-user/apd.html
pythonSources: list[str] = ["addon/appModules/*.py", "addon/GlobalPlugins/UnigramPlus/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources: list[str] = pythonSources + ["buildVars.py", "changelog.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
# You can either list every file (using ""/") as a path separator,
# or use glob expressions. NVDA compiles Python sources for its own interpreter,
# so developer-machine bytecode caches must not be shipped.
excludedFiles: list[str] = ["**/__pycache__/*", "**/*.pyc"]

# Base language for the NVDA add-on
# If your add-on is written in a language other than english, modify this variable.
# For example, set baseLanguage to "es" if your add-on is primarily written in spanish.
# You must also edit .gitignore file to specify base language files to be ignored.
baseLanguage: str = "en"

# Markdown extensions for add-on documentation
# Most add-ons do not require additional Markdown extensions.
# If you need to add support for markup such as tables, fill out the below list.
# Extensions string must be of the form "markdown.extensions.extensionName"
# e.g. "markdown.extensions.tables" to add tables.
markdownExtensions: list[str] = ["markdown.extensions.tables"]

# Custom braille translation tables
# If your add-on includes custom braille tables (most will not), fill out this dictionary.
brailleTables: BrailleTables = {}

# Custom speech symbol dictionaries
# If your add-on includes custom speech symbol dictionaries (most will not), fill out this dictionary.
symbolDictionaries: SymbolDictionaries = {}
