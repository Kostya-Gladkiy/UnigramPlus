# Unigram Plus

* 作者：Kostya Gladkiy（Ukraine）
* [Telegram 頻道](https://t.me/unigramPlus)
* Telegram：@unigramPlus
* 贊助連結：[https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)
* PayPal：gladkiy.kostya@gmail.com

UnigramPlus 讓 Unigram 更容易以 NVDA 操作。它提供許多快速鍵，可快速移到聊天清單、訊息清單、聊天資料夾、個人資料與搜尋結果，也改善訊息、媒體、語音訊息、通話與刪除操作的讀出與焦點行為。

## 主要改善
* 改善投票、連結、附加媒體與語音訊息的讀出。
* 在聊天清單與訊息清單中減少不必要的控制項描述，讓焦點讀出更乾淨。
* 在開啟或下載檔案按鈕上讀出檔案名稱與大小；在音訊播放按鈕上讀出名稱與長度。
* 開始錄製與傳送語音訊息時可使用文字或音效通知，取消錄製則由 Unigram 13.0 及更新版本自行讀出；焦點會留在原位置。
* 使用空格鍵開啟訊息中的媒體後，關閉檢視器時會盡量回到先前的焦點。
* 進度列讀出可設定為全部、只限檔案上傳與下載，或完全關閉。
* 可在設定中選擇空白訊息編輯欄位按上方向鍵時的動作。

## 將 Unigram 介面切換為正體中文
1. 按下「Open navigation menu」（開啟導覽功能表）按鈕。
2. 進入「Settings」（設定）。
3. 進入「Language」（語言）。
4. 在語言清單中選擇「繁體中文, Chinese (Traditional)」，接著按一次 `Tab`，再按一次空格鍵即可套用。

## 自訂音效
UnigramPlus 的音效檔案位於附加元件的 `appModules\media` 資料夾。請開啟 NVDA 設定 > UnigramPlus，按下 **開啟 UnigramPlus 音效資料夾**。若要自訂音效，請將替換用的 WAV 檔案放入此資料夾，並使用與要取代的音效完全相同的檔名，然後重新啟動 NVDA 或重新載入附加元件。附加元件更新可能會還原內建音效，建議另外保留自訂檔案備份。

<!-- shortcut-table-start -->
## 快速鍵清單

> 「類別」欄位中，「UnigramPlus」表示附加元件提供的快速鍵，「Unigram」表示 Unigram 內建的快速鍵。

> 「Unigram（官方說明未列出）」表示目前 Unigram 原始碼已實作、但官方 Shortcuts.md 尚未列出的快速鍵。

> [!TIP]
> 您可以透過「NVDA 功能表 → 偏好 → 輸入手勢」自訂 UnigramPlus 快速鍵。

### 切換聊天

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | 下一個聊天 |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | 上一個聊天 |
| **Ctrl+Alt+Home** | Unigram（官方說明未列出） | 第一個聊天室 |
| **Ctrl+Alt+End** | Unigram（官方說明未列出） | 最後一個聊天室 |
| **Ctrl+Alt+Up/Down** | UnigramPlus | 移到下一個或上一個含未讀提及的聊天 |
| **ALT+1** | UnigramPlus | 將焦點移到聊天清單 |
| **ALT+2** | UnigramPlus | 將焦點移到已開啟聊天中的最後一則訊息 |
| **ALT+3** | UnigramPlus | 將焦點移到「未讀訊息」標籤 |
| **ALT+4** | UnigramPlus | 將焦點移到聊天資料夾清單 |
| **ALT+5** | UnigramPlus | 將焦點移到已開啟的個人資料 |
| **ALT+6** | UnigramPlus | 將焦點移到群組主題清單 |
| **ALT+D** | UnigramPlus | 將焦點移到編輯欄位。若焦點已在編輯欄位中，按下快速鍵後會移回先前所在的位置 |

### 搜尋

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+E** | Unigram | 搜尋聊天 |
| **Ctrl+F** | Unigram | 搜尋目前聊天中的訊息 |
| **Ctrl+Shift+F** | Unigram（官方說明未列出） | 搜尋聊天 |
| **Search key** | Unigram（官方說明未列出） | 搜尋目前頁面 |
| **ALT+I** | UnigramPlus | 移至搜尋結果清單 |
| **F3** | UnigramPlus | 移至下一個搜尋結果 |
| **Shift+F3** | UnigramPlus | 移至上一個搜尋結果 |

### 輸入區中選取的文字

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+Z** | Unigram | 復原 |
| **Ctrl+Y** | Unigram | 取消復原 |
| **Ctrl+Shift+Z** | Unigram（官方說明未列出） | 重做 |
| **Alt+X** | Unigram（官方說明未列出） | 將選取的四位十六進位數字轉換為對應字元 |
| **Ctrl+X** | Unigram | 剪下 |
| **Ctrl+C** | Unigram | 複製 |
| **Ctrl+V** | Unigram | 貼上 |
| **Ctrl+A** | Unigram | 全選 |
| **Ctrl+Shift+.** | Unigram | 引用 |
| **Ctrl+B** | Unigram | 粗體 |
| **Ctrl+I** | Unigram | 斜體 |
| **Ctrl+U** | Unigram | 底線 |
| **Ctrl+Shift+X** | Unigram | 刪除線 |
| **Ctrl+Shift+M** | Unigram | 等寬 |
| **Ctrl+Shift+P** | Unigram | 防劇透 |
| **Ctrl+K** | Unigram | 建立連結 |
| **Ctrl+Shift+N** | Unigram | 清除格式 |

### 聊天資料夾

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+1** | Unigram | 第一個資料夾（所有聊天） |
| **Ctrl+2** | Unigram | 第二個資料夾 |
| **Ctrl+3** | Unigram | 第三個資料夾 |
| **Ctrl+4** | Unigram | 第四個資料夾 |
| **Ctrl+5** | Unigram | 第五個資料夾 |
| **Ctrl+6** | Unigram | 第六個資料夾 |
| **Ctrl+7** | Unigram | 第七個資料夾 |
| **Ctrl+8** | Unigram | 第八個資料夾 |
| **Ctrl+9** | Unigram | 封存 |
| **Ctrl+Shift+Down** | Unigram（官方說明未列出） | 下一個資料夾 |
| **Ctrl+Shift+Up** | Unigram（官方說明未列出） | 上一個資料夾 |

### 訊息操作

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Space** | UnigramPlus | 播放或停止焦點所在的語音或視訊訊息，或開啟訊息附加的媒體 |
| **Ctrl+C** | UnigramPlus | 若訊息包含文字則複製訊息；若焦點位於連結上，則複製該連結 |
| **ALT+Q** | UnigramPlus | 若目前訊息包含「即時檢視」按鈕，則按下它 |
| **ALT+Delete** | UnigramPlus | 刪除訊息或聊天 |
| **Shift+Delete** | UnigramPlus | 在雙方刪除訊息或聊天 |
| **Delete** | Unigram（官方說明未列出） | 刪除選取或焦點所在的訊息 |
| **Ctrl+ALT+C** | UnigramPlus | 開啟留言 |
| **Enter** | UnigramPlus | 回覆訊息 |
| **ALT+F** | UnigramPlus | 轉傳訊息 |
| **Backspace** | UnigramPlus | 編輯訊息 |
| **ALT+Shift+R** | UnigramPlus | 將聊天標示為已讀 |
| **Ctrl+Space** | UnigramPlus | 切換到選取模式 |
| **Unassigned** | UnigramPlus | 另存檔案為... |
| **Unassigned** | UnigramPlus | 置頂訊息或聊天 |
| **Left Arrow** | UnigramPlus | 讀出原始訊息，也就是回覆所針對的訊息 |
| **Right Arrow** | UnigramPlus | 移到焦點訊息中的下一個媒體附件 |
| **ALT+C** | UnigramPlus | 在快顯視窗顯示訊息文字 |
| **ALT+W** | UnigramPlus | 讀出訊息的傳送或接收時間，以及反應清單。連按兩次可切換是否讀出此資訊。 |
| **ALT+[** | UnigramPlus | 切換在訊息內容之前或之後讀出訊息標頭 |
| **NVDA+Ctrl+0-9** | UnigramPlus | 讀出最近十則訊息之一；1 是最新訊息，0 是第十則訊息 |
| **Ctrl+Shift+A** | UnigramPlus | 按下「附加檔案」按鈕 |
| **Ctrl+Shift+E** | Unigram（官方說明未列出） | 開啟表情符號選擇器 |
| **Ctrl+Shift+G** | Unigram（官方說明未列出） | 開啟 GIF 選擇器 |
| **Ctrl+Shift+S** | Unigram（官方說明未列出） | 開啟貼圖選擇器 |
| **Ctrl+O** | Unigram（官方說明未列出） | 開啟檔案選擇器以傳送檔案 |
| **Ctrl+N** | UnigramPlus | 按下「新增對話」按鈕 |
| **Arrow Up** | Unigram | 編輯上一則已傳送訊息 |
| **Ctrl+Arrow Up** | Unigram | 回覆上一則已傳送訊息 |
| **Esc / Alt+Arrow Left** | Unigram | 返回 |
| **Alt+Arrow Right** | Unigram | 前進 |

### 語音訊息與媒體

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **ALT+P** | UnigramPlus | 播放或暫停目前播放中的語音訊息 |
| **ALT+S** | UnigramPlus | 提高或降低語音訊息播放速度 |
| **ALT+E** | UnigramPlus | 關閉音訊播放器 |
| **NVDA+ALT+R** | UnigramPlus | 將語音訊息轉換為文字 |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | 快轉語音訊息 |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | 倒轉語音訊息 |

### 錄製訊息

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+R** | Unigram | 開始錄製 |
| **Ctrl+R (again)** | Unigram | 傳送錄製內容 |
| **Ctrl+D** | Unigram | 停止錄製 |
| **Space (while recording) / Ctrl+P** | Unigram | 暫停錄製 |

### 通話

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+Home** | Unigram | 接聽來電 |
| **Ctrl+End** | Unigram | 拒絕來電 |
| **Ctrl+Page Up** | Unigram | 切換相機 |
| **Ctrl+Page Down** | Unigram | 切換麥克風 |
| **ALT+Shift+C** | UnigramPlus | 若為聯絡人則撥打電話，若為群組則進入語音聊天 |
| **ALT+Shift+V** | UnigramPlus | 按下視訊通話按鈕 |
| **ALT+Y** | UnigramPlus | 接聽來電 |
| **ALT+N** | UnigramPlus | 若有來電則按下「拒絕通話」按鈕；若正在通話則按下「結束通話」按鈕；若語音聊天作用中則離開語音聊天。 |
| **ALT+A** | UnigramPlus | 按下「麥克風靜音或取消靜音」按鈕 |
| **ALT+V** | UnigramPlus | 按下「啟用或停用相機」按鈕 |

### 其他快速鍵

| 快速鍵 | 類別 | 操作 |
|---|---|---|
| **Ctrl+0** | Unigram | 我的收藏 |
| **Ctrl+W** | Unigram | 關閉目前視窗 |
| **Ctrl+Q** | Unigram | 關閉 Unigram（僅限主視窗） |
| **Ctrl+Shift+Y** | Unigram | 變更狀態 |
| **Ctrl+Shift+W** | Unigram（官方說明未列出） | 停止媒體播放 |
| **Ctrl+F4** | Unigram（官方說明未列出） | 關閉目前視窗 |
| **Ctrl+L** | Unigram（官方說明未列出） | 鎖定 Unigram |
| **Ctrl+M** | Unigram（官方說明未列出） | 最小化 Unigram |
| **Ctrl+J** | Unigram（官方說明未列出） | 開啟下載 |
| **ALT+T** | UnigramPlus | 讀出已開啟聊天的名稱與狀態 |
| **NVDA+Alt+V** | UnigramPlus | 在唯讀視窗中開啟 Unigram 與 UnigramPlus 的版本資訊 |
| **ALT+M** | UnigramPlus | 開啟導覽功能表 |
| **ALT+Shift+M** | UnigramPlus | 開啟 Unigram 設定 |
| **ALT+Shift+P** | UnigramPlus | 開啟目前聊天的個人資料 |
| **ALT+L** | UnigramPlus | 啟用目前聊天中新訊息的自動讀出 |
| **ALT+H** | UnigramPlus | 顯示所有 UnigramPlus 快速鍵清單 |
| **ALT+U** | UnigramPlus | 切換進度列讀出 |
| **ALT+Shift+L** | UnigramPlus | 將廣播資料複製到剪貼簿 |
| **NVDA+ALT+U** | UnigramPlus | 開啟 UnigramPlus 設定視窗 |
<!-- shortcut-table-end -->

## 版本變更

### 版本 5.8.6

* 在 Unigram 13.0 以上版本中，空白鍵又能播放、開啟和下載訊息中的媒體了。從 Unigram 13.0 起，相片、影片、GIF、檔案、音樂或語音訊息的內容本身就是執行這些動作的按鈕。Unigram 13.0.1 為這個按鈕找回了 UnigramPlus 用來辨識它的識別碼，但在語音訊息上，這個識別碼卻給了語音轉文字按鈕，因此在語音訊息上按空白鍵沒有任何作用。現在 UnigramPlus 會依據語音訊息本身的按鈕所回報的下載進度來辨識它。Unigram 13.1.1 在選取模式以外仍不會處理訊息上的空白鍵，因此由 UnigramPlus 按下這個按鈕：空白鍵會播放或暫停語音訊息或音樂、在檢視器中開啟相片、影片或 GIF，以及下載或開啟檔案。
* 用空白鍵播放語音訊息或音樂、或下載檔案後，焦點會停留在該訊息上，下一次按 Esc 也不會再把焦點移回那裡。只有檢視器才需要這麼做，但在 Unigram 13.0 以上版本中，檔案或音樂和相片一樣寬，因此 UnigramPlus 誤把它當成了相片。
* 空白鍵不會再開啟貼圖或連結預覽。Unigram 13.0.1 給了它們和媒體按鈕相同的識別碼，但它們其實是連結。在顯示相片或影片的連結預覽中，空白鍵仍會開啟該相片或影片。
* 在 Unigram 13.0 以上版本中，在含有多個媒體附件的訊息（例如相簿）上按右、左方向鍵，又能讀出每張相片、每部影片、檔案或音樂了。從 Unigram 13.0 起，每個附件裡只有其內容本身的按鈕，因此 UnigramPlus 找不到用來區分相片和影片的部分，對每個附件都只讀出佔位字「Медіа」。現在它會查看該按鈕內部：影片在那裡有自己的下載按鈕，檔案或音樂有其標題，而相片兩者都沒有。
* Ctrl+Space 現在在聊天清單中也能使用了，以前在這裡按下沒有任何作用。和訊息一樣，第一次按下會從該聊天的內容功能表進入選取模式，並選取目前焦點所在的聊天；之後每按一次就會選取或取消選取目前焦點所在的聊天，就像在 Unigram 中按空白鍵一樣，接著 UnigramPlus 會報告聊天是否已選取。取消選取最後一個已選取的聊天會結束選取模式。聊天清單處於選取模式時，焦點移到已選取的聊天上，UnigramPlus 也會在聊天名稱前讀出「已選取」，和訊息一樣。
* 新增 Alt+Shift+M，可在 Unigram 13.1 以上版本中開啟 Unigram 設定，與 UnigramPlusRussianMod 相同。Unigram 13.1 把設定從側邊窗格移到了聊天清單下方的一個分頁。Alt+Shift+M 會選取這個分頁，然後把焦點移到設定的最上方：移到第一個其他帳號；如果只登入了一個帳號，就移到「新增帳號」。在 Unigram 13.1 之前的版本中，以及在只顯示目前聊天的窄視窗中，UnigramPlus 會讀出「設定無法使用」。

### 版本 5.8.5

* 在 Unigram 13.1 以上版本中，Alt+M 又能開啟主選單了。Unigram 13.1 把側邊窗格換成從同一個按鈕開啟的選單，而且這個按鈕不再是切換按鈕，因此 UnigramPlus 找不到它，只會讀出「主選單無法使用」。
* 修正 Ctrl+Space 在 Unigram 選取模式中的問題。在選取模式中，已選取訊息的內容功能表沒有「選取」指令，因此 UnigramPlus 會在功能表中一路往下找卻找不到，訊息也一直保持選取。現在 Ctrl+Space 的運作方式與 Unigram 13.1.1 相同：第一次按下仍會從內容功能表進入選取模式，之後每按一次就會選取或取消選取目前焦點所在的訊息，就像在 Unigram 中按空白鍵一樣，接著 UnigramPlus 會報告訊息是否已選取。取消選取最後一則已選取的訊息會結束選取模式。
* 在選取模式中，在訊息上按空白鍵和 Enter 現在會像在 Unigram 中一樣選取或取消選取該訊息，而不是播放其中的媒體或在內容功能表中尋找「回覆」；按 Backspace 也不會再去那裡尋找「編輯」。
* 更新了與 NVDA 2026.3 的相容性。UnigramPlus 不再使用 NVDA 已棄用的 API，這些 API 目前仍可使用，但日後的版本可能會移除：更新檢查的訊息方塊、開啟 UnigramPlus 設定的舊方法，以及調整語音訊息播放位置時使用的按鍵常數。
* 更新波蘭文與越南文翻譯。

### 版本 5.8.4

* 啟用「Unigram 啟動時自動將焦點移到聊天清單」後，焦點現在會停留在 Unigram 啟動時顯示的彈出視窗中，例如從邀請連結開啟的申請加入群組視窗。自 5.6.1 版起，UnigramPlus 會把焦點從彈出視窗移到後方的聊天清單，導致彈出視窗被跳過。
* 更新越南文翻譯。

### 版本 5.8.3

* 移除 UnigramPlus 自 4.8.0 版起為 Unigram 設定類別清單加入的 Enter 與空格鍵處理。在 Unigram 13.0 及更新版本中，每個設定類別都是一個按鈕，按 Enter 或空格鍵即可自行開啟，焦點也會落在該按鈕上，而不是附加元件所處理的清單項目，因此這項處理已不再生效。現在開啟類別後，焦點會如同 Unigram 本身的行為一樣停留在該類別上，不會再移入類別內容。這項處理先前也會套用到其他分頁清單（例如表情符號、GIF 與貼圖分頁）並攔截其中的 Enter 與空格鍵，現在這些按鍵在那裡也會交由 Unigram 處理。
* 在 Unigram 設定中，Alt+1 現在會將焦點移到目前開啟的設定類別；若沒有開啟任何類別，則移到第一個類別。先前它是在設定頁面的固定位置尋找類別清單，接著嘗試把焦點移到一個在 Unigram 13.0 中無法取得焦點的元素。
* 移除已無法執行的程式碼，使用上沒有任何變化。Unigram 9.5 之前，部分清單項目會以內部類別名稱讀出，UnigramPlus 會將其替換為易懂的名稱；Unigram 9.5 更改了這些類別的名稱，因此這些替換再也不會生效。另外也移除了自 5.2.0 版起已停用、用於在獨立視窗中開啟測驗解釋的處理程式。
* 更新波蘭文與越南文翻譯。

### 版本 5.8.2

* 修正新版 Unigram WinUI 3 測試版的 NVDA 錯誤。自 5.5.6 版起，每次切回 Unigram 或使用中文、日文、韓文等輸入法（IME）輸入文字時，NVDA 都會記錄一筆錯誤。Unigram 的 UWP 版本不受影響。
* 未安裝 Telegram Desktop 附加元件時，UnigramPlus 不再干擾 Telegram Desktop 的焦點朗讀。
* 移除 UnigramPlus 在取消錄製語音或影片訊息時發出的通知。無論是按 Ctrl+D 還是取消按鈕取消錄製，Unigram 13.0 及更新版本都會自行讀出，因此不會再重複讀出；較慢出現在聊天中的錄音也不會再被誤報為已取消。開始錄製與傳送仍會通知，相關設定現在稱為「開始錄製或傳送語音訊息時的通知方式」。
* 更新波蘭文與越南文翻譯。

### 版本 5.8.1

* 移除通話長度的暫時處理。Unigram 12.10 及更新版本會自行讀出通話訊息的長度，因此 UnigramPlus 不再補上，也不會重複讀出。
* 修正在缺少 utils.security 模組的舊版 NVDA 上附加元件無法啟動的問題。
* 移除附加元件已不再使用的匯入。
* 更新越南文翻譯。

### 版本 5.8.0

* 附加元件的週期性背景檢查不再於 NVDA 主迴圈執行，因此 Unigram 回應期間不會再拖慢聊天瀏覽、輸入與朗讀。
* 5.4 之後新增的所有行為現在都可在 UnigramPlus 設定中開啟或關閉，並集中在同一個標題下：語音訊息錄製按鈕的讀出方式、以 ALT+C 讀出訊息的格式化文字、個人檔案身分按鈕標籤、訊息欄位中回覆與編輯的讀出、訊息前「清單」讀出的抑制、通話中麥克風與鏡頭的即時狀態，以及切換聊天資料夾時的未讀數量。每一項預設維持目前行為，標籤也會說明它恢復的是 5.4 的哪一種行為。
* 修正空格鍵無法播放語音訊息、音樂與檔案的問題。
* 修正 Enter 無法回覆訊息、Backspace 無法編輯訊息、ALT+C 無法顯示訊息文字、ALT+D 無法返回訊息的問題。
* 修正 ALT+E 無法關閉音訊播放器的問題。
* 修正 Ctrl+ALT+左/右無法調整語音訊息播放進度的問題，包含按住輔助鍵時再次按方向鍵的情況。
* 取消語音錄製的提示改為停止後約一秒半讀出，而非五秒後。
* 選擇 5.4 版錄製按鈕選項時，開始錄製後焦點會留在訊息欄位，同時 Tab 仍可到達錄製按鈕。
* 修正多個快速鍵在 Unigram 樹狀結構缺少預期元素時靜默失效的問題：ALT+3、ALT+4、ALT+5、ALT+6、ALT+Q、ALT+T、ALT+Shift+L、ALT+Shift+P、Shift+Delete、媒體瀏覽與通話控制項。
* 語音訊息轉文字在等待期間不再每半秒啟動新執行緒，並會放棄等待而非無限等待。

### 版本 5.7.3

* NVDA+Alt+V 現在會在新的一行顯示 UnigramPlus 版本。

### 版本 5.7.2

* NVDA+Alt+V 現在會在唯讀多行視窗中開啟版本資訊。

### 版本 5.7.1

* 修正 Unigram 12.10.2 將表情回應按鈕視為訊息的問題，因此訊息導覽快速鍵不再覆蓋其原生切換動作。

### 版本 5.7.0

* 已恢復切換資料夾時讀出非零未讀數的功能，同時保留檔案傳輸進度追蹤器的保護範圍。
* 已依據目前的 Unigram 原始碼更新快速鍵清單，並標示官方 Shortcuts.md 尚未列出的內建快速鍵。

### 版本 5.6.9

* 修正了當 NVDA 進入安全桌面（例如 UAC 提示）且啟用 UnigramPlus 背景訊息追蹤時可能發生的錯誤。
* 修正 Unigram 12.10.1+ 將「我的收藏」聊天室名稱僅因原生摘要包含傳送或接收時間而誤判為訊息的問題。
* 移除了過時的「我的收藏」聊天室名稱暫時解決方法；目前版本的 Unigram 現已原生為「我的收藏」聊天室提供無障礙名稱。
* 更新了與 NVDA 2026.2 的相容性。
* 更新了波蘭語和緬甸語翻譯。

### 版本 5.6.8

* 修正安裝 WhatsApp Enhancer 時，因 appModules 輔助模組名稱衝突導致 Alt+C 失效的問題。

### 版本 5.6.7

* 為避免快速鍵衝突，讀出已安裝 Unigram 與 UnigramPlus 版本的快速鍵已從 NVDA+Shift+V 改為 NVDA+Alt+V。
* 修正目前 Unigram 版本中以 Shift+Delete 刪除聊天及退出群組或頻道的問題，包括自動處理彈出式視窗的確認動作。

### 版本 5.6.6

* 新增 NVDA+Shift+V，用來讀出已安裝的 Unigram 與 UnigramPlus 版本。
* Unigram 12.9.1 已修正按鈕標籤，因此移除針對 Unigram 12.9 inline 按鈕的暫時解法；這可避免機器人清單、訊息導覽、表情回應與聊天清單發生 UIA 卡頓。
* 已更新 5.6.6 版的所有翻譯與說明文件。

### 版本 5.6.5

* 修正目前 Unigram 版本中按 Enter 回覆訊息，以及按 Alt+Shift+R 將聊天標示為已讀的問題。
* 移除 Web 檢視模式及其設定；Alt+C 現在一律在原始 wx 快顯視窗中開啟訊息文字。
* 已將所有翻譯與說明文件更新至版本 5.6.5。

### 版本 5.6.4

* 修正 Shift+Delete：現在使用 Unigram 原生 Delete 命令，並自動確認從雙方刪除。
* Alt+2 現在會優先啟動 Unigram 的「跳轉到底部」按鈕；已移除重複的 Alt+End 快速鍵。
* 新增設定，可選擇在按 Alt+C 顯示訊息文字時使用傳統 wx 視窗（預設）或 Web 檢視。
* 現在使用 Unigram 官方提供的 Rich 訊息無障礙文字，並為 Unigram 12.9 中沒有標籤的行內按鈕加入暫時修正。
* 依據 Unigram 12.9 官方文件更新快速鍵清單。
* 加入暫時修正，使「我的收藏」主題列朗讀畫面上顯示的聊天標題，而不是 TDLib 型別名稱。

### 版本 5.6.3

* 修正使用向上、向下方向鍵在訊息間移動時，NVDA 偶爾會在訊息前讀出「清單」的問題。
* 新增 Alt+[ 功能的設定：在訊息內容之後讀出訊息標頭；此功能預設為關閉。
* 新增到達聊天室末尾時的可選聲音提示。

### 版本 5.6.2

* 修正 Ctrl+Alt+Left/Right Arrow 在語音訊息播放期間無法倒轉或快轉的問題。
* 修正 Alt+I，使其可前往聊天搜尋結果的內嵌清單。
* 新增 Alt+[，用於切換在訊息內容之前或之後讀出訊息標頭。將標頭置於內容之後時，「檔案」區段會先讀出檔名。

### 版本 5.6.1

* 修正檔案傳輸進度追蹤：進度到達 100% 時停止，且不再於每次輪詢建立新的執行緒。
* 開啟 Unigram 時，焦點現在會自動移到聊天清單。
* 新增 Ctrl+Alt+Up/Down，用於瀏覽含未讀提及的聊天室。

### 版本 5.6.0

* 修正 rich message 判斷，貼圖與表情符號訊息不再被錯誤朗讀為 rich message。
* Ctrl+R 現在使用 Unigram 官方的語音訊息錄製與傳送行為，同時保留 UnigramPlus 的錄製開始與結束提示。
* 更新本地化翻譯。

### 版本 5.5.9

* 新增豐富訊息支援。豐富訊息取得焦點時會被朗讀，並可按 Alt+C 在可瀏覽視窗中開啟。
* 豐富訊息中的連結與混合內容會被保留，且可在可瀏覽視窗中啟用連結。

### 版本 5.5.8

* 修正自動更新：現在會從 GitHub 安全取得版本，並在安裝前驗證下載的附加元件。

* 修復與 Unigram 12.7 的相容性，先前有多個快速鍵與語音提示失效。
* 投票訊息會再次朗讀問題與答案選項。
* 論壇主題清單會再次朗讀最後一則訊息的預覽。
* 一對一通話中，靜音麥克風（ALT+A）、開啟或關閉鏡頭（ALT+V）與結束通話（ALT+N）的快速鍵可再次使用。
* ALT+End 會再次移動到聊天中最新的訊息。

### 版本 5.5.7

* 將快速鍵區段重新整理為分類表格，並整合 Unigram 與 UnigramPlus 快速鍵。
* 錄製語音或視訊訊息時，NVDA 現在會朗讀「正在錄製語音訊息」或「正在錄製視訊訊息」並念出經過時間，而不再是「Tn voice message」。

### 版本 5.5.6

* 修正在群組或頻道個人資料中，按 Tab 越過名稱後，身分按鈕被讀成「Identity root」的問題；現在會讀出聊天名稱與成員數。
* control+C 不再被處理兩次：焦點在連結上時複製連結，其他情況則交由 Unigram 複製訊息。

### 版本 5.5.5

* 回覆或編輯訊息時，現在會在訊息輸入欄位中提示「回覆」或「編輯」，而不是平常的訊息輸入提示。
* 修正在關閉應用程式後、對方停止輸入後，或離開聊天後，輸入音效有時仍持續播放的問題；現在只要已開啟的聊天中沒有人在輸入，音效就會立即停止。
* 更新緬甸文本地化。

### 版本 5.5.4

* 修正聊天資料夾未讀數量變化被不必要讀出的問題，例如「全部 535」。檔案傳輸進度現在只會在 Unigram 的上傳與下載控制項中讀出，且會忽略非 Unigram 視窗。
* 修正與 Telegram Desktop NVDA 附加元件的衝突；只有偵測到目前執行的應用程式是 Unigram 時，才會啟用 UnigramPlus。
* 在 UnigramPlus 設定中新增開啟內建音效資料夾的按鈕，方便使用者以相同檔名替換自訂 WAV 音效檔案。
* 在訊息編輯欄位的上方向鍵動作中，新增「移到最後取得焦點的訊息」選項。
* 正體中文重新整理並獨立為 zh_TW，另新增簡體中文 zh_CN。

### 版本 5.5.3

* 新增檔案上傳與下載進度的自動讀出。進度列讀出設定新增「只在上傳與下載時」選項，並設為預設值。ALT+U 現在會在關閉、只限上傳下載、讀出全部進度列三種狀態間切換。
* 更新讀我檔案與翻譯。

### 版本 5.5.2

* 更新讀我檔案與翻譯。
* 變更輸入中提示音效。

### 版本 5.5.1

* 修正移到群組主題清單的快速鍵 ALT+6。
* 新增輸入中提示音：當對方在已開啟聊天中輸入時循環播放，停止輸入後結束播放。
