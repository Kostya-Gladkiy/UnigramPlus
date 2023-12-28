# Phrase indicating whether the message has been read
# Phrase indicating message not read
# Phrase indicating that the message has been sent
# Phrase indicating that the message has been received
# The phrase that precedes the text of the message in sent messages
# The phrase that precedes the message text in received messages
keywordsInMessages = {
	"ar": (". تم قرائتها.", ". غير مقروءة.", ", تم الإرسال ⁨الساعة ⁨‎", ", تم التسليم ⁨الساعة ⁨‎", ", تم الإرسال ⁨الساعة ⁨‎", ", تم التسليم ⁨الساعة ⁨‎"),
	"en": (". Seen.", ". Not seen.", ", Sent at ‎", ", Received at ‎", ", Sent at ‎", ", Received at ‎"),
	"cs": (". Viděno.", ". Neviděno.", ", Odesláno v ‎", ", Přijato v ‎", ", Odesláno v ‎", ", Přijato v ‎"),
	"fr": (". Vu.", ". Non vu.", ", Envoyé à ‎", ", Reçu à ‎", ", Envoyé à ‎", ", Reçu à ‎"),
	"de": (". Gesehen.", ". Noch nicht gesehen.", ", Gesendet um ‎", ", Empfangen um ‎", ", Gesendet um ‎", ", Empfangen um ‎"),
	"it": (". Visto.", ". Non visto.", ", Inviato alle ‎", ", Ricevuto alle ‎", ", Inviato alle ‎", ", Ricevuto alle ‎"),
	"fa": (". دیده شده.", ". دیده نشده.", ", ⁨در ⁨‎", ", ⁨در ⁨‎", ", ⁨در ⁨‎", ", ⁨در ⁨‎"),
	"fi": (". Nähty.", ". Ei nähty.", ", Lähetetty klo ‎", ", Vastaanotettu klo ‎", ", Lähetetty klo ‎", ", Vastaanotettu klo ‎"),
	"sl": (". Videné.", ". Nevidené.", ", Odoslať o ‎", ", Prijaté o ‎", ", Odoslať o ‎", ", Prijaté o ‎"),
	"nb": (". Sett.", ". Ikke sett.", ", Sendt ‎", ", Mottatt ‎", ", Sendt ‎", ", Mottatt ‎"),
	"pl": (". Wyświetlono.", ". Nie wyświetlono.", ", Wysłana o ‎", ", Odebrane o ‎", ", Wysłana o ‎", ", Odebrane o ‎"),
	"pt": (". Visto.", ". Não visto.", ", Enviado às ‎", ", Recebido às ‎", ", Enviado às ‎", ", Recebido às ‎"),
	"ru": (". Прочитано.", ". Не прочитано.", ", Отправлено в ‎", ", Получено в ‎", ", Отправлено в ‎", ", Получено в ‎"),
	"es": (". Visto.", ". No visto.", ", Enviado a las ‎", ", Recibido el a las ‎", ", Enviado a las ‎", ", Recibido el a las ‎"),
	"tr": (". Görüldü.", ". Görülmedi.", "tarihinde gönderildi.", "tarihinde alındı.", ", bugün ‎", ", bugün ‎"),
	"uk": (". Прочитане.", ". Непрочитане.", ", Надіслано ‎", ", Отримано ‎", ", Надіслано ‎", ", Отримано ‎"),
	"be": (". Прагледжана.", ". Не прагледжана.", ", Адпраўлена а ‎", ", Атрымана а ‎", ", Адпраўлена а ‎", ", Атрымана а ‎"),
	"zh": (". 已讀.", ". 未讀.", ", 傳了  今天‎", ", 收到了  今天‎", ", 傳了  今天‎", ", 收到了  今天‎"),
	"sr": (". Viđeno.", ". Nije viđeno.", ", Poslato u ‎", ", Primljeno u ‎", ", Poslato u ‎", ", Primljeno u ‎"),
	"hr": (". Viđeno.", ". Nije viđeno.", ", Poslano u ‎", ", Primljeno u ‎", ", Poslano u ‎", ", Primljeno u ‎"),
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