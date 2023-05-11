# Unigram Plus

* Author: Kostya Gladkiy (Ukrain)
* Download [stable version][1] (Compatible with NVDA 2021.2 to 2023.1)
* [Telegram channel][2]
* [Donation link][3]
* PayPal: gladkiy.kostya@gmail.com

## about

Use Unigram in a more comfortable and productive way. This addon provides many hotkeys for a quick and comfortable use of Unigram and makes a lot of small improvements.

## Some of the major improvements are:

* Adds a significant improvement to the display of messages such as a poll, a link, or a message with attached media.
* When focus enters the list of chats, it removes such phrases as: "chats, tab, selected list". And when the focus hits the list of messages, the phrase "list".
* The name and size of the file will be spoken when the cursor is focused on the "Open File" button or the "Download File" button, and when the cursor is focused on the play button of the audio file, you will hear its name and duration.
* When focus is placed on a voice message that is currently being played, first information about the time of its playback is announced, and then all other information.
* When the focus is on a message that contains information about a call, the duration of this call is announced.
* When focusing on a selected message in a chat, you will first hear the information that it is selected, and then the content of the message.
* Now, when moving in the chat, the phrase "Seen" will not be pronounced at all, and the phrase "Not seen" will be pronounced before the content of the message. This feature currently only works in English, Russian, Ukrainian, Spanish, Portuguese, Polish, Croatian, Turkish, and Persian.
* Significantly improved the function of recording voice messages. Recording, sending and canceling the recording of a voice message are accompanied by characteristic sounds.
* Also, when performing these functions, the focus remains in its position and does not jump to either the record button or the message input field.
* If the media attached to the message is opened using the spacebar, then after closing it, the focus will return to the last element that was in focus.
* The add-on allows you to completely disable the announcement of progress bars, as well as disable only the announcement of the progress bar for playing voice messages.

## Information about the opportunity to donate to the developer:

If you really like this add-on and you have the desire, and most importantly the opportunity, to financially support the developer and thereby motivate him to further develop this add-on, you can do this by transferring a small amount to the following bank details: [donation link][3], or card number is 5169360009004502(Ukraine).

And remember that everyone who read this line thought that someone will definitely support the developer, but it will not be me.

## Hotkey list:

* ALT+1: Move focus to chat list;
* ALT+2: Move focus to the last message in an open chat;
* ALT+3: Move focus to "unread messages" label;
* ALT+D: Move the focus to the edit field. If the focus is already in the edit field, then after pressing the hotkey, it will move to where it was before;
* ALT+T: Announce the name and status of an open chat;
* space: Play/stop the focused voice or video message, or open a media file attached to the current message;
* ALT+P: Play/pause the voice message currently playing;
* ALT+S: Increase/decrease the playback speed of voice messages;
* ALT+E: Close audio player;
* control+C: Copy the message if it contains text. If the focus is on a link, the link will be copied;
* ALT+shift+C: Call if it's a contact, or enter a voice chat if it's a group;
* ALT+shift+V: Press the video call button;
* ALT+Y: Accept call;
* ALT+N: Press the \"Decline call\" button if there is an incoming call, the \"End call\" button if the call is in progress, or leave the voice chat if it is active;
* ALT+A: Press \"Mute/unmute microphone\" button;
* ALT+C: Press "Enable/disable camera" button;
* ALT+Q: Press \"Instant view\" button, if it is included in the current message;
* ALT+O: Press "More Options" button in an open chat, voice chat, or call window;
* ALT+M: Open navigation menu;
* control+R: Start/stop voice message recording;
* control+D: If pressed once, cancels the recording of a voice message. If pressed twice, changes the notification type when starting, sending, or canceling a voice message recording;
* ALT+U: Toggle progress bar announcements;
* control+P: Open current chat profile;
* delete: Delete a message or chat;
* shift+delete: Delete message or chat from both sides;
* control+ALT+C: Open comments;
* Unassigned: Reply to message;
* ALT+F: Forward message;
* Unassigned: Edit message;
* ALT+shift+R: Mark a chat as read;
* control+space: Switch to selection mode;
* control+shift+C: Copy messages with formatting preserved;
* ALT+shift+L: Copy data for broadcasting to the clipboard;
* control+ALT+right arrow: Fast forward a voice message.
* control+ALT+left arrow: Rewind voice message.
* ALT+C: Show message text in popup window.
* NVDA+control+U: Open UnigramPlus settings window
* ALT+4: Move focus to list of chat folders.
* control+shift+A: Press "Attach file" button.
* control+N: Press "New chat" button.
* Unassigned: Pin a message or chat.
* ALT+5: Move focus to open profile.
* ALT+L: Enable automatic reading of new messages in the current chat.
* NVDA+ALT+R: Convert voice message to text.
* Left arrow: Announce the original message, the message that was replied to.
* ALT+6: Move focus to the list of group threads.
* ALT+H: Show a list of all UnigramPlus keyboard shortcuts.

### Note

* All hotkeys can be reassigned in NVDA menu, preferences, input gestures.
* The fact that the function that focuses the cursor on the "unread message" label can sometimes react with a delay is a known issue. This may depend on the number of cash messages at the moment.

## List of changes:

### Version 4.8.3

* Fixed an issue that caused the keyboard shortcut to open the navigation menu to not work.

### Version 4.8.1

* UnigramPlus has been adapted to be compatible with the NVDA add-on store format.
* Minor fixes in the English documentation.

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
* The automatic announcement of new messages in chat, as well as the announcement of chat actions, have been significantly redesigned, resulting in improved stability.
* A keyboard shortcut has been added to display all UnigramPlus commands. By default, this function is assigned to ALT+H.
* Several minor issues have also been fixed.

### Version 4.6.0

* Added a keyboard shortcut to move focus to list of group threads. By default, this function is assigned to the ALT+6 combination. Please note that often when pressing the enter key on the group that we want to open, the list of threads may not be displayed and then it is necessary to set the focus on this group again and press the enter key. As a rule, after the second press, a list of threads is displayed, and after that we can press a key combination that will move the focus to this list.
* Now the ALT+2 combination moves the focus not only to the list with messages, but also to the open profile, to the open list of group threads, or to the open section with settings.
* Now in the UnigramPlus settings, you can disable the pronunciation of the phrases "Admin" and "Owner" on messages in groups.
* Hotkeys for accepting and declining calls now work correctly.
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

[1]: https://github.com/Kostya-Gladkiy/UnigramPlus/releases/download/4.8.1/UnigramPlus-4.8.1.nvda-addon

[2]: https://t.me/unigramPlus

[3]: https://unigramplus.diaka.ua/donate
