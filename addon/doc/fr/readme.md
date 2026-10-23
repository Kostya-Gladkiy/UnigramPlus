# Unigram Plus

* Auteur : Kostya Gladkiy (Ukraine)
* [Canal Telegram] (https://t.me/unigramPlus)
* Telegram : @unigramPlus
* Lien pour faire un don : [https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)
* PayPal : gladkiy.kostya@gmail.com

Utilisez Unigram de manière plus confortable et plus productive. Cet extension fournit de nombreuses touches de raccourci pour une navigation rapide et agréable dans Unigram, tout en apportant de nombreuses petites améliorations dont voici un aperçu :

* Amélioration significative de l'affichage des messages tels qu'un sondage, un lien ou un message avec un média attaché.
* Lorsque le focus est placé dans la liste des échanges, il supprime les termes superflus tels que : "échanges, onglet, liste sélectionnée" et sur la liste des messages, le mot "liste".
* Lorsque le curseur est placé sur le bouton "Ouvrir fichier" ou "Télécharger fichier", le nom et la taille du fichier sont énoncés. De même, quand le curseur atteint le bouton de lecture d'un fichier audio, vous entendez son nom et sa durée.
* Lorsque le focus est placé sur un message vocal en cours de lecture, vous entendez d'abord la durée de lecture écoulée, puis toutes les autres informations.
* Lorsque vous déplacez le focus sur un message au sein d'un échange, vous entendez d'abord l'information selon laquelle il est sélectionné, puis le contenu du message.
* Désormais, lorsque vous vous déplacez dans un échange, le mot "vu" ne sera pas prononcé du tout et "non vu" sera énoncé avant le contenu du message.
* Amélioration significative de la fonction d'enregistrement des messages vocaux. Le début et l'envoi de l'enregistrement d'un message vocal sont accompagnés de sons caractéristiques, tandis qu'Unigram 13.0 et versions ultérieures annoncent eux-mêmes l'annulation d'un enregistrement. De plus, lors de l'exécution de ces fonctions, le focus reste à sa position et ne saute ni sur le bouton d'enregistrement ni sur le champ de saisie du message.
* Si le média joint au message est ouvert à l'aide de la barre d'espacement, le focus revient au dernier élément sélectionné après sa fermeture.
* L'extension vous permet de désactiver complètement l'annonce des barres de progression, ou encore de désactiver uniquement l'annonce de celle relative à la lecture des messages vocaux.

##Soutenir le développement

Si vous appréciez vraiment cette extension et que vous avez l'envie,  mais surtout la possibilité de soutenir financièrement le développeur, le motivant ainsi à faire évoluer cette extension, vous pouvez le faire en envoyant votre contribution à l'aide des coordonnées bancaires suivantes : [Faire un don,](https://unigramplus.diaka.ua/donate) ou en utilisant le numéro de carte suivant : 5169360009004502 (Ukraine). Et rappelez-vous que certains de ceux qui ont lu ces lignes ce sont dit que quelqu'un soutiendra bien le développeur, mais que ce ne sera pas eux".

## Sons personnalisés
Les sons d'UnigramPlus se trouvent dans le dossier `appModules\media` de l'extension. Ouvrez les paramètres de NVDA > UnigramPlus puis appuyez sur **Ouvrir le dossier des sons UnigramPlus**. Pour personnaliser un son, copiez dans ce dossier un fichier WAV de remplacement portant le même nom que le son à remplacer, puis redémarrez NVDA ou rechargez les extensions. Les mises à jour de l'extension peuvent restaurer les sons fournis, gardez donc une copie de vos fichiers personnalisés.

<!-- shortcut-table-start -->
## Liste de raccourcis :

> In the Category column, `UnigramPlus` identifies shortcuts provided by the add-on and `Unigram` identifies shortcuts built into Unigram.

> `Unigram (non documenté)` désigne les raccourcis implémentés dans le code source actuel d’Unigram mais pas encore répertoriés dans son Shortcuts.md officiel.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Navigation entre les discussions

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | Next chat |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | Previous chat |
| **Ctrl+Alt+Home** | Unigram (non documenté) | Première discussion |
| **Ctrl+Alt+End** | Unigram (non documenté) | Dernière discussion |
| **Ctrl+Alt+Up/Down** | UnigramPlus | Aller à l’échange suivant ou précédent contenant des mentions non lues |
| **ALT+1** | UnigramPlus | Déplacer le focus vers la liste des échanges |
| **ALT+2** | UnigramPlus | Déplace le focus au dernier message d'un échange ouvert |
| **ALT+3** | UnigramPlus | Déplacer le focus à l'indicateur de messages non lus |
| **ALT+4** | UnigramPlus | Déplace le focus à la liste des dossiers des échanges |
| **ALT+5** | UnigramPlus | Déplace le focus au profil ouvert |
| **ALT+6** | UnigramPlus | Déplace le focus à la liste des dossiers des échanges |
| **ALT+D** | UnigramPlus | Déplacer le focus au champ d'édition. Si le focus y est déjà, il reviendra où il était auparavant |

### Recherche

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **Ctrl+F** | Unigram | Messages search per chat |
| **Ctrl+Shift+F** | Unigram (non documenté) | Chat search |
| **Search key** | Unigram (non documenté) | Rechercher dans la page actuelle |
| **ALT+I** | UnigramPlus | Go to the list with search results |
| **F3** | UnigramPlus | Go to the next search result |
| **Shift+F3** | UnigramPlus | Go to the previous search result |

### Texte sélectionné dans la zone de saisie

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (non documenté) | Rétablir |
| **Alt+X** | Unigram (non documenté) | Convertir quatre chiffres hexadécimaux sélectionnés en leur caractère correspondant |
| **Ctrl+X** | Unigram | Cut |
| **Ctrl+C** | Unigram | Copy |
| **Ctrl+V** | Unigram | Paste |
| **Ctrl+A** | Unigram | Select All |
| **Ctrl+Shift+.** | Unigram | Citation |
| **Ctrl+B** | Unigram | Bold |
| **Ctrl+I** | Unigram | Italic |
| **Ctrl+U** | Unigram | Souligné |
| **Ctrl+Shift+X** | Unigram | Strikethrough |
| **Ctrl+Shift+M** | Unigram | Monospace |
| **Ctrl+Shift+P** | Unigram | Spoiler |
| **Ctrl+K** | Unigram | Create Link |
| **Ctrl+Shift+N** | Unigram | Supprimer la mise en forme (texte normal) |

### Dossiers

| Raccourci | Catégorie | Action |
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
| **Ctrl+Shift+Down** | Unigram (non documenté) | Dossier suivant |
| **Ctrl+Shift+Up** | Unigram (non documenté) | Dossier précédent |

### Actions sur les messages

| Raccourci | Catégorie | Action |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Copier le message s'il contient du texte. Si le focus est sur un lien, ce dernier sera copié |
| **ALT+Q** | UnigramPlus | Activer le bouton "affichage instantanée" s'il est inclus dans le message courant. |
| **ALT+Delete** | UnigramPlus | Supprimer un message ou un échange |
| **Shift+Delete** | UnigramPlus | Supprimer un message ou un échange pour tout le monde |
| **Delete** | Unigram (non documenté) | Supprimer le message sélectionné ou ayant le focus |
| **Ctrl+ALT+C** | UnigramPlus | Ouvrir les commentaires |
| **Enter** | UnigramPlus | Répondre au message |
| **ALT+F** | UnigramPlus | Transférer le message |
| **Backspace** | UnigramPlus | Éditer le message |
| **ALT+Shift+R** | UnigramPlus | Marquer un échange comme lu |
| **Ctrl+Space** | UnigramPlus | Basculer en mode sélection |
| **Unassigned** | UnigramPlus | Enregistrer le fichier sous... |
| **Unassigned** | UnigramPlus | Épingler un message ou un échange |
| **Left Arrow** | UnigramPlus | Annoncer si un message contient une réaction |
| **Right Arrow** | UnigramPlus | Move to the next media attachment in the focused message |
| **ALT+C** | UnigramPlus | Montrer le message dans une fenêtre virtuelle |
| **ALT+W** | UnigramPlus | Announces the time a message was sent or received, as well as a list of reactions. Double-clicking toggles the announcement mode for this information. |
| **ALT+[** | UnigramPlus | Basculer l’annonce des en-têtes de message avant ou après le contenu du message |
| **NVDA+Ctrl+0-9** | UnigramPlus | Review one of the ten most recent messages; 1 is the newest and 0 is the tenth newest |
| **Ctrl+Shift+A** | UnigramPlus | Activer le bouton "joindre un fichier" |
| **Ctrl+Shift+E** | Unigram (non documenté) | Ouvrir le sélecteur d’emojis |
| **Ctrl+Shift+G** | Unigram (non documenté) | Ouvrir le sélecteur de GIF |
| **Ctrl+Shift+S** | Unigram (non documenté) | Ouvrir le sélecteur de stickers |
| **Ctrl+O** | Unigram (non documenté) | Ouvrir le sélecteur de fichiers pour envoyer des documents |
| **Ctrl+N** | UnigramPlus | Activer le bouton "nouvel échange" |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Messages vocaux et médias

| Raccourci | Catégorie | Action |
|---|---|---|
| **ALT+P** | UnigramPlus | Jouer / mettre en pause le message en cours de lecture |
| **ALT+S** | UnigramPlus | Accélérer et ralentir la vistesse de lecture |
| **ALT+E** | UnigramPlus | Fermer le lecteur audio |
| **NVDA+ALT+R** | UnigramPlus | Convertir le message vocal en texte |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | Avancer rapidement dans un message vocal |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | Reculer dans un message vocal |

### Enregistrement de messages

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+R** | Unigram | Start record |
| **Ctrl+R (again)** | Unigram | Send recorded |
| **Ctrl+D** | Unigram | Stop recording |
| **Space (while recording) / Ctrl+P** | Unigram | Pause recording |

### Appels

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+Home** | Unigram | Accept incoming call |
| **Ctrl+End** | Unigram | Reject incoming call |
| **Ctrl+Page Up** | Unigram | Toggle camera |
| **Ctrl+Page Down** | Unigram | Toggle microphone |
| **ALT+Shift+C** | UnigramPlus | Appeler s'il s'agit d'un contact, ou initier un échange vocal s'il s'agit d'un groupe |
| **ALT+Shift+V** | UnigramPlus | Activer le bouton Appell vidéo |
| **ALT+Y** | UnigramPlus | Accepter l'appel |
| **ALT+N** | UnigramPlus | Activer le bouton "refuser l'appel" lors d'un appell entrant, "terminer l'appel" si un appel est en cours ou quitter l'échange vocal s'il est actif |
| **ALT+A** | UnigramPlus | Activer le bouton "activer/désactiver le micro" |
| **ALT+V** | UnigramPlus | Activer le bouton "activer/désactiver la caméra |

### Autres raccourcis

| Raccourci | Catégorie | Action |
|---|---|---|
| **Ctrl+0** | Unigram | Saved messages |
| **Ctrl+W** | Unigram | Close current window |
| **Ctrl+Q** | Unigram | Close Unigram (main window only) |
| **Ctrl+Shift+Y** | Unigram | Change status |
| **Ctrl+Shift+W** | Unigram (non documenté) | Arrêter la lecture du média |
| **Ctrl+F4** | Unigram (non documenté) | Close current window |
| **Ctrl+L** | Unigram (non documenté) | Verrouiller Unigram |
| **Ctrl+M** | Unigram (non documenté) | Réduire Unigram |
| **Ctrl+J** | Unigram (non documenté) | Ouvrir les téléchargements |
| **ALT+T** | UnigramPlus | Annoncer le nom et l'état d'un échange ouvert |
| **NVDA+Alt+V** | UnigramPlus | Ouvrir les informations de version d’Unigram et d’UnigramPlus dans une fenêtre en lecture seule |
| **ALT+M** | UnigramPlus | Ouvrir le menu de navigation |
| **ALT+Shift+M** | UnigramPlus | Ouvrir les paramètres d'Unigram |
| **ALT+Shift+P** | UnigramPlus | Ouvrir le profil de l'échange en cours |
| **ALT+L** | UnigramPlus | Activer la lecture automatique des nouveaux messages dans l'échange courant |
| **ALT+H** | UnigramPlus | Show a list of all UnigramPlus shortcuts |
| **ALT+U** | UnigramPlus | Basculer l'annonce des bares de progression |
| **ALT+Shift+L** | UnigramPlus | Copier les données relatives à la diffusion dans le presse-papiers |
| **NVDA+ALT+U** | UnigramPlus | Ouvrir les préférences d'UnigramPlus |
<!-- shortcut-table-end -->

##Liste des changements :

### Version 5.8.6

* Espace lit, ouvre et télécharge de nouveau le média d’un message dans Unigram 13.0 et versions ultérieures. Depuis Unigram 13.0, le contenu d’un message photo, vidéo, GIF, fichier, musique ou vocal est lui-même le bouton qui le fait. Unigram 13.0.1 a rendu à ce bouton l’identifiant que cherche UnigramPlus, sauf pour les messages vocaux, où l’identifiant est allé au bouton de transcription, si bien qu’Espace ne faisait rien sur un message vocal. UnigramPlus reconnaît désormais le bouton propre d’un message vocal à la progression du téléchargement qu’il indique. Unigram 13.1.1 n’associe toujours aucune action à Espace sur un message en dehors du mode sélection ; UnigramPlus appuie donc sur ce bouton : Espace lit ou met en pause un message vocal ou une musique, ouvre une photo, une vidéo ou un GIF dans la visionneuse, et télécharge ou ouvre un fichier.
* Après qu’Espace a lu un message vocal ou une musique ou téléchargé un fichier, le focus reste sur le message, et l’appui suivant sur Échap ne l’y ramène plus. Seule la visionneuse en a besoin, mais dans Unigram 13.0 et versions ultérieures un fichier ou une musique est aussi large qu’une photo, et UnigramPlus le prenait pour une photo.
* Espace n’ouvre plus les autocollants ni les aperçus de liens. Unigram 13.0.1 leur a donné le même identifiant qu’aux boutons de média, mais ce sont des liens. Dans un aperçu de lien qui affiche une photo ou une vidéo, Espace ouvre toujours la photo ou la vidéo.
* Flèche droite et Flèche gauche sur un message à plusieurs pièces jointes multimédias, comme un album, annoncent de nouveau chaque photo, vidéo, fichier ou musique dans Unigram 13.0 et versions ultérieures. Depuis Unigram 13.0, chaque pièce jointe ne contient que le bouton propre à son contenu ; UnigramPlus ne trouvait donc plus ce qui distingue une photo d’une vidéo et annonçait le mot provisoire « Медіа » pour chaque pièce jointe. Il regarde désormais à l’intérieur de ce bouton : une vidéo y a son propre bouton de téléchargement, un fichier ou une musique son titre, et une photo ni l’un ni l’autre.
* Ctrl+Space fonctionne désormais aussi dans la liste des échanges, où il ne faisait rien jusqu’ici. Comme pour les messages, le premier appui active le mode sélection avec l’échange qui a le focus depuis le menu contextuel de l’échange, puis chaque appui sélectionne ou désélectionne l’échange qui a le focus, comme le fait Espace dans Unigram. UnigramPlus annonce ensuite si l’échange est sélectionné. Désélectionner le dernier échange sélectionné quitte le mode sélection. Tant que la liste des échanges est en mode sélection, UnigramPlus dit aussi « Sélectionnée » avant le nom d’un échange sélectionné quand le focus y arrive, comme il le fait pour les messages.
* Ajout d’Alt+Shift+M, qui ouvre les paramètres d’Unigram dans Unigram 13.1 et versions ultérieures, comme le fait UnigramPlusRussianMod. Unigram 13.1 a déplacé les paramètres du volet latéral vers un onglet situé sous la liste des échanges. Alt+Shift+M sélectionne cet onglet, puis place le focus en haut des paramètres : sur le premier de vos autres comptes ou, si vous n’êtes connecté qu’à un seul compte, sur « Ajouter un compte ». Dans les versions d’Unigram antérieures à 13.1, et dans une fenêtre étroite qui n’affiche que l’échange ouvert, UnigramPlus annonce « Paramètres non disponibles ».

### Version 5.8.5

* Alt+M ouvre de nouveau le menu de navigation dans Unigram 13.1 et versions ultérieures. Unigram 13.1 a remplacé le volet latéral par un menu qui s’ouvre à partir du même bouton, et ce bouton n’est plus un bouton bascule ; UnigramPlus ne le trouvait donc pas et annonçait « Menu de navigation non disponible ».
* Correction de Ctrl+Space dans le mode sélection d’Unigram. Dans ce mode, le menu contextuel d’un message sélectionné n’a pas de commande Sélectionner ; UnigramPlus parcourait donc le menu sans la trouver, et le message restait sélectionné. Ctrl+Space fonctionne désormais comme dans Unigram 13.1.1 : le premier appui active toujours le mode sélection depuis le menu contextuel, puis chaque appui sélectionne ou désélectionne le message qui a le focus, comme le fait Espace dans Unigram. UnigramPlus annonce ensuite si le message est sélectionné. Désélectionner le dernier message sélectionné quitte le mode sélection.
* En mode sélection, Espace et Entrée sur un message le sélectionnent ou le désélectionnent désormais, comme dans Unigram, au lieu de lire son média ou de chercher Répondre dans le menu contextuel, et Retour arrière ne cherche plus Modifier dans ce menu.
* Mise à jour de la compatibilité avec NVDA 2026.3. UnigramPlus n’utilise plus des parties obsolètes de l’API de NVDA, que NVDA prend encore en charge mais pourrait supprimer dans une version ultérieure : les boîtes de message de la recherche de mises à jour, l’ancienne manière d’ouvrir les paramètres d’UnigramPlus et une constante de touche utilisée pour avancer ou reculer dans les messages vocaux.
* Mise à jour des traductions polonaise et vietnamienne.

### Version 5.8.4

* Lorsque l’option « Placer automatiquement le focus dans la liste des échanges au démarrage d’Unigram » est activée, le focus reste désormais dans la fenêtre contextuelle qu’Unigram affiche au démarrage, comme la demande pour rejoindre un groupe ouverte depuis un lien d’invitation. Depuis la version 5.6.1, UnigramPlus déplaçait le focus de cette fenêtre vers la liste des échanges située derrière, si bien que la fenêtre était ignorée.
* Mise à jour de la traduction vietnamienne.

### Version 5.8.3

* Suppression de la gestion des touches Entrée et Espace qu'UnigramPlus ajoutait depuis la version 4.8.0 à la liste des catégories de paramètres d'Unigram. Dans Unigram 13.0 et versions ultérieures, chaque catégorie de paramètres est un bouton qui s'ouvre de lui-même avec Entrée ou Espace, et le focus arrive sur ce bouton plutôt que sur l'élément de liste que gérait l'extension ; cette gestion ne s'y appliquait donc plus. À l'ouverture d'une catégorie, le focus reste désormais sur celle-ci, comme dans Unigram lui-même, au lieu d'être déplacé dans la catégorie. Cette gestion s'appliquait aussi à d'autres listes d'onglets, comme les onglets Emoji, GIF et Stickers, où elle interceptait Entrée et Espace ; ces touches parviennent désormais aussi à Unigram à ces endroits.
* Dans les paramètres d'Unigram, Alt+1 place désormais le focus sur la catégorie de paramètres ouverte, ou sur la première catégorie si aucune n'est ouverte. Auparavant, il cherchait la liste des catégories à une position fixe de la page des paramètres, puis tentait de placer le focus sur un élément qui ne peut pas recevoir le focus dans Unigram 13.0.
* Suppression de code qui ne pouvait plus s'exécuter, sans aucun changement à l'usage. Avant Unigram 9.5, certains éléments de liste étaient annoncés par un nom de classe interne, qu'UnigramPlus remplaçait par un nom lisible ; Unigram 9.5 a renommé ces classes, si bien que ces remplacements ne s'appliquaient plus jamais. Le gestionnaire qui ouvrait l'explication d'un quiz dans une fenêtre séparée, désactivé depuis la version 5.2.0, a également été supprimé.
* Mise à jour des traductions polonaise et vietnamienne.

### Version 5.8.2

* Correction des erreurs de NVDA dans la nouvelle version bêta WinUI 3 d'Unigram. Depuis la version 5.5.6, une erreur était journalisée à chaque retour dans Unigram ou à chaque saisie avec un éditeur de méthode d'entrée (IME), comme ceux du chinois, du japonais ou du coréen. La version UWP d'Unigram n'était pas concernée.
* UnigramPlus n'interfère plus avec les annonces du focus dans Telegram Desktop lorsque l'extension Telegram Desktop n'est pas installée.
* Suppression de la notification qu'UnigramPlus donnait lors de l'annulation de l'enregistrement d'un message vocal ou vidéo. Unigram 13.0 et versions ultérieures annoncent eux-mêmes un enregistrement annulé, que ce soit avec Ctrl+D ou le bouton d'annulation ; elle n'est donc plus entendue deux fois. Un enregistrement qui tarde à apparaître dans l'échange n'est plus non plus signalé comme annulé. Le début et l'envoi d'un enregistrement sont toujours annoncés, et l'option correspondante s'appelle désormais « Notification au début ou à l'envoi de l'enregistrement d'un message vocal ».
* Mise à jour des traductions polonaise et vietnamienne.

### Version 5.8.1

* Suppression du contournement relatif à la durée des appels. Unigram 12.10 et versions ultérieures annoncent eux-mêmes la durée d'un message d'appel ; UnigramPlus ne l'ajoute donc plus et elle n'est plus entendue deux fois.
* Correction du démarrage impossible de l'extension sur les anciennes versions de NVDA qui ne fournissent pas le module utils.security.
* Suppression des importations que l'extension n'utilise plus.
* Mise à jour de la traduction vietnamienne.

### Version 5.8.0

* Les vérifications périodiques effectuées en arrière-plan par l'extension ne s'exécutent plus dans la boucle principale de NVDA : la navigation dans les échanges, la saisie et la parole ne sont donc plus retardées pendant qu'Unigram répond.
* Tous les comportements ajoutés après la version 5.4 peuvent désormais être activés ou désactivés dans les paramètres d'UnigramPlus, regroupés sous un même intitulé : l'annonce du bouton d'enregistrement de message vocal, le texte enrichi des messages avec ALT+C, l'étiquette du bouton d'identité du profil, l'annonce de réponse et de modification dans le champ de message, la suppression de l'annonce « liste » avant les messages, l'état en direct du micro et de la caméra pendant un appel, ainsi que le nombre de messages non lus lors du changement de dossier. Chaque option conserve son comportement actuel par défaut et chaque libellé précise quel comportement de la version 5.4 elle rétablit.
* Correction de la barre d'espace qui ne lisait pas les messages vocaux, la musique et les fichiers.
* Correction d'Entrée qui ne répondait pas à un message, de Retour arrière qui ne le modifiait pas, d'ALT+C qui n'affichait pas son texte et d'ALT+D qui n'y revenait pas.
* Correction d'ALT+E qui ne fermait pas le lecteur audio.
* Correction de Ctrl+ALT+Gauche et Ctrl+ALT+Droite qui ne déplaçaient pas la lecture du message vocal, y compris lorsque la flèche est pressée de nouveau alors que les modificateurs restent enfoncés.
* L'annulation d'un enregistrement vocal est annoncée environ une seconde et demie après son arrêt, au lieu de cinq secondes plus tard.
* Avec l'option du bouton d'enregistrement de la version 5.4 sélectionnée, le focus reste dans le champ de message au démarrage d'un enregistrement, tandis que Tab atteint toujours le bouton d'enregistrement.
* Correction de plusieurs raccourcis qui échouaient silencieusement lorsqu'un élément attendu manquait dans l'arborescence d'Unigram : ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Maj+L, ALT+Maj+P, Maj+Suppr, la navigation dans les médias et les commandes d'appel.
* La conversion d'un message vocal en texte ne lance plus un nouveau thread toutes les demi-secondes pendant l'attente et abandonne au lieu d'attendre indéfiniment.

### Version 5.7.3

* NVDA+Alt+V affiche désormais la version d’UnigramPlus sur une nouvelle ligne.

### Version 5.7.2

* NVDA+Alt+V ouvre maintenant les informations de version dans une fenêtre multiligne en lecture seule.

### Version 5.7.1

* Correction du traitement des boutons de réaction d’Unigram 12.10.2 comme des messages : les raccourcis de navigation entre les messages ne remplacent plus leur action bascule native.

### Version 5.7.0

* Les annonces de changement de dossier avec un nombre de non-lus non nul ont été rétablies, tout en conservant les protections du suivi de progression des transferts de fichiers.
* La liste des raccourcis a été mise à jour d’après le code source actuel d’Unigram et les raccourcis intégrés absents de son Shortcuts.md officiel ont été identifiés.

### Version 5.6.9

* Correction d’une erreur pouvant survenir lorsque NVDA entrait dans un bureau sécurisé, par exemple lors d’une invite UAC, alors que le suivi des messages en arrière-plan d’UnigramPlus était activé.
* Correction des lignes de rubriques Messages enregistrés d’Unigram 12.10.1+ qui étaient traitées comme des messages simplement parce que leurs résumés natifs contiennent des horodatages d’envoi ou de réception.
* Suppression de l’ancien correctif de nom des rubriques Messages enregistrés ; les versions actuelles d’Unigram fournissent désormais nativement des noms accessibles pour les discussions Messages enregistrés.
* Mise à jour de la compatibilité avec NVDA 2026.2.
* Mise à jour des traductions polonaise et birmane.

### Version 5.6.8

* Correction de l’échec de Alt+C lorsque WhatsApp Enhancer est installé, dû à une collision de noms de modules auxiliaires dans appModules.

### Version 5.6.7

* Le raccourci annonçant les versions installées d’Unigram et d’UnigramPlus est passé de NVDA+Maj+V à NVDA+Alt+V afin d’éviter les conflits de raccourcis.
* Correction de Shift+Suppr pour supprimer des discussions et quitter des groupes ou canaux dans les versions actuelles d’Unigram, y compris la confirmation automatique de la fenêtre contextuelle.

### Version 5.6.6

* Ajout de NVDA+Maj+V pour annoncer les versions installées d’Unigram et d’UnigramPlus.
* Suppression du correctif temporaire des boutons intégrés d’Unigram 12.9 après la correction de leurs libellés dans Unigram 12.9.1 ; cela évite les blocages UIA dans les listes de bots, la navigation entre les messages, les réactions et la liste des discussions.
* Mise à jour de toutes les traductions et de tous les manuels pour la version 5.6.6.

### Version 5.6.5

* Correction de la touche Entrée pour répondre aux messages et de Alt+Maj+R pour marquer les discussions comme lues dans les versions actuelles d’Unigram.
* Suppression du mode vue Web et de son réglage ; Alt+C ouvre désormais toujours le texte du message dans la fenêtre contextuelle wx d’origine.
* Mise à jour de toutes les traductions et de tous les manuels pour la version 5.6.5.

### Version 5.6.4

* Correction de Shift+Delete en utilisant la commande Delete native d’Unigram et en confirmant automatiquement la suppression des deux côtés.
* Alt+2 active désormais d’abord le bouton « Aller en bas » d’Unigram ; le raccourci Alt+End en double a été supprimé.
* Ajout d’un réglage permettant de choisir la fenêtre wx classique (par défaut) ou la vue Web lors de l’affichage du texte avec Alt+C.
* Le texte officiel accessible des messages enrichis d’Unigram est désormais utilisé, avec un correctif temporaire pour les boutons intégrés sans étiquette d’Unigram 12.9.
* Mise à jour de la liste des raccourcis d’après la documentation officielle d’Unigram 12.9.
* Ajout d’un correctif temporaire afin que les lignes de sujets des Messages enregistrés annoncent le titre visible de la discussion plutôt qu’un nom de type TDLib.

### Version 5.6.3

* Correction d’un problème intermittent où NVDA annonçait « liste » avant un message lors de la navigation avec les flèches haut et bas.
* Ajout d’un réglage pour le comportement de Alt+[, qui annonce les en-têtes des messages après leur contenu ; il est désactivé par défaut.
* Ajout d’une notification sonore facultative à l’arrivée à la fin d’un échange.

### Version 5.6.2

* Correction du raccourci Ctrl+Alt+Left/Right Arrow pour reculer et avancer dans un message vocal en cours de lecture.
* Correction du raccourci Alt+I : il permet désormais d’accéder à la liste intégrée des résultats de recherche de l’échange.
* Ajout de Alt+[ pour basculer l’annonce des en-têtes avant ou après le contenu du message. Lorsque les en-têtes sont placés après le contenu, les noms de fichiers sont annoncés en premier dans les sections de fichiers.

### Version 5.6.1

* Correction du suivi de la progression des transferts de fichiers : il s’arrête désormais à 100 % et ne crée plus de nouveau thread à chaque cycle d’interrogation.
* À l’ouverture d’Unigram, le focus est désormais placé automatiquement dans la liste des échanges.
* Ajout de Ctrl+Alt+Up/Down pour parcourir les échanges contenant des mentions non lues.

### Version 5.6.0

* Correction de la détection des messages enrichis afin que les messages contenant des autocollants ou des émojis ne soient plus annoncés à tort comme des messages enrichis.
* Ctrl+R utilise désormais le comportement natif d’Unigram pour enregistrer et envoyer les messages vocaux, tout en conservant les notifications de début et de fin d’enregistrement d’UnigramPlus.
* Mise à jour des traductions.

### Version 5.5.9

* Ajout de la prise en charge des messages enrichis. Ils sont annoncés lorsqu'ils reçoivent le focus et peuvent être ouverts avec Alt+C dans une fenêtre navigable.
* Les liens et le contenu mixte sont préservés, et les liens peuvent être activés depuis la fenêtre navigable.

### Version 5.5.8

* Correction des mises à jour automatiques : les versions sont désormais récupérées de manière sécurisée depuis GitHub et l'extension téléchargée est validée avant son installation.

* Compatibilité restaurée avec Unigram 12.7, où plusieurs raccourcis et annonces ne fonctionnaient plus.
* Les messages de sondage annoncent à nouveau la question et les options de réponse.
* La liste des sujets du forum annonce à nouveau l'aperçu du dernier message.
* Pendant un appel individuel, les raccourcis pour couper le micro (ALT+A), activer ou désactiver la caméra (ALT+V) et terminer l'appel (ALT+N) fonctionnent à nouveau.
* ALT+End se déplace à nouveau vers le message le plus récent de la discussion.

### Version 5.5.7

* La section des raccourcis clavier a été réorganisée en tableaux par catégorie et combine désormais les raccourcis d’Unigram et d’UnigramPlus.
* Lors de l'enregistrement d'un message vocal ou vidéo, NVDA annonce désormais "Enregistrement d'un message vocal" ou "Enregistrement d'un message vidéo" avec le temps écoulé, au lieu de "Tn voice message".

### Version 5.5.6

* Correction du bouton d'identité dans le profil d'un groupe ou d'un canal qui annonçait « Identity root » lorsqu'on passait le nom avec la touche Tab ; il annonce désormais le nom de la discussion et le nombre de membres.
* Ctrl+C n'est plus traité deux fois : il copie le lien lorsque le focus est sur un lien, et laisse sinon Unigram copier le message.

### Version 5.5.5

* La réponse à un message ou sa modification est désormais annoncée dans le champ de saisie au lieu de l'invite de message habituelle.
* Correction du son de saisie qui continuait parfois à être joué après la fermeture de l'application, après que l'interlocuteur a cessé d'écrire ou après avoir quitté la discussion ; il s'arrête maintenant dès que plus personne n'écrit dans la discussion ouverte.
* Mise à jour de la localisation birmane.

### Version 5.5.4

* Correction des annonces indésirables comme les compteurs de discussions non lues dans les dossiers, par exemple "Tous 535". La progression des transferts de fichiers est maintenant limitée aux contrôles d'envoi et de téléchargement d'Unigram et ignorée hors des fenêtres Unigram.
* Correction de la coexistence avec l'extension NVDA pour Telegram Desktop en activant UnigramPlus uniquement lorsque l'application exécutée est détectée comme Unigram.
* Ajout d'un bouton dans les paramètres d'UnigramPlus pour ouvrir le dossier des sons fournis afin de remplacer plus facilement les fichiers WAV en conservant les mêmes noms.
* Ajout d'une option pour flèche haut dans le champ d'édition de message afin de placer le focus sur le dernier message ayant reçu le focus.
* Reconstruction du chinois traditionnel en zh_TW et ajout du chinois simplifié en zh_CN.

### Version 5.5.3

* Ajout de l'annonce automatique de la progression des téléchargements et envois de fichiers. Une nouvelle option « Uniquement pendant l'envoi et le téléchargement » a été ajoutée au paramètre d'annonce des barres de progression et est désormais l'option par défaut. La combinaison ALT+U bascule à présent entre trois états : désactivé, uniquement pendant l'envoi/téléchargement, et annoncer toutes les barres de progression.
* Mise à jour du fichier readme et des traductions.

### Version 5.5.2

* Mise à jour du fichier readme et des traductions.
* Modification du son de l'indicateur de frappe.

### Version 5.5.1

* Correction du raccourci pour naviguer dans la liste des sujets de groupe (ALT+6). Il détecte désormais correctement la liste des sujets lors de l'ouverture d'un groupe de forum depuis la liste des conversations.
* Ajout d'un son indiquant que l'interlocuteur est en train d'écrire : un son est joué en boucle pendant que l'autre personne écrit dans la conversation et s'arrête lorsqu'elle a terminé. Cette fonctionnalité s'inspire de celle équivalente dans le script Unigram pour JAWS.

### Version 5.5.0

* Compatibilité avec NVDA 2026.1 ajoutée.

### Version 5.4.2

* Compatibilité avec NVDA 2025.3.3 ajoutée.

### Version 5.4.1

* Compatibilité avec NVDA 2025.1.2 ajoutée.

### Version 5.4.0

* Correction d'un problème avec la liste des conversations.

### Version 4.6.0

* Ajout d'un raccourci clavier pour déplacer le focus sur la liste des conversations de groupe. Par défaut, cette fonction est attribuée à la combinaison ALT+6. Veuillez noter que souvent, lorsque l'on appuie sur la touche Entrée sur le groupe que l'on veut ouvrir, la liste des conversations peut ne pas s'afficher et il est alors nécessaire de mettre à nouveau le focus sur ce groupe et d'appuyer sur la touche Entrée. En règle générale, après la deuxième pression, une liste de conversations est affichée, et après cela nous pouvons appuyer sur une combinaison de touches qui déplacera le focus sur cette liste.
* Maintenant, la combinaison ALT+2 déplace le focus non seulement sur la liste des messages, mais aussi sur le profil ouvert, sur la liste ouverte des discussions de groupe, ou sur la section ouverte des paramètres.
* Maintenant dans les paramètres d'UnigramPlus, vous pouvez désactiver la prononciation des expressions "Administrateur" et "propriétaire" sur les messages dans les groupes.
* Les combinaisons pour accepter et rejeter les appels fonctionnent maintenant correctement.
* Désormais, la fonction d'annonce automatique des nouveaux messages et de l'activité de chat ne se désactive pas lors du redémarrage de NVDA, mais fonctionne jusqu'à ce que vous la désactiviez vous-même.
* Amélioration de l'affichage de certains éléments de l'interface.

### Version 4.5.0

* Adapté à la dernière version d'Unigram
* Maintenant si un message a été envoyé en réponse à un autre message, en appuyant sur la touche flèche gauche, vous pouvez entendre le texte du message en réponse auquel il a été envoyé
* Ajout de la localisation française
* Suppression de la possibilité d'ajouter des réactions aux messages avec des raccourcis clavier, car je n'ai pas pu adapter cette fonction aux changements de l'interface d'Unigram
* Correction de quelques bugs mineurs.

###Version 4.4.0

* La fonction d'annonce d'activité dans les échanges a été ajoutée. Par défaut, cette fonction est activée par une double pression sur la combinaison ALT+T. La fonction reste active jusqu'à ce que NVDA soit redémarré.
* La fonction d'annonce automatique des nouveaux messages dans un échange a été ajoutée. Par défaut, celle-ci d'active en appuyant sur ALT+L. Cette fonction ne reste active que jusqu'au redémarrage de NVDA. Notez que des problèmes de stabilité peuvent survenir si trop de nouveaux messages apparaissent rapidement dans l'échange.
* Ajout d'un raccourci clavier pour convertir des messages vocaux en texte. Par défaut, cette fonction est assignée à la combinaison NVDA+ALT+R. Veuillez noter que dans les cas où le message vocal est très long, la conversion en texte se fait par segments. Il se peut donc que, lorsque UnigramPlus vous informe que la conversion est terminée, seule une partie du message vocal soit effectivement convertie. Après quelques secondes, ce texte restant sera ajouté.
* Désormais, UnigramPlus signale les informations relatives aux comptes premium et aux comptes vérifiés lorsque vous naviguez dans la liste des échanges.

###Version 4.3.0

* Maintenant, UnigramPlus fonctionne correctement lorsque plusieurs échanges sont ouverts dans différentes fenêtres.
* Ajout d'un raccourci clavier pour déplacer le focus sur la zone du profil utilisateur si elle est ouverte. Le raccourci clavier par défaut est Alt+5.
* Correction de bugs mineurs.

###Version 4.2.0

* Le mécanisme de sauvegarde des paramètres d'UnigramPlus a été considérablement remanié. Désormais, les paramètres ne seront pas stockés dans le fichier de configuration NVDA,     mais dans son propre fichier de configuration. Cela devrait résoudre le problème des utilisateurs qui, après une mise à jour ou tout simplement soudainement, n'étaient plus en mesure d'utiliser UnigramPlus, en raison de problèmes d'accès au fichier de configuration NVDA. Malheureusement, vous devrez reconfigurer UnigramPlus, car après l'installation de cette mise à jour, tous les paramètres seront réinitialisés.
* Correction du problème de compatibilité d'UnigramPlus avec l'extension BluetoothAudio.
* Désormais, l'information selon laquelle le message n'est pas sélectionné ne sera pas signalée. Si un message est sélectionné, l'information sera annoncée avant le contenu du message.
* Maintenant, le numéro d'ordre des éléments dans un échange sera annoncé si vous avez activé la position de l'élément dans les paramètres NVDA.
* Ajout d'étiquettes à certains boutons.

###Version 4.1.0

* Ajout d'une commande pour épingler un message ou un échange. Par défaut, aucun raccourci clavier n'est attribué à cette fonctionnalité.
* Ajout d'un raccourci clavier pour appuyer sur le bouton "Nouvel échange". La commande par défaut pour cette fonctionnalité est Ctrl+n.
* Ajout d'un raccourci clavier pour appuyer sur le bouton "Joindre un média". La commande par défaut est Ctrl+Maj+a.
* Ajout d'un raccourci clavier pour aller à la liste des dossiers d'échanges. La commande par défaut est Alt+4. Cette fonctionnalité sera utile pour ceux qui utilisent plus de neuf dossiers d'échanges.
* Maintenant, lorsque vous passez d'un dossier à l'autre à l'aide des flèches, le focus ne sautera plus n'importe où.
* Désormais, lorsque vous passez d'un dossier à l'autre à l'aide des touches de raccourci, en plus du nom du dossier actif, le nombre d'échanges non lus dans ce dossier sera annoncé.
* Désormais, les fonctions telles que "Marquer un échange comme lu" et "Épingler un message ou un échange" fonctionnent également en sens inverse.
* Ajout de la traduction en roumain.

###Version 4.0.0

* Fourni la compatibilité avec Unigram 8.8. Comme l'interface d'Unigram a changé, j'ai dû réécrire une partie importante du code de l'extension.
* Ajout de la possibilité de reculer et d'avancer rapidement dans les messages vocaux. Pour l'avance rapide, utilisez la combinaison Ctrl+flèche droite et pour revenir en arrière, Ctrl+flèche gauche.
* Désormais, UnigramPlus signalera non seulement la présence de réactions dans les messages, mais annoncera également des informations détaillées sur celles-ci.
* Ajout de la possibilité de visualiser le texte du message dans une fenêtre pop-up. La commande par défaut pour cette fonctionnalité est ALT+C.
* Ajout d'un raccourci clavier pour ouvrir la fenêtre des préférences d'UnigramPlus. La commande par défaut pour cette fonctionnalité est NVDA+Ctrl+U.
* Ajout des traductions tchèque et roumaine.
* Correction du problème de mise à jour d'UnigramPlus pour les résidents ukrainiens.

###Version 3.2.3

* Ajout d'une traduction en chinois.
* Mise à jour des traductions existantes, y compris l'anglais.
* Correction de bugs mineurs.

###Version 3.2.0

* Suppression de fonctions telles que "Suivi de l'activité d'échange" et "Lire les nouveaux messages dans l'échange ouvert" car je n'ai pas réussi à les faire fonctionner correctement dans NVDA 2022.1.
* Amélioration de l'accessibilité de la fonction activation / désactivation du micro et de l'activation / désactivation de la caméra lors des appels. Maintenant, après avoir appuyé sur le raccourci pour ces deux fonctions, leur état sera annoncé.
* Correction d'un problème où la touche Entrée ne fonctionnait pas correctement sur certains éléments. Désormais, vous pouvez enregistrer des messages vocaux en maintenant la touche Entrée sur le bouton d'enregistrement.
* Vous pouvez désormais réaffecter des raccourcis clavier à des fonctions telles que "Répondre au message" et "Modifier le message". Vous avez également la possibilité d'affecter ces fonctions à des touches telles que Entrée, Retour arrière ou même les flèches gauche ou droite et sans que cela n'interfère avec ces touches sur d'autres éléments. Notez qu'aucune touche ne sera affectée à ces fonctions au début et vous ne pourrez les affecter que lorsque le focus sera sur l'un des messages d'un échange.
* Maintenant, la fonction "Annoncer le nom de l'expéditeur" devrait mieux fonctionner.
* Lorsque vous êtes sur un lien contenu dans un message, le texte du message ne sera pas prononcé avant le texte d'aperçu du lien.
* Nous avons apporté quantité de petites améliorations et corrigé de nombreux bugs.
* Maintenant, UnigramPlus devrait être nettement plus réactif.

###Version 3.1.0

* L'annonce des sondages a été améliorée. Les noms des utilisateurs qui ont répondu aux sondages sont désormais annoncés dans la fenêtre des résultats. Les sondages fourniront également des informations sur l'option correcte.
* La possibilité de réagir aux messages a été ajoutée, mais uniquement dans les échanges privés. Cette fonctionnalité est pour l'instant instable dans les groupes et les canaux. Dans les échanges privés, en appuyant sur NVDA + ALT + les chiffres de 1 à 5, vous pouvez utiliser les réactions suivantes : 1 - 👍, 2 - 👎, 3 - ❤, 4 - 🔥, 5 - 🥰.
* Ajout de la possibilité d'annoncer des informations sur les réponses existantes aux messages. Malheureusement, il n'est pas encore possible d'annoncer le nom des réactions disponibles.
* Ajout d'une touche de raccourci pour copier rapidement les données nécessaires aux diffusions.
* Correction d'un problème d'affichage des résultats en ligne qui apparaissait dans les dernières versions d'Unigram.

###Version 3.0.0

Attention ! UnigramPlus ne prendra plus en charge les versions NVDA antérieures à 21.2.0.
* Ajout d'étiquettes pour de nombreux éléments de l'interface utilisateur.
* Correction de quelques bugs.

###Version 2.9.0

* Désormais, le champ d'édition change de libellé selon que l'on répond au message ou qu'on le modifie.
* Ajout de la possibilité d'activer un dialogue de confirmation pour la suppression des messages ou des échanges en utilisant les touches de raccourci dans les paramètres.
* Ajout de la traduction serbe.
* Correction de petits problèmes.

###Version 2.8.0

* Ajout de la possibilité de mettre à jour l'extension à partir de celle-ci. Maintenant, pour vérifier les mises à jour et les installer, il suffit d'ouvrir les paramètres d'UnigramPlus et de cliquer sur le bouton approprié. Vous pouvez également activer la vérification automatique des mises à jour au démarrage de NVDA.
* Ajout d'une traduction en arabe.

###Version 2.7.0

* Vous serez désormais averti que le message a été transféré.
* Amélioration de la fonction de copie des messages. Désormais, si le texte contient un lien cliquable et que le focus est sur ce lien, l'appui sur CTRL+C copiera le lien au lieu du texte entier.
* Ajout d'une touche de raccourci pour copier les messages tout en conservant le formatage du texte. Cette fonction émule l'activation de l'élément correspondant dans le menu de l'application. Le raccourci clavier par défaut pour cette fonction est CTRL+Maj+C. En raison de cette fonctionnalité, le raccourci clavier pour ouvrir les commentaires a été modifié en CTRL+ALT+C.
* Ajout de la possibilité d'annoncer automatiquement les nouveaux messages dans l'échange ouvert. Par défaut, elle peut être activée en appuyant sur ALT+L.
* Ajout de touches de raccourci pour un affichage rapide des messages dans un échange. Appuyez sur NVDA+CTRL+ le numéro correspondant au numéro d'un message particulier dans l'ordre inverse, c'est-à-dire que si vous voulez afficher le dernier message, appuyez sur 1, si vous voulez afficher le message précédent, appuyez sur 2, etc.
* En appuyant maintenant sur ALT+T, vous obtiendrez des informations sur l'échange vocal actif dans le groupe actuel.

###Version 2.6.0

* Compatibilité avec NVDA 21.3.
* Ajout d'une touche de raccourci pour permettre la sélection des messages ou des échanges.
* Ajout d'un raccourci pour transférer des messages.
* Ajout d'un raccourci pour marquer un échange comme lu.
* Amélioration des performances des fonctionnalités existantes.


###Version 2.5.0

* Il y a maintenant une case à cocher qui, si elle est cochée, résout le problème d'enregistrement des messages vocaux que certains utilisateurs rencontrent.
* Ajout d'une touche de raccourci pour répondre à un message. Ceci dit, Vous pouviez le faire en faisant Entrée sur le message et vous pouvez donc réaffecter ce raccourci alternatif pour autre chose.
* Ajout d'un raccourci clavier pour l'édition des messages. Le raccourci clavier par défaut est ALT+Retour arrière.

###Version 2.4.0

* Vous entendrez désormais le nom de l'expéditeur lorsque vous sélectionnez un message.
* Lorsque vous sélectionnez une discussion de groupe qui contient des messages non lus, vous serez averti si des réponses vous sont adressées dans ce groupe.
* Les performances des fonctionnalités ajoutées dans la mise à jour précédente ont également été améliorées.

###Version 2.3.0

* Amélioration de l'accessibilité des messages contenant plusieurs pièces jointes multimédia. Auparavant, la légende d'un message contenant plus d'une pièce jointe ne pouvait être consultée qu'en utilisant la navigation par objet. Désormais, cette légende sera lue immédiatement après avoir sélectionné un tel message.
* Amélioration de l'accessibilité des messages contenant des sondages. Désormais, lorsque vous sélectionnez un tel message, vous entendrez le nombre de personnes qui ont déjà voté, ainsi que toutes les options de réponse avec le résultat pour chaque option.
* Amélioration de l'accessibilité des messages contenant des URL. Désormais, si l'URL comporte une description, celle-ci sera également lue. Par exemple, si le message comporte une URL YouTube, le titre et la description de cette vidéo seront lus juste après l'URL elle-même. En outre, si l'URL comporte plus de 30 caractères, elle sera raccourcie pour faciliter la lecture de la description qui suit.
* Amélioration de l'accessibilité du panneau de résultats des requêtes intégrées... Pour naviguer dans les résultats des requêtes intégrées, utilisez les combinaisons Ctrl+ flèche haut et Ctrl+flèche bas.
* Ajout d'une touche de raccourci pour ouvrir les commentaires.

###Version 2.2.0

* Ajout d'une touche de raccourci pour supprimer les messages ou les échanges juste pour vous mais aussi des deux côtés. Cette fonction est liée à la langue de l'interface Unigram, elle peut donc ne pas fonctionner avec certaines traductions.
* Dans les paramètres, vous pouvez choisir le type de notifications, texte ou audio.
* Ajout de la possibilité de spécifier la langue d'interface que vous utilisez avec Unigram dans les paramètres. Ceci est nécessaire pour l'utilisation des fonctions associées à certaines traductions.
* Ajout d'une touche de raccourci pour ouvrir le profil de l'échange actuel.
* Maintenant, après avoir fermé un échange, le focus se déplace vers la liste des échanges et non vers le bouton "Ouvrir le menu de navigation".

###Version 2.1.0

* Lorsque vous passez d'un dossier à l'autre dans la liste des échanges, le nom du dossier en cours est annoncé.
* Dans la liste des échanges, vous entendez le nom du celui-ci, suivi de son type.
* Amélioration de la fonction de déplacement du focus dans la liste des échanges. Elle devrait maintenant se comporter de manière plus précise et sans délai.
* Les paramètres de l'extension sont devenus encore plus flexibles, car une section avec certaines options d'UnigramPlus est apparue dans le menu des préférences de NVDA.
* Ajout de la traduction polonaise.
* De nombreuses petites corrections et améliorations.

###Version 2.0.0

* La fonction permettant d'annoncer le statut "Vu" et "Non vu" avant la lecture du contenu du message fonctionne désormais dans les localisations espagnole, portugaise, croate, turque et perse.
* Amélioration de la fonction d'annonce de la barre de progression. Désormais, lorsque ce mode est activé, tous les indicateurs de progression ne sont pas annoncés, mais seulement ceux qui sont en focus.
* Si vous appuyez sur la barre d'espacement dans un message qui contient un fichier dont le téléchargement n'est pas terminé, vous serez informé que le téléchargement a été mis en pause.
* Ajout d'une traduction en portugais.
* Correction de quelques petits problèmes et amélioration des performances.

###Version 1.9.0
* Une touche de raccourci a été ajoutée pour basculer le niveau d'annonce des barres de progression entre les valeurs suivantes
    * "Annoncer toutes les barres de progression",
    * "Annoncer certaines barres de progression",
    * "Annoncer toutes les barres de progression sauf celle de la lecture des messages vocaux",
    * "N'annoncer aucune barre de progression".
Pour les utilisateurs dont le téléchargement automatique des médias est désactivé dans Unigram, le niveau d'annonce des barres de progression peut être défini sur "Annoncer toutes les barres de progression sauf celle de la lecture des  messages vocaux" et pour ceux qui l'ont activé, il est préférable de le définir sur "Ne pas annoncer les barres de progression".
* Ajout des traductions espagnole, croate et perse.
* Correction de bogues mineurs des versions précédentes.

###Version 1.8.0

* Le nom et la taille du fichier sont énoncés lorsque le curseur est placé sur le bouton "Ouvrir fichier" ou "Télécharger fichier". Lorsque le curseur est placé sur le bouton de lecture du fichier audio, vous entendez son nom et sa durée.
* Ajout d'une touche de raccourci pour déplacer le focus sur le champ d'édition. Si le curseur est déjà dans le champ d'édition, après avoir appuyé sur la touche de raccourci, il sera déplacé à l'endroit où il était auparavant.
* La fonction de suivi des activités d'un échange est maintenant activée en appuyant deux fois sur ALT+T. Vous pouvez simplement l'activer ou l'activer temporairement jusqu'à la prochaine fermeture de l'application.
* Ajout de la possibilité de sélectionner le type de notification pour l'enregistrement des messages vocaux. Cela se fait en appuyant deux fois sur la touche de raccourci Ctrl+d. Là, vous pouvez choisir entre le son, une notification textuelle ou le retour au comportement standard d'enregistrement des messages vocaux.

###Version 1.7.0

La fonction d'enregistrement des messages vocaux a été considérablement améliorée. L'enregistrement, l'envoi et l'annulation de ceux-ci sont accompagnés de sons caractéristiques. De plus, lors de l'exécution de ces fonctions, le focus reste à sa position et ne saute ni sur le bouton d'enregistrement ni sur le champ de saisie du message.

###Version 1.7.0

* Ajout de la possibilité de suivre l'activité de l'échange. Cette option peut être activée en appuyant sur ALT+Maj+T et reste active jusqu'à la fermeture d'Unigram ou le prochain redémarrage de NVDA.
* Le raccourci clavier qui active le bouton "Plus d'options" fonctionne désormais dans la fenêtre d'échange vocal et dans la fenêtre d'appel.

###Version 1.6.0

* Si le média joint au message est ouvert à l'aide de la barre d'espacement, après sa fermeture, le focus reviendra au dernier élément qui était sélectionné.
* Vous pouvez désormais revenir à l'échange vocal actif non seulement à partir du groupe actuel, mais aussi à partir de n'importe quel autre échange.
* En appuyant sur ALT+Maj+C dans un échange ouvert, vous retournerez à l'échange vocal au lieu d'appeler le contact.
* Si un message n'a pas été envoyé, vous serez averti dès que ce message aura été séletionné.
* Si le message sélectionné contient un lien, vous n'entendrez que le texte du lien et non l'intégralité du message.
* Correction d'un problème pour lequel les changements d'état des boutons tels qu'activation / désactivation du micro ou de la caméra n'étaient pas signalés dans les appels privés et les échangesvocaux.
* La fonction de copie de message vous permet désormais de copier le contenu des éléments dans la fenêtre d'affichage rapide du message.

###Version 1.5.1

Cette mise à jour corrige un grand nombre de bugs et améliore les performances de l'extension.

###Version 1.5.0

Cette mise à jour ajoute une touche de raccourci qui permet de cliquer sur le bouton "Affichage instantané" dans un message s'il est inclus dans ce dernier. Par défaut, cette fonctionnalité est activée avec la touche de raccourci ALT+Q. Après l'ouverture d'un tel article, le focus ira automatiquement sur le premier élément de cet article, et après la fermeture, le focus reviendra sur le dernier message consulté. Nous avons également corrigé un problème où tous les éléments de l'article dans la fenêtre d'affichage instantané n'étaient pas lisibles, même s'ils contenaient du texte.

###Version 1.1.7

Ajout de la traduction en turc.
