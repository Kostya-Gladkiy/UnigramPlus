# Phrase indicating whether the message has been read
# Phrase indicating message not read
# Phrase indicating that the message has been sent
# Phrase indicating that the message has been received
# The phrase that precedes the text of the message in sent messages
# The phrase that precedes the message text in received messages
keywordsInMessages = {
	"ar": (". تم قرائتها", ". غير مقروءة", ", تم الإرسال ⁨الساعة ⁨", ", تم التسليم ⁨الساعة ⁨", ", تم الإرسال ⁨الساعة ⁨", ", تم التسليم ⁨الساعة ⁨"),
	"en": (". Seen", ". Not seen", ", Sent at ", ", Received at ", ", Sent at ", ", Received at "),
	"cs": (". Viděno", ". Neviděno", ", Odesláno v ", ", Přijato v ", ", Odesláno v ", ", Přijato v "),
	"fr": (". Vu", ". Non vu", ", Envoyé à ", ", Reçu à ", ", Envoyé à ", ", Reçu à "),
	"de": (". Gesehen", ". Noch nicht gesehen", ", Gesendet um ", ", Empfangen um ", ", Gesendet um ", ", Empfangen um "),
	"it": (". Visto", ". Non visto", ", Inviato alle ", ", Ricevuto alle ", ", Inviato alle ", ", Ricevuto alle "),
	"fa": (". دیده شده", ". دیده نشده", ", ⁨در ⁨", ", ⁨در ⁨", ", ⁨در ⁨", ", ⁨در ⁨"),
	"fi": (". Nähty", ". Ei nähty", ", Lähetetty klo ", ", Vastaanotettu klo ", ", Lähetetty klo ", ", Vastaanotettu klo "),
	"sl": (". Videné", ". Nevidené", ", Odoslať o ", ", Prijaté o ", ", Odoslať o ", ", Prijaté o "),
	"nb": (". Sett", ". Ikke sett", ", Sendt ", ", Mottatt ", ", Sendt ", ", Mottatt "),
	"pl": (". Wyświetlono", ". Nie wyświetlono", ", Wysłana o ", ", Odebrane o ", ", Wysłana o ", ", Odebrane o "),
	"pt": (". Visto", ". Não visto", ", Enviado às ", ", Recebido às ", ", Enviado às ", ", Recebido às "),
	"ru": (". Прочитано", ". Не прочитано", ", Отправлено в ", ", Получено в ", ", Отправлено в ", ", Получено в "),
	"es": (". Visto", ". No visto", ", Enviado a las ", ", Recibido el a las ", ", Enviado a las ", ", Recibido el a las "),
	"tr": (". Görüldü", ". Görülmedi", "tarihinde gönderildi.", "tarihinde alındı.", ", bugün ", ", bugün "),
	"uk": (". Прочитане", ". Непрочитане", ", Надіслано ", ", Отримано ", ", Надіслано ", ", Отримано "),
	"be": (". Прагледжана", ". Не прагледжана", ", Адпраўлена а ", ", Атрымана а ", ", Адпраўлена а ", ", Атрымана а "),
	"zh": (". 已讀", ". 未讀", ", 傳送於  今天", ", 收到了  今天", ", 傳送於  今天", ", 收到了  今天"),
	"sr": (". Viđeno", ". Nije viđeno", ", Poslato u ", ", Primljeno u ", ", Poslato u ", ", Primljeno u "),
	"hr": (". Viđeno", ". Nije viđeno", ", Poslano u ", ", Primljeno u ", ", Poslano u ", ", Primljeno u "),
	"ro": (". Citit", ". Necitit.", ", Trimis la ", ", Primit la ", ", Trimis la ", ", Primit la "),
}
keywordsInMessages["zh_TW"] = (". 已讀", ". 未讀", ", 傳送於 ", ", 收到了 ", ", 傳送於 ", ", 收到了 ")
keywordsInMessages["zh_CN"] = (". 已读", ". 未读", ", 已发送于 ", ", 已收到 ", ", 已发送于 ", ", 已收到 ")

# Icons on the audio player header. Current Unigram gives its close button no
# automation id and a localized name, so its glyph is what identifies it.
icons_in_audio_player = {
	"close": "",
}

icons_from_context_menu = {
	"attach": "\ue840",
	"unpin": "\ue77a",
	"reply": "\ue248",
	"copy": "\ue8c8",
	"edit": "\ue104",
	"forward": "\ue72d",
	"delete": "\ue74d",
	"save_as": "\ue792",
	"select": "\ue97e",
	"read": "\ue91d",
	"unread": "\ue91c"
}

labels_for_buttons = {
	"Back": _("Back"),
	"Menu": _("Menu"),
	"Pin": _("Attach"),
	"Edit": _("Edit"),
	"Photo": _("Photo"),
	"Image": _("Image"),
	"InviteLink": _("Invite link"),
	"FieldSeconds": _("Choose time"),
	"TitleField": _("Title field"),
}

labels_in_buttons = {
	"\ue987": _("Go to next reaction"),
	"\ue76e": _("Insert emojis"),
	"\ue10b": _("Done"),
	"\ue722": _("Next"),
	"\ue90c": _("Merge files"),
	"\ue721": _("Search"),
	"\ue74d": _("Delete"),
	"\ue711": _("Close"),
}

# Keywords used to detect "typing..."-style chat actions shown in the chat title.
# When any of these appears in the chat-title status text, the addon treats it as
# an active typing/recording/uploading state and starts the Typing.wav loop.
typing_keywords = (
	"typing",			# en
	"輸入",			# zh (Traditional & Simplified)
	"输入",
	"печат",			# ru: печатает / печатают
	"набира",		# ru: набирает
	"пише",			# uk
	"schreibt",		# de
	"écrit",			# fr
	"escribiend",		# es
	"scriv",			# it: sta scrivendo
	"digitando",		# pt
	"pisze",			# pl
	"يكتب",			# ar
	"píše",			# cs
	"yazıyor",		# tr
	"kirjoittaa",		# fi
	"skriver",		# nb
	"입력",			# ko
	"入力",			# ja
	"пиша",			# be / sr
	"kuca",			# sr-Latn / hr / bs
	"tipkati",		# hr
	"scrie",			# ro
	# Other chat actions that should also play the indicator sound
	"recording",
	"sending",
	"uploading",
	"录制",
	"錄製",
	"上傳",
	"上传",
	"запис",
	"відправ",
	"отправ",
	"пересил",
	"загруж",
)
typing_keywords += (
	"正在輸入",
	"正在输入",
	"正在錄製",
	"正在录制",
	"正在傳送",
	"正在发送",
	"正在上傳",
	"正在上传",
)


phrase_administrator_in_message = {
	"uk": ("Адміністратор", "Власник"),
	"fr": ("Administrateur", "Propriétaire"),
	"en": ("Admin", "Owner"),
	"zh": ("管理員", "擁有者"),
	"hr": ("Administrator", "Vlasnik"),
	"ar": ("مشرف", "المالك"),
	"sr": ("Administrator", "Vlasnik"),
	"it": ("Proprietario", "Amministratore"),
	"ne": ("मालिक", "प्रसाशक"),
	"es": ("Administrador", "Propietario"),
	"cs": ("Správce", "Vlastník"),
	"ru": ("Администратор", "Владелец"),
}
phrase_administrator_in_message["zh_TW"] = ("管理員", "擁有者")
phrase_administrator_in_message["zh_CN"] = ("管理员", "所有者")
