# Unigram Plus

* Author: Kostya Gladkiy (Ukrain)
* [Telegram channel](https://t.me/unigramPlus)
* Telegram: @unigramPlus
* donation link: [https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)
* PayPal: gladkiy.kostya@gmail.com


Use Unigram in a more comfortable and productive way. This addon provides many hotkeys for a quick and comfortable use of Unigram and makes a lot of small improvements.
## Some of the major improvements are:

* Adds a significant improvement to the display of messages such as a poll, a link, or a message with attached media.
* When focus enters the list of chats, it removes such phrases as: "chats, tab, selected list". And when the focus hits the list of messages, the phrase "list".
* The name and size of the file will be spoken when the cursor is focused on the "Open File" button or the "Download File" button, and when the cursor is focused on the play button of the audio file, you will hear its name and duration.
* When focus is placed on a voice message that is currently being played, first information about the time of its playback is announced, and then all other information.
* When focusing on a selected message in a chat, you will first hear the information that it is selected, and then the content of the message.
* Now, when moving in the chat, the phrase "Seen" will not be pronounced at all, and the phrase "Not seen" will be pronounced before the content of the message. This feature currently only works in English, Russian, Ukrainian, Spanish, Portuguese, Polish, Croatian, Turkish, and Persian.
* Significantly improved the function of recording voice messages. Starting and sending a voice message recording are accompanied by characteristic sounds, while Unigram 13.0 and later announce a canceled recording themselves. Also, when performing these functions, the focus remains in its position and does not jump to either the record button or the message input field.
* If the media attached to the message is opened using the spacebar, then after closing it, the focus will return to the last element that was in focus.
* The add-on allows you to completely disable the announcement of progress bars, as well as disable only the announcement of the progress bar for playing voice messages.

## Custom sounds
UnigramPlus sound files are stored in the add-on's `appModules\media` folder. Open NVDA Settings > UnigramPlus and press **Open UnigramPlus sounds folder** to open it. To customize a sound, copy your replacement WAV file into that folder using the same file name as the sound you want to replace, then restart NVDA or reload add-ons. Add-on updates may restore bundled sounds, so keep a backup of your custom files.

## Information about the opportunity to donate to the developer:
If you really like this add-on and you have the desire, and most importantly the opportunity, to financially support the developer and thereby motivate him to further develop this add-on, you can do this by transferring a small amount to the following bank details: [donation link](https://unigramplus.diaka.ua/donate), or card number is 5169360009004502(Ukraine).
And remember that everyone who read this line thought that someone will definitely support the developer, but it will not be me.

<!-- shortcut-table-start -->
## Hotkey list:

> In the Category column, `UnigramPlus` identifies shortcuts provided by the add-on and `Unigram` identifies shortcuts built into Unigram.

> `Unigram (undocumented)` identifies shortcuts implemented by the current Unigram source but not yet listed in its official Shortcuts.md.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Move among chats

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | Next chat |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | Previous chat |
| **Ctrl+Alt+Home** | Unigram (undocumented) | First chat |
| **Ctrl+Alt+End** | Unigram (undocumented) | Last chat |
| **Ctrl+Alt+Up/Down** | UnigramPlus | Move to the next or previous chat with unread mentions |
| **ALT+1** | UnigramPlus | Move focus to chat list |
| **ALT+2** | UnigramPlus | Move focus to the last message in an open chat |
| **ALT+3** | UnigramPlus | Move focus to 'unread messages' label |
| **ALT+4** | UnigramPlus | Move focus to list of chat folders |
| **ALT+5** | UnigramPlus | Move focus to open profile |
| **ALT+6** | UnigramPlus | Move focus to the list of group threads |
| **ALT+D** | UnigramPlus | Move the focus to the edit field. If the focus is already in the edit field, then after pressing the hotkey, it will move to where it was before |

### Search

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **Ctrl+F** | Unigram | Messages search per chat |
| **Ctrl+Shift+F** | Unigram (undocumented) | Chat search |
| **Search key** | Unigram (undocumented) | Search the current page |
| **ALT+I** | UnigramPlus | Go to the list with search results |
| **F3** | UnigramPlus | Go to the next search result |
| **Shift+F3** | UnigramPlus | Go to the previous search result |

### Selected text in typing area

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (undocumented) | Redo |
| **Alt+X** | Unigram (undocumented) | Convert four selected hexadecimal digits to their corresponding character |
| **Ctrl+X** | Unigram | Cut |
| **Ctrl+C** | Unigram | Copy |
| **Ctrl+V** | Unigram | Paste |
| **Ctrl+A** | Unigram | Select All |
| **Ctrl+Shift+.** | Unigram | Quote |
| **Ctrl+B** | Unigram | Bold |
| **Ctrl+I** | Unigram | Italic |
| **Ctrl+U** | Unigram | Underline |
| **Ctrl+Shift+X** | Unigram | Strikethrough |
| **Ctrl+Shift+M** | Unigram | Monospace |
| **Ctrl+Shift+P** | Unigram | Spoiler |
| **Ctrl+K** | Unigram | Create Link |
| **Ctrl+Shift+N** | Unigram | Remove formatting (Regular text) |

### Folders

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+1** | Unigram | First folder (All chats) |
| **Ctrl+2** | Unigram | Second folder |
| **Ctrl+3** | Unigram | Third folder |
| **Ctrl+4** | Unigram | Fourth folder |
| **Ctrl+5** | Unigram | Fifth folder |
| **Ctrl+6** | Unigram | Sixth folder |
| **Ctrl+7** | Unigram | Seventh folder |
| **Ctrl+8** | Unigram | Eighth folder |
| **Ctrl+9** | Unigram | Archive |
| **Ctrl+Shift+Down** | Unigram (undocumented) | Next folder |
| **Ctrl+Shift+Up** | Unigram (undocumented) | Previous folder |

### Message actions

| Shortcut | Category | Action |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Copy the message if it contains text. If the focus is on a link, the link will be copied |
| **ALT+Q** | UnigramPlus | Press "Instant view" button, if it is included in the current message |
| **ALT+Delete** | UnigramPlus | Delete a message or chat |
| **Shift+Delete** | UnigramPlus | Delete message or chat from both sides |
| **Delete** | Unigram (undocumented) | Delete the selected or focused message |
| **Ctrl+ALT+C** | UnigramPlus | Open comments |
| **Enter** | UnigramPlus | Reply to message |
| **ALT+F** | UnigramPlus | Forward message |
| **Backspace** | UnigramPlus | Edit message |
| **ALT+Shift+R** | UnigramPlus | Mark a chat as read |
| **Ctrl+Space** | UnigramPlus | Switch to selection mode |
| **Unassigned** | UnigramPlus | Save file as... |
| **Unassigned** | UnigramPlus | Pin a message or chat |
| **Left Arrow** | UnigramPlus | Announce the original message, the message that was replied to |
| **Right Arrow** | UnigramPlus | Move to the next media attachment in the focused message |
| **ALT+C** | UnigramPlus | Show message text in popup window |
| **ALT+W** | UnigramPlus | Announces the time a message was sent or received, as well as a list of reactions. Double-clicking toggles the announcement mode for this information. |
| **ALT+[** | UnigramPlus | Toggle whether message headers are announced before or after the message content |
| **NVDA+Ctrl+0-9** | UnigramPlus | Review one of the ten most recent messages; 1 is the newest and 0 is the tenth newest |
| **Ctrl+Shift+A** | UnigramPlus | Press "Attach file" button |
| **Ctrl+Shift+E** | Unigram (undocumented) | Open emoji picker |
| **Ctrl+Shift+G** | Unigram (undocumented) | Open GIF picker |
| **Ctrl+Shift+S** | Unigram (undocumented) | Open sticker picker |
| **Ctrl+O** | Unigram (undocumented) | Open file picker to send documents |
| **Ctrl+N** | UnigramPlus | Press "New conversation" button |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Voice messages and media

| Shortcut | Category | Action |
|---|---|---|
| **ALT+P** | UnigramPlus | Play/pause the voice message currently playing |
| **ALT+S** | UnigramPlus | Increase/decrease the playback speed of voice messages |
| **ALT+E** | UnigramPlus | Close audio player |
| **NVDA+ALT+R** | UnigramPlus | Convert voice message to text |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | Fast forward a voice message |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | Rewind voice message |

### Record notes

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+R** | Unigram | Start record |
| **Ctrl+R (again)** | Unigram | Send recorded |
| **Ctrl+D** | Unigram | Stop recording |
| **Space (while recording) / Ctrl+P** | Unigram | Pause recording |

### Calls

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+Home** | Unigram | Accept incoming call |
| **Ctrl+End** | Unigram | Reject incoming call |
| **Ctrl+Page Up** | Unigram | Toggle camera |
| **Ctrl+Page Down** | Unigram | Toggle microphone |
| **ALT+Shift+C** | UnigramPlus | Call if it's a contact, or enter a voice chat if it's a group |
| **ALT+Shift+V** | UnigramPlus | Press the video call button |
| **ALT+Y** | UnigramPlus | Accept call |
| **ALT+N** | UnigramPlus | Press "Decline call" button if there is an incoming call, "End call" button if a call is in progress or leave voice chat if it is active. |
| **ALT+A** | UnigramPlus | Press "Mute/unmute microphone" button |
| **ALT+V** | UnigramPlus | Press "Enable/disable camera" button |

### Other shortcuts

| Shortcut | Category | Action |
|---|---|---|
| **Ctrl+0** | Unigram | Saved messages |
| **Ctrl+W** | Unigram | Close current window |
| **Ctrl+Q** | Unigram | Close Unigram (main window only) |
| **Ctrl+Shift+Y** | Unigram | Change status |
| **Ctrl+Shift+W** | Unigram (undocumented) | Stop media playback |
| **Ctrl+F4** | Unigram (undocumented) | Close current window |
| **Ctrl+L** | Unigram (undocumented) | Lock Unigram |
| **Ctrl+M** | Unigram (undocumented) | Minimize Unigram |
| **Ctrl+J** | Unigram (undocumented) | Open downloads |
| **ALT+T** | UnigramPlus | Announce the name and status of an open chat |
| **NVDA+Alt+V** | UnigramPlus | Open Unigram and UnigramPlus version information in a read-only window |
| **ALT+M** | UnigramPlus | Open navigation menu |
| **ALT+Shift+M** | UnigramPlus | Open Unigram settings |
| **ALT+Shift+P** | UnigramPlus | Open current chat profile |
| **ALT+L** | UnigramPlus | Enable automatic reading of new messages in the current chat |
| **ALT+H** | UnigramPlus | Show a list of all UnigramPlus shortcuts |
| **ALT+U** | UnigramPlus | Toggle progress bar announcements |
| **ALT+Shift+L** | UnigramPlus | Copy data for broadcasting to the clipboard |
| **NVDA+ALT+U** | UnigramPlus | Open UnigramPlus settings window |
<!-- shortcut-table-end -->

## List of changes:

### Version 5.8.6

* Space plays, opens and downloads the media of a message again in Unigram 13.0 and later. Since Unigram 13.0 the content of a photo, video, GIF, file, song or voice message is itself the button that does this. Unigram 13.0.1 gave that button back the identifier UnigramPlus looks for, except on voice messages, where the identifier went to the voice-to-text button, so Space did nothing on a voice message. UnigramPlus now recognizes a voice message's own button by the download progress it reports. Unigram 13.1.1 still has no Space action for a message outside selection mode, so UnigramPlus presses that button: Space plays or pauses a voice message or a song, opens a photo, video or GIF in the viewer, and downloads or opens a file.
* After Space plays a voice message or a song or downloads a file, the focus stays on the message, and the next Escape no longer moves it back there. Only the viewer needs that, but in Unigram 13.0 and later a file or a song is as wide as a photo, so UnigramPlus took it for one.
* Space no longer opens stickers or link previews. Unigram 13.0.1 gave them the same identifier as media buttons, but they are links. In a link preview that shows a photo or video, Space still opens the photo or video.
* Right and Left Arrow on a message with several media attachments, such as an album, announce each photo, video, file or song again in Unigram 13.0 and later. Since Unigram 13.0 each attachment holds only its content's own button, so UnigramPlus no longer found what tells a photo from a video and announced the placeholder word "Медіа" for every attachment. It now looks inside that button: a video has its own download button there, a file or song its title, and a photo neither.
* Ctrl+Space now also works in the chat list, where it did nothing before. As with messages, the first press starts selection mode with the focused chat from the chat's context menu, and after that each press selects or unselects the focused chat, the way Space does in Unigram. UnigramPlus then announces whether the chat is selected. Unselecting the last selected chat ends selection mode. While the chat list is in selection mode, UnigramPlus also says "Selected" before the name of a selected chat when the focus moves to it, as it does for messages.
* Added Alt+Shift+M, which opens Unigram's settings in Unigram 13.1 and later, as UnigramPlusRussianMod does. Unigram 13.1 moved Settings from the side pane to a tab below the chat list. Alt+Shift+M selects that tab and then moves the focus to the top of the settings: to the first of your other accounts, or to Add account if you are signed in to only one account. In Unigram versions before 13.1, and in a narrow window that shows only the open chat, UnigramPlus reports "Settings not available".

### Version 5.8.5

* Alt+M opens the navigation menu again in Unigram 13.1 and later. Unigram 13.1 replaced the side pane with a menu that opens from the same button, and that button is no longer a toggle button, so UnigramPlus did not find it and reported "Navigation menu not available".
* Fixed Ctrl+Space in Unigram's selection mode. There the context menu of a selected message has no Select command, so UnigramPlus moved through the menu without finding it, and the message stayed selected. Ctrl+Space now works as in Unigram 13.1.1: the first press still starts selection mode from the context menu, and after that each press selects or unselects the focused message, the way Space does in Unigram. UnigramPlus then announces whether the message is selected. Unselecting the last selected message ends selection mode.
* In selection mode, Space and Enter on a message now select or unselect it, as in Unigram, instead of playing its media or looking for Reply in the context menu, and Backspace no longer looks for Edit there.
* Updated compatibility for NVDA 2026.3. UnigramPlus no longer uses deprecated parts of the NVDA API, which NVDA still supports but may remove in a later version: the message boxes of the update check, the old way of opening the UnigramPlus settings, and a key constant used when seeking in voice messages.
* Updated the Polish and Vietnamese translations.

### Version 5.8.4

* When "Automatically move focus to the chat list when Unigram starts" is on, the focus now stays in a popup that Unigram shows as it starts, such as the request to join a group opened from an invite link. Since version 5.6.1, UnigramPlus moved the focus from the popup to the chat list behind it, so the popup was skipped.
* Updated the Vietnamese translation.

### Version 5.8.3

* Removed the Enter and Space handling that UnigramPlus added to the list of Unigram settings categories in version 4.8.0. In Unigram 13.0 and later, each settings category is a button that opens with Enter or Space by itself, and the focus lands on that button rather than on the list item the add-on handled, so the handling no longer applied there. When you open a category, the focus now stays on it, as in Unigram itself, instead of moving into the category. The handling had also caught other tab lists, such as the Emoji, GIFs and Stickers tabs, and intercepted Enter and Space there; these keys now reach Unigram there as well.
* In Unigram settings, Alt+1 now moves the focus to the open settings category, or to the first category if none is open. It used to look for the category list at a fixed position on the settings page and then tried to focus an element that cannot receive the focus in Unigram 13.0.
* Removed code that could no longer run, with no change in use. Before Unigram 9.5, some list items were announced by an internal class name, which UnigramPlus replaced with a readable one; Unigram 9.5 renamed those classes, so the replacements never matched again. The handler that opened a quiz explanation in a separate window, disabled since version 5.2.0, was removed as well.
* Updated the Polish and Vietnamese translations.

### Version 5.8.2

* Fixed NVDA errors with the new WinUI 3 beta of Unigram. Since version 5.5.6, an error was logged every time you switched back to Unigram or typed with an input method (IME), such as one for Chinese, Japanese or Korean. The UWP version of Unigram was not affected.
* UnigramPlus no longer interferes with focus announcements in Telegram Desktop when the Telegram Desktop add-on is not installed.
* Removed the notification UnigramPlus gave when a voice or video message recording was canceled. Unigram 13.0 and later announce a canceled recording themselves, whether it is canceled with Ctrl+D or the cancel button, so it is no longer heard twice. A recording that is slow to appear in the chat is no longer reported as canceled either. Starting and sending a recording are still announced, and the setting for them is now called "Notification when a voice message recording starts or is sent".
* Updated the Polish and Vietnamese translations.

### Version 5.8.1

* Removed the call duration workaround. Unigram 12.10 and later announce the duration of a call message themselves, so UnigramPlus no longer adds it and it is no longer heard twice.
* Fixed the add-on failing to start on older NVDA versions that do not provide the utils.security module.
* Removed imports that the add-on no longer uses.
* Updated the Vietnamese translation.

### Version 5.8.0

* The add-on's recurring background checks no longer run on NVDA's main loop, so chat navigation, typing and speech are no longer held up while Unigram answers.
* Every behavior added after 5.4 can now be turned on or off in UnigramPlus settings, gathered under one heading: how the voice message record button is announced, rich message text with ALT+C, the profile identity button label, the replying and editing announcement in the message field, the suppressed "list" announcement before messages, the live microphone and camera state during a call, and the unread count when switching chat folders. Each keeps its current behavior by default, and each label states which version 5.4 behavior it restores.
* Fixed the space bar not playing voice messages, music and files.
* Fixed Enter not replying to a message, Backspace not editing it, ALT+C not showing its text, and ALT+D not returning to it.
* Fixed ALT+E not closing the audio player.
* Fixed Ctrl+ALT+Left and Ctrl+ALT+Right not seeking voice message playback, including when the arrow is pressed again while the modifiers stay held.
* Canceling a voice recording is announced about a second and a half after it stops, instead of five seconds later.
* With the version 5.4 record button option selected, the focus stays in the message field when a recording starts, while Tab still reaches the record button.
* Fixed a range of shortcuts failing silently when Unigram's tree was missing an element they assumed was there: ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Shift+L, ALT+Shift+P, Shift+Delete, media navigation and the call controls.
* Converting a voice message to text no longer starts a new thread every half second while it waits, and gives up instead of waiting for ever.

### Version 5.7.3

* NVDA+Alt+V displays the UnigramPlus version on a new line.

### Version 5.7.2

* NVDA+Alt+V now opens Unigram and UnigramPlus version information in a read-only, multiline window.

### Version 5.7.1

* Fixed Unigram 12.10.2 reaction buttons being treated as messages, so message navigation shortcuts no longer override their native Toggle action.

### Version 5.7.0

* Restored folder-switch announcements with a nonzero unread count while retaining the file-transfer progress tracker safeguards.
* Updated the shortcut lists from the current Unigram source and identified built-in shortcuts not yet listed in Unigram's official Shortcuts.md.

### Version 5.6.9

* Fixed an error that could occur when NVDA entered a secure desktop, such as a UAC prompt, while UnigramPlus background message tracking was enabled.
* Fixed Saved Messages topic rows in Unigram 12.10.1+ being treated as messages merely because their native summaries contain sent or received timestamps.
* Removed the obsolete Saved Messages topic name workaround; current Unigram versions now provide accessible names for Saved Messages chats natively.
* Updated compatibility for NVDA 2026.2.
* Updated Polish and Burmese translations.

### Version 5.6.8

* Fixed Alt+C failing when WhatsApp Enhancer is installed due to an appModules helper module name collision.

### Version 5.6.7

* Changed the shortcut for announcing the installed Unigram and UnigramPlus versions from NVDA+Shift+V to NVDA+Alt+V to avoid shortcut conflicts.
* Fixed Shift+Delete for deleting chats and leaving groups or channels in current Unigram versions, including automatic popup confirmation handling.

### Version 5.6.6

* Added NVDA+Shift+V to announce the installed Unigram and UnigramPlus versions.
* Removed the temporary Unigram 12.9 inline-button workaround after Unigram 12.9.1 fixed button labels; this avoids UIA stalls in bot lists, message navigation, reactions, and the chat list.
* Updated all translations and manuals for version 5.6.6.

### Version 5.6.5

* Fixed Enter for replying to messages and Alt+Shift+R for marking chats as read in current Unigram versions.
* Removed the web view mode and its setting; Alt+C now always opens message text in the original wx popup window.
* Updated all translations and manuals for version 5.6.5.

### Version 5.6.4

* Fixed Shift+Delete by using Unigram's native Delete command and automatically confirming deletion for both sides.
* Alt+2 now activates Unigram's Go to bottom button first; the duplicate Alt+End shortcut was removed.
* Added a setting to choose between the classic wx window (default) and web view when displaying message text with Alt+C.
* Unigram's official rich-message text is now used, with a temporary fix for unlabeled inline buttons in Unigram 12.9.
* Updated the shortcut list from the official Unigram 12.9 documentation.
* Added a temporary fix so Saved Messages topic rows announce the visible chat title instead of a TDLib type name.

### Version 5.6.3

* Fixed an intermittent issue where NVDA announced "list" before a message while navigating with the Up and Down Arrow keys.
* Added a setting for the Alt+[ behavior that announces message headers after their content; it is disabled by default.
* Added an optional sound notification when reaching the end of a chat.

### Version 5.6.2

* Fixed Ctrl+Alt+Left/Right so they seek the current voice message playback again.
* Fixed Alt+I so it moves to Unigram's inline chat search results list.
* Added Alt+[ to announce message headers after the content, so file names can be announced before sender names in profile media sections.

### Version 5.6.1

* Fixed file-transfer progress tracking so it stops at 100% and no longer creates a new thread on every polling cycle.
* When Unigram opens, focus now moves automatically to the chat list.
* Added Ctrl+Alt+Up/Down to move through chats with unread mentions.

### Version 5.6.0

* Fixed rich-message detection so sticker and emoji messages are no longer incorrectly announced as rich messages.
* Ctrl+R now uses Unigram's native voice-message recording and sending behavior while retaining UnigramPlus recording start and end notifications.
* Updated localizations.

### Version 5.5.9

* Added support for rich messages. Rich messages are announced when focused and can be opened with Alt+C in a browseable window.
* Links and mixed content are preserved, and links can be activated from the browseable window.

### Version 5.5.8

* Fixed automatic updates: releases are now retrieved securely from GitHub and the downloaded add-on is validated before installation.

* Restored compatibility with Unigram 12.7, where several shortcuts and announcements had stopped working.
* Poll messages again announce the question and the answer options.
* The forum topic list again announces the last message preview.
* During a one-to-one call, the mute microphone (ALT+A), enable or disable camera (ALT+V) and end call (ALT+N) shortcuts work again.
* ALT+End again moves to the latest message in the chat.

### Version 5.5.7

* Reorganized the keyboard shortcuts section into categorized tables and combined Unigram and UnigramPlus shortcuts.
* When recording a voice or video message, NVDA now announces "Recording a voice message" or "Recording a video message" along with the elapsed time, instead of "Tn voice message".

### Version 5.5.6
* Fixed the identity button in a group or channel profile announcing "Identity root" when tabbing past the name; it now announces the chat name and member count.
* Ctrl+C is no longer handled twice: it copies the link when the focus is on a link, and otherwise lets Unigram copy the message.

### Version 5.5.5
* Replying to or editing a message is now announced in the message input field instead of the usual message prompt.
* Fixed the typing indicator sound sometimes continuing to play after the app was closed, after the other person stopped typing, or after leaving the chat; it now stops as soon as no one is typing in the open chat.
* Updated Burmese localization.

### Version 5.5.4

* Fixed unwanted announcements such as chat folder unread counts, for example "All 535". File transfer progress is now restricted to Unigram upload and download controls and is ignored outside Unigram windows.
* Fixed coexistence with the Telegram Desktop NVDA add-on by enabling UnigramPlus only when the running application is detected as Unigram.
* Added a button in UnigramPlus settings to open the bundled sounds folder, making it easier to replace sound files with custom WAV files that use the same names.
* Added an up-arrow option for the message edit field that moves focus to the last focused message.
* Rebuilt Traditional Chinese as zh_TW and added Simplified Chinese as zh_CN.

### Version 5.5.3

* Added automatic announcement of file upload and download progress. A new option "Only during upload and download" was added to the progress bar announcement setting and is now the default. The ALT+U hotkey now cycles between three states: off, only during upload/download, and announce all progress bars.
* Updated the readme and translations.

### Version 5.5.2

* Updated the readme and translations.
* Changed the typing indicator sound.

### Version 5.5.1

* Fixed the hotkey for navigating through the list of group topics (ALT+6). Now it correctly detects the topic list when a forum group is opened from the chat list.
* Added a typing indicator sound: a sound plays in a loop while the other side is typing inside a chat and stops when they finish. This feature is inspired by the corresponding feature in the Unigram JAWS script.

### Version 5.5.0

* Added compatibility with NVDA 2026.1.

### Version 5.4.2

* Added compatibility with NVDA 2025.3.3.

### Version 5.4.1

* Added compatibility with NVDA 2025.1.2.

### Version 5.4.0

* Fixed an issue with the chat list.

### Version 5.3.0

* Added a keyboard shortcut that announces the sending time or receiving time of a message and reactions in the message. This is useful when you want to hear the sending or receiving time of a message without re-listening to the full text of the message beforehand. By default, this is the ALT W key combination. Double-clicking toggles the mode of announcing this information.
* Fixed all the issues that have accumulated recently as a result of changes in the Unigram interface.
* Changed the keyboard shortcut for opening a user profile to ALT shift P.
* Changed the keyboard shortcuts for navigating to the next and previous search results to F3 and shift F3, as in most applications.
* Added compatibility with NVDA 2024.4.

### Version 5.2.5

* Compatibility of the add-on with the latest version of Unigram has been implemented.

### Version 5.2.0

* Added the ability to select files attached to messages with horizontal arrows and open the selected file with the space bar.
* Now links in messages will not be read in full, but only up to the question mark.
* Now, when you close the photo or video viewer, UnigramPlus will try to set the focus on the message you were viewing.
* The keyboard shortcut to open UnigramPlus settings has been changed. Now this function is assigned to the combination NVDA+ALT+U.
* Code optimisation has been done, resulting in significantly improved response time when navigating the chat list and message list. This is especially noticeable on messages that contain many nested elements.
* Many minor issues have been fixed.
* A lot of outdated code has been removed.

### Version 5.1.0

* Added keyboard shortcuts for navigating to the next and previous search results in chat. By default, these functions are assigned to the ALT+K and ALT+J key combinations.
* Added a keyboard shortcut for opening a list with all the search results in chat. By default, this function is assigned to the ALT+I key combination.
* Now, double-pressing the left arrow on a message will shift focus to the message that the current message is replying to.
* Fixed an issue where descriptions of links embedded in messages were not being read.
* UnigramPlus will no longer suggest updates on protected screens. However, users will need to open NVDA settings one more time and click the "Use the last saved settings during login and reading of protected screens (administrator rights required)" button.
* Removed the feature for rewinding voice messages and the feature for setting reactions to messages, as these features were not working reliably.
* Removed the message copying feature, as Unigram now has this function. Be aware that sometimes copying messages may cause a slight freezing of the program, but this is not related to UnigramPlus.
* Fixed some other minor bugs.

### Version 5.0.0

* Fixed an issue where messages in chats were being read twice.
* Fixed an issue where the shortcut to navigate to an open profile was not correctly functioning.
* Fixed an issue where the keyboard shortcut to open the navigation menu didn't work.
* Resolved all issues with the button for enabling/disabling the microphone in voice chats.
* Fixed an issue in the Polish language where inputting a character was blocked by the ALT+C combination.
* Corrected the pronunciation of the phrases "Owner" and "Administrator" in messages.
* Addressed several other minor issues.

### Version 4.9.0

* Added an option to change the behavior when pressing the up arrow in an empty message edit field. You can choose from the following options: activate the function of editing the last sent message, move the focus to the last message in the chat or do nothing.
* Fixed answering and rejecting calls using hotkeys.
* Fixed minor issues such as the ALT+H key combination not working And an issue when the message to which the reply was written was not spoken when pressing the left arrow.
* Fixed display of some elements.

### Version 4.8.0

* Now in the Unigram settings, the settings categories can be opened by pressing Enter. When you open any category of settings, the focus will be placed on that category.
* Now, when clicking the "Explanation" button in quizzes, the explanation text will open in a separate window for convenient viewing.
* Fixed an issue where chat folder names were not spoken when switching between them.
* Fixed a bug that made it impossible to disable or change the order of speaking the chat type and name.
* Fixed the issue when it was not possible to find out the correct answer in quizzes.
* Fixed the problem with copying a message using the control+shift+C combination.
* Made several minor fixes, improvements, and code optimizations.

### Version 4.7.0

* UnigramPlus is now adapted to the latest version of Unigram.
* Compatibility with NVDA-2023 is now ensured.
* The keyboard shortcut ALT+1 now moves focus not only to the chat list, but also to the contact list and settings section list.
* The automatic announcement of new messages in the chat and the automatic sounding of chat activity have been significantly revised, resulting in improved stability.
* A keyboard shortcut has been added to display all UnigramPlus commands. By default, this function is assigned to ALT+H.
* Several minor issues have also been fixed.

### Version 4.6.0

* Added a keyboard shortcut to move focus to list of group threads. By default, this function is assigned to the ALT+6 combination. Please note that often when pressing the enter key on the group that we want to open, the list of threads may not be displayed and then it is necessary to set the focus on this group again and press the enter key. As a rule, after the second press, a list of threads is displayed, and after that we can press a key combination that will move the focus to this list.
* Now the ALT+2 combination moves the focus not only to the list with messages, but also to the open profile, to the open list of group threads, or to the open section with settings.
* Now in the UnigramPlus settings, you can disable the pronunciation of the phrases "Admin" and "Owner" on messages in groups.
* Combinations for accepting and rejecting calls now work correctly.
* Now the automatic announcement feature for new messages and the chat activity will not turn off when NVDA is restarted, but will work until you turn it off yourself.
* Improved display of some interface elements.

### Version 4.5.0

* Adapted to the latest version of Unigram
* Now if a message was sent in response to another message, by pressing the left arrow key, you can hear the text of the message in response to which it was sent
* Added French localization
* Removed the ability to add reactions to messages with keyboard shortcuts, since I was unable to adapt this function to changes in the Unigram interface
* Fixed some minor bugs

### Version 4.4.0

* The function of announcing activity in chats has been added. By default, this function is activated by double-pressing the ALT+T combination. The function remains active only until NVDA is restarted.
* The function of automatic announcements of new messages in the chat has been added. By default, this function is activated by pressing ALT+L. The feature remains active only until NVDA is restarted. There may be stability issues if too many new messages quicly appear in the chat.
* Added a keyboard shortcut for the function of converting voice messages to text. By default, this function is assigned to the NVDA+ALT+R combination. Please note that in cases where the voice message is very long, then the conversion to text takes place in parts. That is, it may happen that when Unigramplus notifies you that the conversion is complete, only part of the voice message will actually be converted. And after a few seconds, this text will be added.
* Now, when navigating through the chat list, UnigramPlus reports information about premium accounts and verified accounts.

### Version 4.3.0

* Now UnigramPlus works correctly when several chats are open in different windows.
* Added keyboard shortcut to move focus to user profile area if it is open. The default gesture is alt+5.
* Fixed minor bugs.

### Version 4.4.0

* The mechanism for saving UnigramPlus settings has been significantly redesigned. Now the settings will not be stored in the NVDA config file, but will be stored in its own config file. This should solve the problem when users after an update or just suddenly UnigramPlus stopped working, due to problems accessing the NVDA config file. Unfortunately, users will have to re-configure UnigramPlus for themselves, as after installing this update, all settings will be reset.
* Fixed UnigramPlus compatibility issue with BluetoothAudio add-on.
* Now the information that the message is not selected will not be reported. If a message is selected, information about it will be announced before the message content.
* Now the order number of the elements in the chat will be announced if you have enabled the element position in the NVDA settings.
* Added labels to some buttons.

### Version 4.1.0

* Added a gesture to pin a message or chat. By default, no keyboard shortcut are assigned to this feature.
* Added a keyboard shortcut for pressing the "New conversation" button. The default gesture for this feature is ctrl+n.
* Added a keyboard shortcut for pressing the "Attach media" button. The default gesture is ctrl+shift+a.
* Added a keyboard shortcut to go to the list of chat folders. The default gesture is alt+4. This feature will be useful for those who use more than nine chat folders.
* Now, when switching between folders using the arrows, the focus will not jump anywhere.
* Now, when switching between folders using hotkeys, in addition to the name of the active folder, the number of unread chats in this folder will be announced.
* Now features such as "Mark a chat as read" and "Pin a message or chat" will also work in reverse.
* Added Romanian localization.

### Version 4.0.0

* Provided compatibility with Unigram 8.8. Since the Unigram interface has changed, I had to rewrite a significant part of the addon code.
* Added the ability to rewind and fast forward voice messages. To fast forward, use the combination control+right arrow, and to rewind, use control+left arrow.
* Now UnigramPlus will report not only the presence of reactions in messages, but also announce detailed information about reactions.
* Added the ability to view the text of the message in the popup window. The default gesture for this feature is ALT+C.
* Added keyboard shortcut to open UnigramPlus settings window. The default gesture for this feature is NVDA+control+U
* Added Czech and Romanian localizations.
* Fixed issue with UnigramPlus update for Ukrainian residents.

### Version 3.2.3

* Added Chinese localization.
* Updated existing localizations, including English.
* Fixed minor bugs.

### Version 3.2.0

* Removed features such as "Chat activity tracking" and "Read new messages in open chat" because I was unable to get them to work properly in NVDA 2022.1.
* Improved accessibility of mute / unmute and turn on / off camera in calls. Now, after pressing the shortcut for both functions, their status will be announced.
* Fixed an issue where the Enter key was not working properly on some elements. Now you can still record voice messages by holding the Enter key on the record button.
* You can now reassign keyboard shortcuts to features such as "Reply to message" and "Edit message". You can also assign these functions to keys such as Enter, Backspace or even left or right arrows, and it won't interfere with those keys on other items. Note that no keys will be assigned to these features at first, but you will only be able to assign them when the focus is on one of the chat messages.
* Now the function "Say the sender's name" should work more correctly.
* When you focus on a link contained in a message, the message text will not be spoken first, but the link text will be spoken immediately.
* made many small improvements and fixed many bugs and shortcomings.
* Now UnigramPlus should run noticeably faster.

### Version 3.1.0

* Poll announcement has been improved. The names of users who have taken surveys are now announced in the results window. Polls will also provide information on which option was correct.
* The ability to react to messages has been added, but only in private chats. This feature will not work properly in groups and channels. In private chats, by pressing NVD + ALT + numbers from 1 to 5, you can type the following reactions: 1 - 👍, 2 - 👎, 3 - ❤, 4 - 🔥, 5 - 🥰.
* Added the ability to announce information about existing replies to messages. Unfortunately, it is not yet possible to announce the name of the available reactions.
* Added hotkey to quickly copy data needed for broadcasts.
* Fixed an issue with displaying inline results that appeared in the latest versions of Unigram.

### Version 3.0.0

Warning! UnigramPlus will now support NVDA versions no older than 21.2.0.
* Added labels for many UI elements.
* Fixed some bugs.

### Version 2.9.0

* Now the edit field will change its label depending on whether we are replying to the message or editing it.
* Added the ability to enable a confirmation dialog for deleting messages or chats using hotkeys in the settings.
* Added Serbian localization.
* Fixed small issues.

### Version 2.8.0

* Added the ability to update the add-on from within the add-on. Now, in order to check for updates and install them, just open the UnigramPlus settings and click the appropriate button. You can also enable automatic check for updates on NVDA startup.
* Added Arabic localization.

### Version 2.7.0

* You will now be notified that the message has been forwarded.
* Improved message copy function. Now, if the text contains a clickable link and the focus is on that link, pressing CTRL+C will copy the link instead of the entire text.
* Added hotkey for copying messages while maintaining text formatting. This function emulates the activation of the corresponding item in the application menu. The default hotkey for this feature is CTRL+shift+C. Because of this feature, the hotkey for opening comments has been changed to CTRL+ALT+C.
* Added the ability to automatically announce new messages in open chat. By default, it can be enabled by pressing ALT + L.
* Added hotkeys for quick viewing of chat messages. Press NVDA + CTRL + the number corresponding to the number of a particular message in reverse order, that is, if you want to view the last message, press 1, if you want to view the previous message, press 2, etc.
* Now pressing ALT+T will give you information about the active voice chat in the current group.

### Version 2.6.0

* Provided compatibility with NVDA 21.3.
* Added hotkey to enable selecting messages or chats.
* Added hotkey for forwarding messages.
* Added hotkey for marking a chat as read.
* Improved performance of the existing features.


### Version 2.5.0

* There is now a checkbox that, if checked, fixes the voice message recording issue that some users are experiencing.
* Added a hotkey for replying to a message.  You can do it by pressing Enter on the message or you can reassign the alternative hotkeys for this feature to something else.
* Added hotkey for editing messages. The default keyboard shortcut is ALT+Backspace.

### Version 2.4.0

* You will now hear the sender's name when focusing on a message.
* When focusing on a group chat that contains unread messages, you will be notified if there are replies for you in that group.
* The performance of features added in the previous update has also been improved.

### Version 2.3.0

* Improved accessibility of messages containing multiple media attachments. Previously, the caption of a message containing more than one media attachment could only be accessed using object navigation. Now this caption will be read immediately after focusing on such a message.
* Improved accessibility of messages containing polls. Now when you focus on such a message, you will hear the number of people who have already voted, as well as all the answer options with the result for each option.
* Improved accessibility of messages containing URLs. Now, if the URL has a description, it will also be read, i.e., for example, if the message has a URL for YouTube, the title and description for that video will be read right after the URL itself. Also, if the URL is longer than 30 characters, it will be shortened to make the following description easier to read.
* Improved accessibility of the inline query results panel.. To navigate through the results of inline queries, use the following combinations: control+up and control+down.
* Added hotkey to open comments.

### Version 2.2.0

* Added hotkey to delete messages or chats just for you and also on both sides. This function is related to the Unigram interface language, so it may not work in some localizations. In the settings you can choose the type of notifications, text or sound.
* Added the ability to specify which interface language you use in Unigram in settings. This is necessary for the correct operation of functions associated with certain localizations.
* Added hotkey to open current chat profile.
* Now, after closing a chat, the focus will move to the list of chats, and not to the button "Open navigation menu".

### Version 2.1.0

* When switching between folders in the chat list, the name of the current folder will be announced.
* In the chat list, you hear the name of the chat, followed by its type.
* Improved the function of moving focus to the list of chats. Now it should work more accurately and without delays.
* Now the add-on settings have become even more flexible, because a section with some UnigramPlus options has appeared in the NVDA Preferences menu.
* Added Polish localization.
* Many small fixes and improvements.

### Version 2.0.0

* The feature where the word "Seen" is not announced and the word "Not seen" is spoken before the message content is read now works in Spanish, Portuguese, Croatian, Turkish and Persian localizations.
* Improved the function of progress bar announcements. Now, when this mode is enabled, not all progress indicators are announced, but only those that are in focus.
* If you press the spacebar in a message that contains a file that has not completed downloading, you will be notified that the download has been paused.
* Added Portuguese localization.
* Fixed some small issues and improved performance.

### Version 1.9.0
* A hotkey has been added that toggles the level of progress bar announcement between values such as: "Announce all progress bars", "Announce some progress bars", "Announce all progress bars except the voice message playback progress bar" and "Do not announce any progress bars". For those users who have automatic media downloads disabled in Unigram, the progress bar announcement level can be set to "Announce all progress bars except the voice message playback progress bar", and for those who have it enabled, it is better to set it to "Do not announce progress bars".
* Added Spanish, Croatian and Persian localizations.
* Fixed minor bugs from previous versions.

### Version 1.8.0

* The name and size of the file will be spoken when the cursor is focused on the "Open File" button or the "Download File" button, and when the cursor is focused on the play button of the audio file, you will hear its name and duration.
* Added hotkey to move focus to edit field. If the focus is already in the edit field, then after pressing the hot key, it will move to where it was before.
* The chat activity tracking feature is now enabled by double pressing ALT + T. You can simply turn it on or turn it on temporarily until the next time you close the application.
* Added the ability to select the type of notification for recording voice messages. This is done by double pressing the control+d hotkey. There you can choose between sound, text notification, or return to the standard voice message recording behavior.

### Version 1.7.0

Significantly improved the function of recording voice messages. Recording, sending and canceling the recording of a voice message are accompanied by characteristic sounds. Also, when performing these functions, the focus remains in its position and does not jump to either the record button or the message input field.

### Version 1.7.0

* Added the ability to track chat activity. This option can be enabled by pressing ALT+shift+T and remains active until Unigram is closed or NVDA is next restarted.
* The hotkey that activates the "More Options" button now works in the voice chat window and the call window.

### Version 1.6.0

* If the media attached to the message is opened using the spacebar, after closing it, the focus will return to the last element that was in focus.
* Now you can return to the active voice chat not only from the current group, but also from any other chat.
* Pressing ALT+shift+C in an open chat will return you to the voice chat instead of calling the contact.
* If a message has not been sent, you will be notified as soon as that message has been focused.
* If the focused message contains a link, you'll only hear the text of the link itself, not the entire message.
* Fixed an issue where status changes for buttons such as Mute/Unmute Mic and Enable/Disable Camera were not reported in private calls and voice chats.
* Now the message copy function allows you to copy the contents of items in the message quick view window.

### Version 1.5.1

This update fixes a huge number of bugs and improves the performance of the add-on.

### Version 1.5.0

This update adds a hotkey that clicks the "Instant View" button in a message if included in the message. By default, this feature is activated with the ALT+Q hotkey. After opening such an article, the focus will automatically go to the first element of this article, and after closing, the focus will return to the last viewed message. We also fixed an issue where not all article elements in the Instant View window were readable, even if they contained text content.

### Version 1.1.7

Added Turkish localization.
