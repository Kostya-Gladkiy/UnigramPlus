# Unigram Plus

* 作者：Kostya Gladkiy（Ukraine）
* [Telegram 频道](https://t.me/unigramPlus)
* Telegram：@unigramPlus
* 赞助链接：[https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)
* PayPal：gladkiy.kostya@gmail.com

UnigramPlus 让 Unigram 更容易通过 NVDA 操作。它提供许多快捷键，可快速移到聊天列表、消息列表、聊天文件夹、个人资料和搜索结果，也改善消息、媒体、语音消息、通话和删除操作的读出与焦点行为。

## 主要改进
* 改善投票、链接、附加媒体和语音消息的读出。
* 在聊天列表和消息列表中减少不必要的控件描述，让焦点读出更简洁。
* 在打开或下载文件按钮上读出文件名称和大小；在音频播放按钮上读出名称和时长。
* 开始录制和发送语音消息时可使用文本或声音通知，取消录制则由 Unigram 13.0 及更高版本自行读出；焦点会保留在原位置。
* 使用空格键打开消息中的媒体后，关闭查看器时会尽量回到先前的焦点。
* 进度条读出可设置为全部、仅限文件上传和下载，或完全关闭。
* 可在设置中选择空白消息编辑字段按上方向键时的操作。

## 将 Unigram 界面切换为简体中文
1. 按下「Open navigation menu」（打开导航菜单）按钮。
2. 进入「Settings」（设置）。
3. 进入「Language」（语言）。
4. 在语言列表中选择「简体中文, Chinese (Simplified)」，接着按一次 `Tab`，再按一次空格键即可应用。

## 自定义声音
UnigramPlus 的声音文件位于插件的 `appModules\media` 文件夹。请打开 NVDA 设置 > UnigramPlus，按下 **打开 UnigramPlus 声音文件夹**。若要自定义声音，请将替换用的 WAV 文件放入此文件夹，并使用与要取代的声音完全相同的文件名，然后重启 NVDA 或重新加载插件。插件更新可能会还原内置声音，建议另外保留自定义文件备份。

<!-- shortcut-table-start -->
## 快捷键清單

> “类别”栏中，“UnigramPlus”表示插件提供的快捷键，“Unigram”表示 Unigram 内置的快捷键。

> 「Unigram（官方文档未列出）」表示当前 Unigram 源码已实现、但官方 Shortcuts.md 尚未列出的快捷键。

> [!TIP]
> 您可以通过“NVDA 菜单 → 选项 → 输入手势”自定义 UnigramPlus 快捷键。

### 切换聊天

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | 下一个聊天 |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | 上一个聊天 |
| **Ctrl+Alt+Home** | Unigram（官方文档未列出） | 第一个聊天 |
| **Ctrl+Alt+End** | Unigram（官方文档未列出） | 最后一个聊天 |
| **Ctrl+Alt+Up/Down** | UnigramPlus | 移到下一个或上一个含未读提及的聊天 |
| **ALT+1** | UnigramPlus | 将焦点移到聊天列表 |
| **ALT+2** | UnigramPlus | 将焦点移到已打开聊天中的最后一条消息 |
| **ALT+3** | UnigramPlus | 将焦点移到“未读消息”标签 |
| **ALT+4** | UnigramPlus | 将焦点移到聊天文件夹列表 |
| **ALT+5** | UnigramPlus | 将焦点移到已打开的个人资料 |
| **ALT+6** | UnigramPlus | 将焦点移到群组话题列表 |
| **ALT+D** | UnigramPlus | 将焦点移到编辑字段。如果焦点已在编辑字段中，按下快捷键后会移回先前所在的位置 |

### 搜索

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+E** | Unigram | 搜索聊天 |
| **Ctrl+F** | Unigram | 搜索当前聊天中的消息 |
| **Ctrl+Shift+F** | Unigram（官方文档未列出） | 搜索聊天 |
| **Search key** | Unigram（官方文档未列出） | 在当前页面中搜索 |
| **ALT+I** | UnigramPlus | 转到搜索结果列表 |
| **F3** | UnigramPlus | 转到下一个搜索结果 |
| **Shift+F3** | UnigramPlus | 转到上一个搜索结果 |

### 输入区中选中的文本

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+Z** | Unigram | 撤消 |
| **Ctrl+Y** | Unigram | 重做 |
| **Ctrl+Shift+Z** | Unigram（官方文档未列出） | 重做 |
| **Alt+X** | Unigram（官方文档未列出） | 将选中的四位十六进制数字转换为对应字符 |
| **Ctrl+X** | Unigram | 剪切 |
| **Ctrl+C** | Unigram | 复制 |
| **Ctrl+V** | Unigram | 粘贴 |
| **Ctrl+A** | Unigram | 全选 |
| **Ctrl+Shift+.** | Unigram | 引用 |
| **Ctrl+B** | Unigram | 粗体 |
| **Ctrl+I** | Unigram | 斜体 |
| **Ctrl+U** | Unigram | 下划线 |
| **Ctrl+Shift+X** | Unigram | 删除线 |
| **Ctrl+Shift+M** | Unigram | 等宽 |
| **Ctrl+Shift+P** | Unigram | 遮罩 |
| **Ctrl+K** | Unigram | 创建链接 |
| **Ctrl+Shift+N** | Unigram | 清除格式 |

### 聊天文件夹

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+1** | Unigram | 第一个文件夹（所有聊天） |
| **Ctrl+2** | Unigram | 第二个文件夹 |
| **Ctrl+3** | Unigram | 第三个文件夹 |
| **Ctrl+4** | Unigram | 第四个文件夹 |
| **Ctrl+5** | Unigram | 第五个文件夹 |
| **Ctrl+6** | Unigram | 第六个文件夹 |
| **Ctrl+7** | Unigram | 第七个文件夹 |
| **Ctrl+8** | Unigram | 第八个文件夹 |
| **Ctrl+9** | Unigram | 归档 |
| **Ctrl+Shift+Down** | Unigram（官方文档未列出） | 下一个文件夹 |
| **Ctrl+Shift+Up** | Unigram（官方文档未列出） | 上一个文件夹 |

### 消息操作

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Space** | UnigramPlus | 播放或停止焦点所在的语音或视频消息，或打开消息附加的媒体 |
| **Ctrl+C** | UnigramPlus | 如果消息包含文本则复制消息；如果焦点位于链接上，则复制该链接 |
| **ALT+Q** | UnigramPlus | 如果当前消息中包含“即时预览”按钮，则按下它 |
| **ALT+Delete** | UnigramPlus | 删除消息或聊天 |
| **Shift+Delete** | UnigramPlus | 为双方删除消息或聊天 |
| **Delete** | Unigram（官方文档未列出） | 删除选中或焦点所在的消息 |
| **Ctrl+ALT+C** | UnigramPlus | 打开评论 |
| **Enter** | UnigramPlus | 回复消息 |
| **ALT+F** | UnigramPlus | 转发消息 |
| **Backspace** | UnigramPlus | 编辑消息 |
| **ALT+Shift+R** | UnigramPlus | 将聊天标记为已读 |
| **Ctrl+Space** | UnigramPlus | 切换到选择模式 |
| **Unassigned** | UnigramPlus | 文件另存为... |
| **Unassigned** | UnigramPlus | 置顶消息或聊天 |
| **Left Arrow** | UnigramPlus | 读出原始消息，也就是所回复的消息 |
| **Right Arrow** | UnigramPlus | 移到焦点消息中的下一个媒体附件 |
| **ALT+C** | UnigramPlus | 在弹出窗口中显示消息文本 |
| **ALT+W** | UnigramPlus | 读出消息的发送或接收时间，以及回应列表。连按两次可切换是否读出此信息。 |
| **ALT+[** | UnigramPlus | 切换在消息内容之前或之后读出消息标头 |
| **NVDA+Ctrl+0-9** | UnigramPlus | 读出最近十条消息之一；1 是最新消息，0 是第十条消息 |
| **Ctrl+Shift+A** | UnigramPlus | 按下“附加文件”按钮 |
| **Ctrl+Shift+E** | Unigram（官方文档未列出） | 打开表情符号选择器 |
| **Ctrl+Shift+G** | Unigram（官方文档未列出） | 打开 GIF 选择器 |
| **Ctrl+Shift+S** | Unigram（官方文档未列出） | 打开贴纸选择器 |
| **Ctrl+O** | Unigram（官方文档未列出） | 打开文件选择器以发送文件 |
| **Ctrl+N** | UnigramPlus | 按下“新建对话”按钮 |
| **Arrow Up** | Unigram | 编辑上一条已发送消息 |
| **Ctrl+Arrow Up** | Unigram | 回复上一条已发送消息 |
| **Esc / Alt+Arrow Left** | Unigram | 返回 |
| **Alt+Arrow Right** | Unigram | 前进 |

### 语音消息与媒体

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **ALT+P** | UnigramPlus | 播放或暂停当前正在播放的语音消息 |
| **ALT+S** | UnigramPlus | 提高或降低语音消息播放速度 |
| **ALT+E** | UnigramPlus | 关闭音频播放器 |
| **NVDA+ALT+R** | UnigramPlus | 将语音消息转换为文本 |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | 快进语音消息 |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | 倒回语音消息 |

### 录制消息

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+R** | Unigram | 开始录制 |
| **Ctrl+R (again)** | Unigram | 发送录制内容 |
| **Ctrl+D** | Unigram | 停止录制 |
| **Space (while recording) / Ctrl+P** | Unigram | 暂停录制 |

### 通话

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+Home** | Unigram | 接听来电 |
| **Ctrl+End** | Unigram | 拒绝来电 |
| **Ctrl+Page Up** | Unigram | 切换相机 |
| **Ctrl+Page Down** | Unigram | 切换麦克风 |
| **ALT+Shift+C** | UnigramPlus | 如果是联系人则拨打电话，如果是群组则进入语音聊天 |
| **ALT+Shift+V** | UnigramPlus | 按下视频通话按钮 |
| **ALT+Y** | UnigramPlus | 接听来电 |
| **ALT+N** | UnigramPlus | 如果有来电则按下“拒绝通话”按钮；如果正在通话则按下“结束通话”按钮；如果语音聊天处于活动状态则离开语音聊天。 |
| **ALT+A** | UnigramPlus | 按下“麦克风静音或取消静音”按钮 |
| **ALT+V** | UnigramPlus | 按下“启用或禁用摄像头”按钮 |

### 其他快捷键

| 快捷键 | 类别 | 操作 |
|---|---|---|
| **Ctrl+0** | Unigram | 我的收藏 |
| **Ctrl+W** | Unigram | 关闭当前窗口 |
| **Ctrl+Q** | Unigram | 关闭 Unigram（仅限主窗口） |
| **Ctrl+Shift+Y** | Unigram | 更改状态 |
| **Ctrl+Shift+W** | Unigram（官方文档未列出） | 停止媒体播放 |
| **Ctrl+F4** | Unigram（官方文档未列出） | 关闭当前窗口 |
| **Ctrl+L** | Unigram（官方文档未列出） | 锁定 Unigram |
| **Ctrl+M** | Unigram（官方文档未列出） | 最小化 Unigram |
| **Ctrl+J** | Unigram（官方文档未列出） | 打开下载 |
| **ALT+T** | UnigramPlus | 读出已打开聊天的名称和状态 |
| **NVDA+Alt+V** | UnigramPlus | 在只读窗口中打开 Unigram 和 UnigramPlus 的版本信息 |
| **ALT+M** | UnigramPlus | 打开导航菜单 |
| **ALT+Shift+M** | UnigramPlus | 打开 Unigram 设置 |
| **ALT+Shift+P** | UnigramPlus | 打开当前聊天的个人资料 |
| **ALT+L** | UnigramPlus | 启用当前聊天中新消息的自动读出 |
| **ALT+H** | UnigramPlus | 显示所有 UnigramPlus 快捷键列表 |
| **ALT+U** | UnigramPlus | 切换进度条读出 |
| **ALT+Shift+L** | UnigramPlus | 将广播数据复制到剪贴板 |
| **NVDA+ALT+U** | UnigramPlus | 打开 UnigramPlus 设置窗口 |
<!-- shortcut-table-end -->

## 版本变更

### 版本 5.8.6

* 在 Unigram 13.0 及更高版本中，空格键又能播放、打开和下载消息中的媒体了。从 Unigram 13.0 起，照片、视频、GIF、文件、音乐或语音消息的内容本身就是执行这些操作的按钮。Unigram 13.0.1 为这个按钮恢复了 UnigramPlus 用来识别它的标识符，但在语音消息上，这个标识符却给了语音转文字按钮，因此在语音消息上按空格键没有任何作用。现在 UnigramPlus 会根据语音消息本身的按钮所报告的下载进度来识别它。Unigram 13.1.1 在选择模式以外仍不会处理消息上的空格键，因此由 UnigramPlus 按下这个按钮：空格键会播放或暂停语音消息或音乐，在查看器中打开照片、视频或 GIF，以及下载或打开文件。
* 用空格键播放语音消息或音乐、或下载文件后，焦点会停留在该消息上，下一次按 Esc 也不会再把焦点移回那里。只有查看器才需要这样做，但在 Unigram 13.0 及更高版本中，文件或音乐和照片一样宽，因此 UnigramPlus 误把它当成了照片。
* 空格键不会再打开贴纸或链接预览。Unigram 13.0.1 给了它们和媒体按钮相同的标识符，但它们其实是链接。在显示照片或视频的链接预览中，空格键仍会打开该照片或视频。
* 在 Unigram 13.0 及更高版本中，在含有多个媒体附件的消息（例如相册）上按右、左方向键，又能读出每张照片、每个视频、文件或音乐了。从 Unigram 13.0 起，每个附件里只有其内容本身的按钮，因此 UnigramPlus 找不到用来区分照片和视频的部分，对每个附件都只读出占位词“Медіа”。现在它会查看该按钮内部：视频在那里有自己的下载按钮，文件或音乐有其标题，而照片两者都没有。
* Ctrl+Space 现在在聊天列表中也能使用了，以前在这里按下没有任何作用。和消息一样，第一次按下会从该聊天的上下文菜单进入选择模式，并选中当前焦点所在的聊天；之后每按一次就会选中或取消选中当前焦点所在的聊天，就像在 Unigram 中按空格键一样，随后 UnigramPlus 会报告聊天是否已选中。取消选中最后一个已选中的聊天会退出选择模式。聊天列表处于选择模式时，焦点移到已选中的聊天上，UnigramPlus 也会在聊天名称前读出“已选中”，和消息一样。
* 新增 Alt+Shift+M，可在 Unigram 13.1 及更高版本中打开 Unigram 设置，与 UnigramPlusRussianMod 相同。Unigram 13.1 把设置从侧边窗格移到了聊天列表下方的一个标签页。Alt+Shift+M 会选中这个标签页，然后把焦点移到设置的最上方：移到第一个其他账号；如果只登录了一个账号，就移到“添加账号”。在 Unigram 13.1 之前的版本中，以及在只显示当前聊天的窄窗口中，UnigramPlus 会报告“设置不可用”。

### 版本 5.8.5

* 在 Unigram 13.1 及更高版本中，Alt+M 又能打开导航菜单了。Unigram 13.1 将侧边窗格改为从同一个按钮打开的菜单，并且该按钮不再是切换按钮，因此 UnigramPlus 找不到它，只会报告“导航菜单不可用”。
* 修复了 Ctrl+Space 在 Unigram 选择模式中的问题。在选择模式中，已选中消息的上下文菜单没有“选择”命令，因此 UnigramPlus 会在菜单中一路往下找却找不到，消息也一直保持选中。现在 Ctrl+Space 的工作方式与 Unigram 13.1.1 相同：第一次按下仍会从上下文菜单进入选择模式，之后每按一次就会选中或取消选中当前焦点所在的消息，就像在 Unigram 中按空格键一样，随后 UnigramPlus 会报告消息是否已选中。取消选中最后一条已选中的消息会退出选择模式。
* 在选择模式中，在消息上按空格键和 Enter 现在会像在 Unigram 中一样选中或取消选中该消息，而不是播放其中的媒体或在上下文菜单中查找“回复”；按 Backspace 也不会再去那里查找“编辑”。
* 更新了与 NVDA 2026.3 的兼容性。UnigramPlus 不再使用 NVDA 已弃用的 API，这些 API 目前仍受支持，但以后的版本可能会将其移除：更新检查的消息框、打开 UnigramPlus 设置的旧方法，以及调整语音消息播放位置时使用的按键常量。
* 更新波兰语和越南语翻译。

### 版本 5.8.4

* 启用“Unigram 启动时自动将焦点移到聊天列表”后，焦点现在会停留在 Unigram 启动时显示的弹出窗口中，例如从邀请链接打开的申请加入群组窗口。自 5.6.1 版起，UnigramPlus 会把焦点从弹出窗口移到其后方的聊天列表，导致弹出窗口被跳过。
* 更新越南语翻译。

### 版本 5.8.3

* 移除 UnigramPlus 自 4.8.0 版起为 Unigram 设置类别列表添加的 Enter 和空格键处理。在 Unigram 13.0 及更高版本中，每个设置类别都是一个按钮，按 Enter 或空格键即可自行打开，焦点也会落在该按钮上，而不是插件所处理的列表项，因此这项处理已不再生效。现在打开类别后，焦点会像 Unigram 本身一样停留在该类别上，不会再移入类别内容。这项处理此前也会作用于其他标签页列表（例如表情符号、GIF 和贴纸标签页），并拦截其中的 Enter 和空格键；现在这些按键在那里也会交由 Unigram 处理。
* 在 Unigram 设置中，Alt+1 现在会将焦点移到当前打开的设置类别；如果没有打开任何类别，则移到第一个类别。此前它会在设置页面的固定位置查找类别列表，然后尝试将焦点移到一个在 Unigram 13.0 中无法获得焦点的元素。
* 移除已无法执行的代码，使用上没有任何变化。Unigram 9.5 之前，部分列表项会以内部类名朗读，UnigramPlus 会将其替换为易懂的名称；Unigram 9.5 更改了这些类的名称，因此这些替换再也不会生效。另外也移除了自 5.2.0 版起已停用、用于在单独窗口中打开测验解释的处理程序。
* 更新波兰语和越南语翻译。

### 版本 5.8.2

* 修正新版 Unigram WinUI 3 测试版的 NVDA 错误。自 5.5.6 版起，每次切回 Unigram 或使用中文、日文、韩文等输入法（IME）输入文字时，NVDA 都会记录一条错误。Unigram 的 UWP 版本不受影响。
* 未安装 Telegram Desktop 插件时，UnigramPlus 不再干扰 Telegram Desktop 的焦点朗读。
* 移除 UnigramPlus 在取消录制语音或视频消息时发出的通知。无论是按 Ctrl+D 还是取消按钮取消录制，Unigram 13.0 及更高版本都会自行读出，因此不会再重复读出；较慢出现在聊天中的录音也不会再被误报为已取消。开始录制和发送仍会通知，相关设置现在称为“开始录制或发送语音消息时的通知方式”。
* 更新波兰语和越南语翻译。

### 版本 5.8.1

* 移除通话时长的临时处理。Unigram 12.10 及更高版本会自行读出通话消息的时长，因此 UnigramPlus 不再补充，也不会重复读出。
* 修正在缺少 utils.security 模块的旧版 NVDA 上插件无法启动的问题。
* 移除插件不再使用的导入。
* 更新越南语翻译。

### 版本 5.8.0

* 插件的周期性后台检查不再运行于 NVDA 主循环，因此 Unigram 响应期间不会再拖慢聊天导航、输入和朗读。
* 5.4 之后新增的所有行为现在都可以在 UnigramPlus 设置中开关，并集中在同一个标题下：语音消息录制按钮的读出方式、用 ALT+C 读出消息的富文本、个人资料身份按钮的标签、消息编辑字段中回复与编辑的读出、消息前“列表”读出的抑制、通话中麦克风和摄像头的实时状态，以及切换聊天文件夹时的未读数量。每一项默认保持当前行为，并在标签中说明它恢复的是 5.4 的哪一种行为。
* 修正空格键无法播放语音消息、音乐和文件的问题。
* 修正 Enter 无法回复消息、Backspace 无法编辑消息、ALT+C 无法显示消息文本、ALT+D 无法返回消息的问题。
* 修正 ALT+E 无法关闭音频播放器的问题。
* 修正 Ctrl+ALT+左/右无法调整语音消息播放进度的问题，包括在按住修饰键的情况下再次按方向键。
* 取消语音录制的提示改为停止后约一秒半读出，而不是五秒后。
* 选择 5.4 版录制按钮选项时，开始录制后焦点会留在消息编辑字段，同时 Tab 仍可到达录制按钮。
* 修正多个快捷键在 Unigram 树中缺少预期元素时静默失效的问题：ALT+3、ALT+4、ALT+5、ALT+6、ALT+Q、ALT+T、ALT+Shift+L、ALT+Shift+P、Shift+Delete、媒体导航和通话控件。
* 语音消息转文字在等待期间不再每半秒启动一个新线程，并会放弃等待而不是无限等待。

### 版本 5.7.3

* NVDA+Alt+V 现在会在新的一行显示 UnigramPlus 版本。

### 版本 5.7.2

* NVDA+Alt+V 现在会在只读多行窗口中打开版本信息。

### 版本 5.7.1

* 修复了 Unigram 12.10.2 中反应按钮被当作消息处理的问题，因此消息导航快捷键不再覆盖其原生切换操作。

### 版本 5.7.0

* 恢复了切换文件夹时朗读非零未读数量的功能，同时保留文件传输进度跟踪器的保护范围。
* 根据当前 Unigram 源码更新了快捷键列表，并标明官方 Shortcuts.md 尚未列出的内置快捷键。

### 版本 5.6.9

* 修复了当 NVDA 进入安全桌面（例如 UAC 提示）且启用了 UnigramPlus 后台消息跟踪时可能发生的错误。
* 修复 Unigram 12.10.1+ 将“已保存消息”主题行仅因原生摘要包含发送或接收时间而误判为消息的问题。
* 移除了过时的“已保存消息”主题名称临时解决方法；当前版本的 Unigram 现已原生为“已保存消息”聊天提供无障碍名称。
* 更新了与 NVDA 2026.2 的兼容性。
* 更新了波兰语和缅甸语翻译。

### 版本 5.6.8

* 修复安装 WhatsApp Enhancer 时因 appModules 辅助模块名称冲突导致 Alt+C 失效的问题。

### 版本 5.6.7

* 为避免快捷键冲突，将读出已安装 Unigram 和 UnigramPlus 版本的快捷键从 NVDA+Shift+V 改为 NVDA+Alt+V。
* 修复了在当前 Unigram 版本中使用 Shift+Delete 删除聊天以及退出群组或频道的问题，包括自动处理弹出窗口确认。

### 版本 5.6.6

* 新增 NVDA+Shift+V，用于读出已安装的 Unigram 和 UnigramPlus 版本。
* Unigram 12.9.1 已修复按钮标签，因此移除了针对 Unigram 12.9 内联按钮的临时解决方案；这可避免机器人列表、消息导航、回应和聊天列表中的 UIA 卡顿。
* 已更新 5.6.6 版的所有翻译和手册。

### 版本 5.6.5

* 修复了当前 Unigram 版本中按 Enter 回复消息以及按 Alt+Shift+R 将聊天标记为已读的问题。
* 移除了 Web 视图模式及其设置；Alt+C 现在始终在原始 wx 弹出窗口中打开消息文本。
* 已将所有翻译和说明文档更新至版本 5.6.5。

### 版本 5.6.4

* 修复 Shift+Delete：现在使用 Unigram 原生 Delete 命令，并自动确认从双方删除。
* Alt+2 现在会优先激活 Unigram 的“转到底部”按钮；已移除重复的 Alt+End 快捷键。
* 新增设置，可选择在按 Alt+C 显示消息文本时使用经典 wx 窗口（默认）或 Web 视图。
* 现在使用 Unigram 官方提供的富消息无障碍文本，并为 Unigram 12.9 中无标签的内联按钮加入临时修复。
* 根据 Unigram 12.9 官方文档更新了快捷键列表。
* 加入临时修复，使“已保存的消息”主题行朗读可见的聊天标题，而不是 TDLib 类型名称。

### 版本 5.6.3

* 修复了使用上、下箭头在消息间移动时，NVDA 偶尔会在消息前读出“列表”的问题。
* 新增 Alt+[ 功能的设置：在消息内容之后读出消息标头；该功能默认关闭。
* 新增到达聊天末尾时的可选声音提示。

### 版本 5.6.2

* 修复 Ctrl+Alt+Left/Right Arrow 在语音消息播放期间无法倒回或快进的问题。
* 修复 Alt+I，使其可转到聊天搜索结果的内嵌列表。
* 新增 Alt+[，用于切换在消息内容之前或之后读出消息标头。将标头置于内容之后时，“文件”分区会先读出文件名。

### 版本 5.6.1

* 修复文件传输进度跟踪：进度达到 100% 时停止，并且不再于每次轮询时创建新线程。
* 打开 Unigram 时，焦点现在会自动移到聊天列表。
* 新增 Ctrl+Alt+Up/Down，用于在含未读提及的聊天之间移动。

### 版本 5.6.0

* 修复富消息识别，贴纸和表情符号消息不再被错误地朗读为富消息。
* Ctrl+R 现使用 Unigram 原生的语音消息录制和发送行为，同时保留 UnigramPlus 的录制开始与结束提示。
* 更新本地化翻译。

### 版本 5.5.9

* 新增富文本消息支持。富文本消息获得焦点时会被朗读，并可按 Alt+C 在浏览窗口中打开。
* 富文本消息中的链接和混合内容会被保留，且可在浏览窗口中激活链接。

### 版本 5.5.8

* 修复自动更新：现在会从 GitHub 安全获取版本，并在安装前验证下载的插件。

* 修复与 Unigram 12.7 的兼容性，此前有多个快捷键和语音提示失效。
* 投票消息会再次朗读问题和答案选项。
* 论坛话题列表会再次朗读最后一条消息的预览。
* 一对一通话中，静音麦克风（ALT+A）、开启或关闭摄像头（ALT+V）和结束通话（ALT+N）的快捷键可再次使用。
* ALT+End 会再次移动到聊天中最新的消息。

### 版本 5.5.7

* 将快捷键区段重新整理为分类表格，并整合 Unigram 与 UnigramPlus 快捷键。
* 录制语音或视频消息时，NVDA 现在会朗读「正在录制语音消息」或「正在录制视频消息」并念出经过时间，而不再是「Tn voice message」。

### 版本 5.5.6

* 修复在群组或频道个人资料中，按 Tab 越过名称后，身份按钮被读成“Identity root”的问题；现在会读出聊天名称与成员数。
* control+C 不再被处理两次：焦点在链接上时复制链接，其他情况则交由 Unigram 复制消息。

### 版本 5.5.5

* 回复或编辑消息时，现在会在消息输入字段中提示“回复”或“编辑”，而不是平常的消息输入提示。
* 修复在关闭应用程序后、对方停止输入后，或离开聊天后，输入声音有时仍持续播放的问题；现在只要已打开的聊天中没有人在输入，声音就会立即停止。
* 更新缅甸语本地化。

### 版本 5.5.4

* 修复聊天文件夹未读数量变化被不必要读出的问题，例如“所有聊天 535”。文件传输进度现在只会在 Unigram 的上传和下载控件中读出，且会忽略非 Unigram 窗口。
* 修复与 Telegram Desktop NVDA 插件的冲突；只有检测到当前运行的应用程序是 Unigram 时，才会启用 UnigramPlus。
* 在 UnigramPlus 设置中新增打开内置声音文件夹的按钮，方便用户以相同文件名替换自定义 WAV 声音文件。
* 在消息编辑字段的上方向键操作中，新增“移到最后获得焦点的消息”选项。
* 繁体中文重新整理并独立为 zh_TW，另新增简体中文 zh_CN。

### 版本 5.5.3

* 新增文件上传和下载进度的自动读出。进度条读出设置新增“仅在上传和下载时”选项，并设为默认值。ALT+U 现在会在关闭、仅限上传下载、读出全部进度条三种状态间切换。
* 更新自述文件和翻译。

### 版本 5.5.2

* 更新自述文件和翻译。
* 更改输入中提示声音。

### 版本 5.5.1

* 修复移到群组话题列表的快捷键 ALT+6。
* 新增输入中提示音：当对方在已打开聊天中输入时循环播放，停止输入后结束播放。
