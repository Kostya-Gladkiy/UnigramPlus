# Unigram Plus

* Autor: Kostya Gladkiy (Ucrânia)
* [Canal no Telegram](https://t.me/unigramPlus)
* Telegram: @unigramPlus
* Link de donactivos: [https://unigramplus.diaka.ua/donate](https://unigramplus.diaka.ua/donate)

Use o Unigram de uma forma mais confortável e produtiva. Este extra fornece muitas teclas de atalho para o uso rápido e confortável do Unigram e introduz muitas melhorias.
## Algumas das maiores melhorias são:
* Quando o foco está na lista de chat, informações como "chat, separadores, lista selecionada" não são anunciadas e se o cursor estiver na lista de mensagens,  não ouvirá a palavra "Lista".
* Quando o foco está no botão abrir ficheiro ou descarregar ficheiro, o nome e o tamanho do ficheiro serão falados, e se estiver no botão reproduzir de um ficheiro de áudio, ouvirá o seu nome e duração.
* Quando estiver numa mensagem de voz que está a ser reproduzida, ouvirá primeiro o tempo de reprodução e, em seguida, o restante das informações relevantes.
* Quando o foco está numa mensagem seleccionada de Conversas, primeiro ouvirá a informação se ela foi seleccionada e, em seguida, o conteúdo da mensagem.
* Agora, ao rolar por uma lista de mensagens ou Conversas, não ouvirá a palavra "lida", mas "não lida" será falada antes de ler a mensagem em si. atualmente, esse recurso funciona apenas em inglês, russo e ucraniano.
* A função de gravação de mensagem de voz foi significativamente modernizada. iniciar e enviar a gravação de uma mensagem de voz são acompanhados por sons distintos, enquanto o Unigram 13.0 e posteriores anunciam por si próprios uma gravação cancelada. além disso, quando essas operações são realizadas, o foco permanece na mesma posição e não salta para o botão de gravação ou o campo de edição.
* Adicionada a capacidade de rastrear a actividade de Conversas. Esta função é activada pressionando a combinação "ALT + T" duas vezes.
* Se os ficheiros de mídia anexados a uma mensagem forem abertos pressionando espaço, após fechá-los, o cursor retorna ao local onde estava anteriormente.
* Todos os sons de prompt de função ou apenas os prompts de reprodução de mensagem de voz podem ser desactivados.

## Sons personalizados
Os sons do UnigramPlus ficam na pasta `appModules\media` do complemento. Abra Configurações do NVDA > UnigramPlus e pressione **Abrir pasta de sons do UnigramPlus**. Para personalizar um som, copie para essa pasta o arquivo WAV substituto com o mesmo nome do som que deseja trocar, depois reinicie o NVDA ou recarregue os complementos. Atualizações do complemento podem restaurar os sons incluídos, portanto mantenha uma cópia dos seus arquivos personalizados.

## Informações do desenvolvedor, sobre donativos:
Se realmente gosta deste extra e deseja, e o mais importante, tem a oportunidade de apoiar o desenvolvedor financeiramente e, portanto, motivá-lo a continuar a desenvolver este extra, pode fazer isso transferindo uma pequena quantia usando os seguintes dados bancários: (link de doação ) (https://unigramplus.diaka.ua/donate), o número do cartão é 5169360009004502.
E lembre-se que todos que leram este post pensaram que alguém definitivamente apoiaria o desenvolvedor, mas não serei eu.
(nota dos tradutores: não se entende o que se quer dizer com a frase anterior)

<!-- shortcut-table-start -->
## lista de teclas de atalho:

> In the Category column, `UnigramPlus` identifies shortcuts provided by the add-on and `Unigram` identifies shortcuts built into Unigram.

> `Unigram (não documentado)` identifica atalhos implementados no código-fonte atual do Unigram, mas ainda não listados no seu Shortcuts.md oficial.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Navegação entre conversas

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+Tab / Alt+Arrow Up / Ctrl+Page Up** | Unigram | Next chat |
| **Ctrl+Shift+Tab / Alt+Arrow Down / Ctrl+Page Down** | Unigram | Previous chat |
| **Ctrl+Alt+Home** | Unigram (não documentado) | Primeira conversa |
| **Ctrl+Alt+End** | Unigram (não documentado) | Última conversa |
| **Ctrl+Alt+Up/Down** | UnigramPlus | Ir para a conversa seguinte ou anterior com menções não lidas |
| **ALT+1** | UnigramPlus | Mover o foco para a lista de conversação |
| **ALT+2** | UnigramPlus | Move focus to the last message in an open chat |
| **ALT+3** | UnigramPlus | Mover o foco para o rótulo de 'mensagens não lidas |
| **ALT+4** | UnigramPlus | Move focus to list of chat folders |
| **ALT+5** | UnigramPlus | Move focus to open profile |
| **ALT+6** | UnigramPlus | Move focus to the list of group threads |
| **ALT+D** | UnigramPlus | Mover o foco para o campo de edição. Se o foco já estiver no campo de edição, depois de premir as teclas de atalho, irá deslocar-se para onde estava anteriormente |

### Pesquisa

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+E** | Unigram | Chat search |
| **Ctrl+F** | Unigram | Messages search per chat |
| **Ctrl+Shift+F** | Unigram (não documentado) | Chat search |
| **Search key** | Unigram (não documentado) | Pesquisar na página atual |
| **ALT+I** | UnigramPlus | Go to the list with search results |
| **F3** | UnigramPlus | Go to the next search result |
| **Shift+F3** | UnigramPlus | Go to the previous search result |

### Texto selecionado na área de escrita

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (não documentado) | Refazer |
| **Alt+X** | Unigram (não documentado) | Converter quatro dígitos hexadecimais selecionados no carácter correspondente |
| **Ctrl+X** | Unigram | Cut |
| **Ctrl+C** | Unigram | Copy |
| **Ctrl+V** | Unigram | Paste |
| **Ctrl+A** | Unigram | Select All |
| **Ctrl+Shift+.** | Unigram | Citação |
| **Ctrl+B** | Unigram | Bold |
| **Ctrl+I** | Unigram | Italic |
| **Ctrl+U** | Unigram | Sublinhado |
| **Ctrl+Shift+X** | Unigram | Strikethrough |
| **Ctrl+Shift+M** | Unigram | Monospace |
| **Ctrl+Shift+P** | Unigram | Spoiler |
| **Ctrl+K** | Unigram | Create Link |
| **Ctrl+Shift+N** | Unigram | Remover formatação (texto normal) |

### Pastas

| Atalho | Categoria | Ação |
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
| **Ctrl+Shift+Down** | Unigram (não documentado) | Pasta seguinte |
| **Ctrl+Shift+Up** | Unigram (não documentado) | Pasta anterior |

### Ações de mensagens

| Atalho | Categoria | Ação |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Copy the message if it contains text. If the focus is on a link, the link will be copied |
| **ALT+Q** | UnigramPlus | Pressione o botão "Visão instantânea", se estiver contido na mensagem actual |
| **ALT+Delete** | UnigramPlus | Eliminar uma mensagem ou conversa |
| **Shift+Delete** | UnigramPlus | Eliminar mensagem ou conversa em ambos os lados |
| **Delete** | Unigram (não documentado) | Eliminar a mensagem selecionada ou com foco |
| **Ctrl+ALT+C** | UnigramPlus | Abrir comentários |
| **Enter** | UnigramPlus | Responder à mensagem |
| **ALT+F** | UnigramPlus | Reencaminhar mensagem |
| **Backspace** | UnigramPlus | Editar mensagem |
| **ALT+Shift+R** | UnigramPlus | Marcar conversa como lida |
| **Ctrl+Space** | UnigramPlus | Alternar para o modo de seleção |
| **Unassigned** | UnigramPlus | Guardar ficheiro como... |
| **Unassigned** | UnigramPlus | Pin a message or chat |
| **Left Arrow** | UnigramPlus | Announce the original message, the message that was replied to |
| **Right Arrow** | UnigramPlus | Move to the next media attachment in the focused message |
| **ALT+C** | UnigramPlus | Show message text in popup window |
| **ALT+W** | UnigramPlus | Announces the time a message was sent or received, as well as a list of reactions. Double-clicking toggles the announcement mode for this information. |
| **ALT+[** | UnigramPlus | Alternar se os cabeçalhos das mensagens são anunciados antes ou depois do conteúdo da mensagem |
| **NVDA+Ctrl+0-9** | UnigramPlus | Review one of the ten most recent messages; 1 is the newest and 0 is the tenth newest |
| **Ctrl+Shift+A** | UnigramPlus | Press "Attach file" button |
| **Ctrl+Shift+E** | Unigram (não documentado) | Abrir o seletor de emojis |
| **Ctrl+Shift+G** | Unigram (não documentado) | Abrir o seletor de GIF |
| **Ctrl+Shift+S** | Unigram (não documentado) | Abrir o seletor de autocolantes |
| **Ctrl+O** | Unigram (não documentado) | Abrir o seletor de ficheiros para enviar documentos |
| **Ctrl+N** | UnigramPlus | Press "New conversation" button |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Mensagens de voz e multimédia

| Atalho | Categoria | Ação |
|---|---|---|
| **ALT+P** | UnigramPlus | Reproduzir/pausar a mensagem de voz que está actualmente a tocar |
| **ALT+S** | UnigramPlus | Aumentar/diminuir a velocidade de reprodução de mensagens de voz |
| **ALT+E** | UnigramPlus | Fechar o leitor de áudio |
| **NVDA+ALT+R** | UnigramPlus | Convert voice message to text |
| **Ctrl+ALT+Right Arrow** | UnigramPlus | Fast forward a voice message |
| **Ctrl+ALT+Left Arrow** | UnigramPlus | Rewind voice message |

### Gravação de mensagens

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+R** | Unigram | Start record |
| **Ctrl+R (again)** | Unigram | Send recorded |
| **Ctrl+D** | Unigram | Stop recording |
| **Space (while recording) / Ctrl+P** | Unigram | Pause recording |

### Chamadas

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+Home** | Unigram | Accept incoming call |
| **Ctrl+End** | Unigram | Reject incoming call |
| **Ctrl+Page Up** | Unigram | Toggle camera |
| **Ctrl+Page Down** | Unigram | Toggle microphone |
| **ALT+Shift+C** | UnigramPlus | Telefonar se for um contacto ou entrar na conversação de voz se for um grupo |
| **ALT+Shift+V** | UnigramPlus | Pressionar o botão de videochamada |
| **ALT+Y** | UnigramPlus | Aceitar chamada |
| **ALT+N** | UnigramPlus | Premir botão "Declinar chamada" se houver uma chamada recebida, botão "Terminar chamada" se uma chamada estiver em curso ou deixar conversa por voz se estiver activa. |
| **ALT+A** | UnigramPlus | Pressionar o botão "Activar/desactivar microfone" |
| **ALT+V** | UnigramPlus | Pressionar o botão "Activar/desactivar câmera |

### Outros atalhos

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+0** | Unigram | Saved messages |
| **Ctrl+W** | Unigram | Close current window |
| **Ctrl+Q** | Unigram | Close Unigram (main window only) |
| **Ctrl+Shift+Y** | Unigram | Change status |
| **Ctrl+Shift+W** | Unigram (não documentado) | Parar a reprodução de multimédia |
| **Ctrl+F4** | Unigram (não documentado) | Close current window |
| **Ctrl+L** | Unigram (não documentado) | Bloquear o Unigram |
| **Ctrl+M** | Unigram (não documentado) | Minimizar o Unigram |
| **Ctrl+J** | Unigram (não documentado) | Abrir transferências |
| **ALT+T** | UnigramPlus | Anunciar o nome e o status de uma conversa aberta |
| **NVDA+Alt+V** | UnigramPlus | Abrir informações de versão do Unigram e do UnigramPlus numa janela só de leitura |
| **ALT+M** | UnigramPlus | Abrir menu de navegação |
| **ALT+Shift+M** | UnigramPlus | Abrir as definições do Unigram |
| **ALT+Shift+P** | UnigramPlus | Abrir o perfil da conversa atual |
| **ALT+L** | UnigramPlus | Enable automatic reading of new messages in the current chat |
| **ALT+H** | UnigramPlus | Show a list of all UnigramPlus shortcuts |
| **ALT+U** | UnigramPlus | Alternar anúncios da barra de progresso |
| **ALT+Shift+L** | UnigramPlus | Copiar dados de transmissão para a área de transferência |
| **NVDA+ALT+U** | UnigramPlus | Open UnigramPlus settings window |
<!-- shortcut-table-end -->

## Lista de alterações:

### Versão 5.8.6

* A barra de espaços volta a reproduzir, abrir e transferir o conteúdo multimédia de uma mensagem no Unigram 13.0 e versões posteriores. Desde o Unigram 13.0, o conteúdo de uma mensagem com fotografia, vídeo, GIF, ficheiro, música ou de uma mensagem de voz é o próprio botão que faz isso. O Unigram 13.0.1 devolveu a esse botão o identificador que o UnigramPlus procura, exceto nas mensagens de voz, em que o identificador passou para o botão de transcrição, pelo que a barra de espaços não fazia nada numa mensagem de voz. O UnigramPlus passa a reconhecer o botão próprio de uma mensagem de voz pelo progresso da transferência que este indica. O Unigram 13.1.1 continua a não ter nenhuma ação para a barra de espaços numa mensagem fora do modo de seleção, pelo que o UnigramPlus prime esse botão: a barra de espaços reproduz ou pausa uma mensagem de voz ou uma música, abre uma fotografia, um vídeo ou um GIF no visualizador e transfere ou abre um ficheiro.
* Depois de a barra de espaços reproduzir uma mensagem de voz ou uma música ou transferir um ficheiro, o foco fica na mensagem, e o Escape seguinte já não o leva de volta para lá. Só o visualizador precisa disso, mas no Unigram 13.0 e versões posteriores um ficheiro ou uma música é tão largo como uma fotografia, pelo que o UnigramPlus o tomava por uma.
* A barra de espaços já não abre autocolantes nem pré-visualizações de ligações. O Unigram 13.0.1 deu-lhes o mesmo identificador dos botões multimédia, mas são ligações. Numa pré-visualização de ligação que mostra uma fotografia ou um vídeo, a barra de espaços continua a abrir a fotografia ou o vídeo.
* As setas para a direita e para a esquerda numa mensagem com vários anexos multimédia, como um álbum, voltam a anunciar cada fotografia, vídeo, ficheiro ou música no Unigram 13.0 e versões posteriores. Desde o Unigram 13.0, cada anexo contém apenas o botão próprio do seu conteúdo, pelo que o UnigramPlus deixou de encontrar o que distingue uma fotografia de um vídeo e anunciava a palavra provisória "Медіа" para cada anexo. Agora procura dentro desse botão: um vídeo tem aí o seu próprio botão de transferência, um ficheiro ou uma música o seu título, e uma fotografia nenhum dos dois.
* O Ctrl+Space agora também funciona na lista de conversas, onde antes não fazia nada. Tal como nas mensagens, a primeira vez que é premido ativa o modo de seleção com a conversa em foco a partir do menu de contexto da conversa e, a partir daí, cada vez que é premido seleciona ou desmarca a conversa em foco, tal como a barra de espaços faz no Unigram. Em seguida, o UnigramPlus anuncia se a conversa está selecionada. Desmarcar a última conversa selecionada termina o modo de seleção. Enquanto a lista de conversas está no modo de seleção, o UnigramPlus também diz "Seleccionado" antes do nome de uma conversa selecionada quando o foco chega a ela, tal como faz com as mensagens.
* Foi adicionado o Alt+Shift+M, que abre as definições do Unigram no Unigram 13.1 e versões posteriores, tal como faz o UnigramPlusRussianMod. O Unigram 13.1 moveu as definições do painel lateral para um separador abaixo da lista de conversas. O Alt+Shift+M seleciona esse separador e depois move o foco para o início das definições: para a primeira das suas outras contas ou, se tiver sessão iniciada em apenas uma conta, para "Adicionar conta". Nas versões do Unigram anteriores à 13.1, e numa janela estreita que mostra apenas a conversa aberta, o UnigramPlus anuncia "Definições indisponíveis".

### Versão 5.8.5

* Alt+M volta a abrir o menu de navegação no Unigram 13.1 e versões posteriores. O Unigram 13.1 substituiu o painel lateral por um menu que se abre a partir do mesmo botão, e esse botão já não é um botão de alternar, pelo que o UnigramPlus não o encontrava e anunciava "Menu de navegação indisponível".
* Corrigido o Ctrl+Space no modo de seleção do Unigram. Nesse modo, o menu de contexto de uma mensagem selecionada não tem o comando Selecionar, pelo que o UnigramPlus percorria o menu sem o encontrar e a mensagem continuava selecionada. Agora o Ctrl+Space funciona como no Unigram 13.1.1: a primeira vez que é premido continua a ativar o modo de seleção a partir do menu de contexto e, a partir daí, cada vez que é premido seleciona ou desmarca a mensagem em foco, tal como a barra de espaços faz no Unigram. Em seguida, o UnigramPlus anuncia se a mensagem está selecionada. Desmarcar a última mensagem selecionada termina o modo de seleção.
* No modo de seleção, a barra de espaços e Enter numa mensagem passam a selecioná-la ou desmarcá-la, tal como no Unigram, em vez de reproduzirem o seu conteúdo multimédia ou procurarem Responder no menu de contexto, e o Backspace já não procura Editar nesse menu.
* Atualizada a compatibilidade com o NVDA 2026.3. O UnigramPlus já não utiliza partes obsoletas da API do NVDA, que o NVDA ainda suporta, mas poderá remover numa versão futura: as caixas de mensagem da verificação de atualizações, a forma antiga de abrir as definições do UnigramPlus e uma constante de tecla utilizada ao avançar ou recuar em mensagens de voz.
* Atualizadas as traduções polaca e vietnamita.

### Versão 5.8.4

* Com a opção "Mover automaticamente o foco para a lista de conversas ao iniciar o Unigram" ativada, o foco permanece agora na janela pop-up que o Unigram mostra ao iniciar, como o pedido para aderir a um grupo aberto a partir de uma ligação de convite. Desde a versão 5.6.1, o UnigramPlus movia o foco da janela pop-up para a lista de conversas por trás dela, pelo que a janela pop-up era ignorada.
* Atualizada a tradução vietnamita.

### Versão 5.8.3

* Removido o tratamento de Enter e espaço que o UnigramPlus acrescentou à lista de categorias de definições do Unigram na versão 4.8.0. No Unigram 13.0 e posteriores, cada categoria de definições é um botão que se abre por si próprio com Enter ou espaço, e o foco vai para esse botão e não para o item de lista que o complemento tratava, pelo que esse tratamento já não tinha efeito aí. Agora, ao abrir uma categoria, o foco permanece nela, tal como no próprio Unigram, em vez de ser movido para dentro da categoria. Esse tratamento também afetava outras listas de separadores, como os separadores Emoji, GIF e Autocolantes, onde intercetava Enter e espaço; agora estas teclas também chegam ao Unigram nesses locais.
* Nas definições do Unigram, Alt+1 move agora o foco para a categoria de definições aberta, ou para a primeira categoria se nenhuma estiver aberta. Antes, procurava a lista de categorias numa posição fixa da página de definições e depois tentava mover o foco para um elemento que não pode receber o foco no Unigram 13.0.
* Removido código que já não podia ser executado, sem qualquer alteração na utilização. Antes do Unigram 9.5, alguns itens de lista eram anunciados por um nome de classe interno, que o UnigramPlus substituía por um nome legível; o Unigram 9.5 mudou o nome dessas classes, pelo que essas substituições nunca mais se aplicaram. Foi também removido o tratamento que abria a explicação de um questionário numa janela separada, desativado desde a versão 5.2.0.
* Atualizadas as traduções polaca e vietnamita.

### Versão 5.8.2

* Corrigidos erros do NVDA na nova versão beta do Unigram em WinUI 3. Desde a versão 5.5.6, era registado um erro sempre que se regressava ao Unigram ou se escrevia com um editor de método de introdução (IME), como os de chinês, japonês ou coreano. A versão UWP do Unigram não era afetada.
* O UnigramPlus já não interfere com os anúncios de foco do Telegram Desktop quando o complemento Telegram Desktop não está instalado.
* Removida a notificação que o UnigramPlus dava ao cancelar a gravação de uma mensagem de voz ou de vídeo. O Unigram 13.0 e posteriores anunciam por si próprios uma gravação cancelada, seja com Ctrl+D ou com o botão de cancelar, pelo que deixa de ser ouvida duas vezes. Uma gravação que demora a aparecer na conversa também já não é anunciada como cancelada. O início e o envio de uma gravação continuam a ser anunciados, e a opção correspondente chama-se agora "Notificação ao iniciar ou enviar a gravação de uma mensagem de voz".
* Atualizadas as traduções polaca e vietnamita.

### Versão 5.8.1

* Removida a solução alternativa para a duração das chamadas. O Unigram 12.10 e posteriores anunciam por si próprios a duração de uma mensagem de chamada, pelo que o UnigramPlus já não a acrescenta e deixa de ser ouvida duas vezes.
* Corrigido o complemento não arrancar em versões antigas do NVDA que não fornecem o módulo utils.security.
* Removidas importações que o complemento já não utiliza.
* Atualizada a tradução vietnamita.

### Versão 5.8.0

* As verificações periódicas em segundo plano do complemento deixaram de ser executadas no ciclo principal do NVDA, pelo que a navegação pelas conversas, a escrita e a fala já não ficam bloqueadas enquanto o Unigram responde.
* Todos os comportamentos acrescentados depois da versão 5.4 podem agora ser ligados ou desligados nas definições do UnigramPlus, reunidos sob um único título: a forma como o botão de gravar mensagem de voz é anunciado, o texto formatado das mensagens com ALT+C, a etiqueta do botão de identidade do perfil, o anúncio de responder e editar no campo de mensagem, o anúncio suprimido de "lista" antes das mensagens, o estado em direto do microfone e da câmara durante uma chamada e a contagem de não lidas ao mudar de pasta de conversas. Cada um mantém o comportamento atual por predefinição e cada etiqueta indica que comportamento da versão 5.4 repõe.
* Corrigida a barra de espaços que não reproduzia mensagens de voz, música e ficheiros.
* Corrigido o Enter que não respondia a uma mensagem, o Backspace que não a editava, o ALT+C que não mostrava o respetivo texto e o ALT+D que não regressava a ela.
* Corrigido o ALT+E que não fechava o reprodutor de áudio.
* Corrigidos o Ctrl+ALT+Esquerda e o Ctrl+ALT+Direita que não avançavam nem recuavam a reprodução da mensagem de voz, incluindo quando a seta é premida novamente com os modificadores ainda premidos.
* O cancelamento de uma gravação de voz é anunciado cerca de um segundo e meio depois de esta parar, em vez de cinco segundos depois.
* Com a opção do botão de gravação da versão 5.4 selecionada, o foco permanece no campo de mensagem quando a gravação começa, continuando o Tab a alcançar o botão de gravar.
* Corrigidos vários atalhos que falhavam em silêncio quando faltava na árvore do Unigram um elemento que esperavam encontrar: ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Shift+L, ALT+Shift+P, Shift+Delete, a navegação por multimédia e os controlos de chamada.
* A conversão de uma mensagem de voz em texto deixou de iniciar uma nova thread a cada meio segundo enquanto espera e desiste em vez de esperar indefinidamente.

### Versão 5.7.3

* NVDA+Alt+V passa agora a apresentar a versão do UnigramPlus numa nova linha.

### Versão 5.7.2

* NVDA+Alt+V passa a abrir as informações de versão numa janela de várias linhas só de leitura.

### Versão 5.7.1

* Corrigido o tratamento dos botões de reação do Unigram 12.10.2 como mensagens, para que os atalhos de navegação por mensagens deixem de substituir a respetiva ação de alternância nativa.

### Versão 5.7.0

* Foram restaurados os anúncios ao mudar de pasta com uma contagem de não lidas diferente de zero, mantendo as proteções do monitor de progresso de transferência de ficheiros.
* A lista de atalhos foi atualizada a partir do código-fonte atual do Unigram e foram identificados os atalhos integrados que ainda não constam no seu Shortcuts.md oficial.

### Versão 5.6.9

* Corrigido um erro que poderia ocorrer quando o NVDA entrava num ambiente de trabalho seguro, como num pedido do UAC, enquanto o acompanhamento de mensagens em segundo plano do UnigramPlus estava activado.
* Corrigida a classificação das linhas de tópicos de Mensagens guardadas no Unigram 12.10.1+ como mensagens apenas porque os seus resumos nativos contêm horas de envio ou recepção.
* Removida a solução alternativa obsoleta para nomes de tópicos de Mensagens guardadas; as versões actuais do Unigram passam agora a disponibilizar nativamente nomes acessíveis para conversas de Mensagens guardadas.
* Actualizada a compatibilidade com o NVDA 2026.2.
* Actualizadas as traduções polaca e birmanesa.

### Versão 5.6.8

* Corrigida a falha do Alt+C quando o WhatsApp Enhancer está instalado, causada por uma colisão de nomes de módulos auxiliares em appModules.

### Versão 5.6.7

* O atalho para anunciar as versões instaladas do Unigram e do UnigramPlus foi alterado de NVDA+Shift+V para NVDA+Alt+V para evitar conflitos de atalhos.
* Corrigido Shift+Delete para eliminar conversas e sair de grupos ou canais nas versões atuais do Unigram, incluindo a confirmação automática da janela de contexto.

### Versão 5.6.6

* Adicionado NVDA+Shift+V para anunciar as versões instaladas do Unigram e do UnigramPlus.
* Eliminada a solução temporária para os botões em linha do Unigram 12.9 depois de o Unigram 12.9.1 corrigir os rótulos dos botões; isto evita bloqueios da UIA nas listas de bots, na navegação por mensagens, nas reações e na lista de conversas.
* Atualizadas todas as traduções e manuais para a versão 5.6.6.

### Versão 5.6.5

* Corrigida a tecla Enter para responder a mensagens e Alt+Shift+R para marcar conversas como lidas nas versões atuais do Unigram.
* Removidos o modo de vista Web e a respetiva definição; Alt+C passa a abrir sempre o texto da mensagem na janela de pop-up wx original.
* Atualizadas todas as traduções e os manuais para a versão 5.6.5.

### Versão 5.6.4

* Corrigido Shift+Delete usando o comando Delete nativo do Unigram e confirmando automaticamente a eliminação para ambos os lados.
* Alt+2 passa a ativar primeiro o botão “Ir para o fim” do Unigram; o atalho Alt+End duplicado foi removido.
* Adicionada uma definição para escolher entre a janela wx clássica (predefinida) e a vista Web ao apresentar o texto da mensagem com Alt+C.
* Passa a ser usado o texto acessível oficial das mensagens avançadas do Unigram, com uma correção temporária para botões em linha sem etiqueta no Unigram 12.9.
* A lista de atalhos foi atualizada segundo a documentação oficial do Unigram 12.9.
* Adicionada uma correção temporária para que as linhas de tópicos das Mensagens guardadas anunciem o título visível da conversa em vez de um nome de tipo do TDLib.

### Versão 5.6.3

* Corrigido um problema intermitente em que o NVDA anunciava «lista» antes de uma mensagem ao navegar com as setas para cima e para baixo.
* Adicionada uma definição para o comportamento de Alt+[ que anuncia os cabeçalhos das mensagens após o respetivo conteúdo; está desativada por predefinição.
* Adicionada uma notificação sonora opcional ao chegar ao fim de uma conversa.

### Versão 5.6.2

* Corrigido o Ctrl+Alt+Left/Right Arrow para recuar e avançar numa mensagem de voz em reprodução.
* Corrigido o Alt+I para aceder à lista integrada dos resultados de pesquisa da conversa.
* Adicionado o Alt+[ para alternar o anúncio dos cabeçalhos antes ou depois do conteúdo da mensagem. Quando os cabeçalhos ficam depois do conteúdo, os nomes dos ficheiros são anunciados primeiro nas secções de ficheiros.

### Versão 5.6.1

* Corrigido o acompanhamento do progresso da transferência de ficheiros para parar nos 100% e deixar de criar uma nova thread em cada ciclo de verificação.
* Ao abrir o Unigram, o foco passa agora automaticamente para a lista de conversas.
* Adicionado Ctrl+Alt+Up/Down para percorrer conversas com menções não lidas.

### Versão 5.6.0

* Corrigida a deteção de mensagens enriquecidas para que as mensagens com autocolantes e emojis deixem de ser anunciadas incorretamente como mensagens enriquecidas.
* Ctrl+R passa a utilizar o comportamento nativo do Unigram para gravar e enviar mensagens de voz, mantendo as notificações de início e fim da gravação do UnigramPlus.
* Traduções atualizadas.

### Versão 5.5.9

* Adicionado suporte a mensagens enriquecidas. São anunciadas quando recebem o foco e podem ser abertas com Alt+C numa janela navegável.
* As ligações e o conteúdo misto são preservados, e as ligações podem ser ativadas a partir da janela navegável.

### Versão 5.5.8

* Corrigidas as atualizações automáticas: as versões são agora obtidas de forma segura do GitHub e o extra transferido é validado antes da instalação.

* Compatibilidade restaurada com o Unigram 12.7, onde vários atalhos e anúncios tinham deixado de funcionar.
* As mensagens de sondagem voltam a anunciar a pergunta e as opções de resposta.
* A lista de tópicos do fórum volta a anunciar a pré-visualização da última mensagem.
* Durante uma chamada individual, os atalhos para silenciar o microfone (ALT+A), ativar ou desativar a câmara (ALT+V) e terminar a chamada (ALT+N) voltam a funcionar.
* ALT+End volta a ir para a mensagem mais recente da conversa.

### Versão 5.5.7

* A secção de atalhos de teclado foi reorganizada em tabelas por categoria e agora combina os atalhos do Unigram e do UnigramPlus.
* Ao gravar uma mensagem de voz ou de vídeo, o NVDA anuncia agora "A gravar uma mensagem de voz" ou "A gravar uma mensagem de vídeo" juntamente com o tempo decorrido, em vez de "Tn voice message".

### Versão 5.5.6

* Corrigido o botão de identidade no perfil de um grupo ou canal que anunciava "Identity root" ao passar pelo nome com a tecla Tab; agora anuncia o nome da conversa e o número de membros.
* O Ctrl+C deixou de ser processado duas vezes: copia a ligação quando o foco está sobre uma ligação e, nos restantes casos, deixa o Unigram copiar a mensagem.

### Versão 5.5.5

* Responder ou editar uma mensagem é agora anunciado no campo de introdução de mensagem, em vez do habitual aviso de mensagem.
* Corrigido o som de escrita que por vezes continuava a tocar após fechar a aplicação, depois de a outra pessoa parar de escrever ou após sair do chat; agora para assim que ninguém está a escrever no chat aberto.
* Atualizada a localização birmanesa.

### Versão 5.5.4

* Corrigidos anúncios indesejados, como contadores de chats não lidos em pastas, por exemplo "Todos 535". O progresso de transferência de arquivos agora fica limitado aos controles de envio e download do Unigram e é ignorado fora das janelas do Unigram.
* Corrigida a convivência com o complemento de NVDA para Telegram Desktop, ativando o UnigramPlus apenas quando o aplicativo em execução é detectado como Unigram.
* Adicionado um botão nas configurações do UnigramPlus para abrir a pasta de sons incluída, facilitando substituir arquivos WAV usando os mesmos nomes.
* Adicionada uma opção para a seta para cima no campo de edição de mensagem que move o foco para a última mensagem focada.
* O chinês tradicional foi recriado como zh_TW e o chinês simplificado foi adicionado como zh_CN.

### Versão 5.5.3

* Adicionado o anúncio automático do progresso de envio e transferência de ficheiros. Foi adicionada uma nova opção "Apenas durante o envio e transferência" à definição de anúncio das barras de progresso e é agora a opção predefinida. O atalho ALT+U alterna agora entre três estados: desativado, apenas durante envio/transferência, e anunciar todas as barras de progresso.
* Atualização do readme e das traduções.

### Versão 5.5.2

* Atualização do readme e das traduções.
* Alterado o som do indicador de escrita.

### Versão 5.5.1

* Corrigido o atalho para navegar pela lista de tópicos do grupo (ALT+6). Agora deteta corretamente a lista de tópicos ao abrir um grupo de fórum a partir da lista de conversas.
* Adicionado som indicador de escrita: é reproduzido um som em ciclo enquanto o outro lado está a escrever na conversa e para quando termina. Esta funcionalidade é inspirada na funcionalidade equivalente do script Unigram para JAWS.

### Versão 5.5.0

* Adicionada compatibilidade com o NVDA 2026.1.

### Versão 5.4.2

* Adicionada compatibilidade com o NVDA 2025.3.3.

### Versão 5.4.1

* Adicionada compatibilidade com o NVDA 2025.1.2.

### Versão 5.4.0

* Corrigido um problema na lista de conversas.

### Versão 1.9.0
* Adicionada uma combinação que alterna o nível de prompts auditivos entre valores como: "anunciar todas as barras de progresso", "anunciar todas as barras de progresso, exceto para reprodução de mensagem de voz" e "não anunciar barras de progresso". Para aqueles utilizadores que têm o carregamento automático de mídia desactivado no Unigram, o valor pode ser definido como "anunciar todas as barras de progresso, exceto aquelas para reprodução de mensagens de voz", e para aqueles que o têm activado, é preferível deixá-lo em "sem anúncio de barras de progresso".
* Adicionadas traduções para espanhol, croata e persa
* Corrigidos pequenos bugs de versões anteriores

### Versão 1.8.0
* Quando o foco é colocado no botão abrir ficheiro ou baixar ficheiro, o nome e o tamanho do ficheiro em questão serão falados, E quando o foco estiver no botão reproduzir em um ficheiro de áudio, ouvirá o seu nome e duração.
* Adicionada função para mover o foco para o campo de edição de mensagem. Se o foco já estiver neste campo, clicar irá mover para o último item em foco.
* Agora a função de seguimento de actividade de chat é activada pressionando ALT + T duas vezes. Ppode simplesmente activá-la, activá-la temporariamente, até a próxima vez que fechar o aplicativo.
* Agora também foi adicionada a capacidade de seleccionar o tipo de notificação para gravar mensagens de voz. Isso é feito pressionando a combinação control + d duas vezes. Aqui pode escolher entre um alerta de áudio, um alerta de texto e retornar ao comportamento padrão de gravação de mensagem de voz.

### Versão 1.7.0
* A função de gravação de mensagem de voz foi significativamente modernizada. gravar, enviar e cancelar são acompanhados por sons distintos. Além disso, enquanto essas operações estão a ser realizadas, o foco permanece na mesma posição e não salta para o botão de gravação ou o campo de edição.
### Versão 1.7.0
* Adicionada capacidade de seguir a actividade de Conversas. Esta opção pode ser activada pressionando ALT + shift + T e permanecerá activa até que o Unigram seja fechado ou até a próxima reinicialização do NVDA.
* As teclas de atalho que activam o botão de mais opções agora funcionam no chat de voz e na janela de chamada.

### Versão 1.6.0
* Se a mídia anexada de uma mensagem for aberta pressionando espaço, após fechá-la, o cursor retornará à sua posição anterior.
* Agora pode retornar ao chat de voz activo, não apenas do grupo actual, mas também de qualquer outro chat.
* Pressionar ALT + shift + C num chat aberto retornará ao chat de voz em vez de ligar para o contacto em questão.
* Se uma mensagem não for enviada, será notificado assim que a mensagem estiver em foco.
* Se uma mensagem em destaque contiver um link, ouvirá apenas o texto do link em si, não a mensagem em sua totalidade.
* Corrigido um problema em que a mudança de estado não era anunciada para botões como ligar / desligar o microfone e ligar / desligar a câmera em chamadas privadas e chats de voz.
* Agora, o recurso de cópia de mensagem permite que copie o conteúdo dos elementos na janela de visualização rápida de uma postagem.

### Versão 1.5.1

Esta actualização corrige um grande número de bugs e melhora o desempenho do extra.

### Versão 1.5.0
Esta actualização adiciona uma combinação que pressiona o botão "visualização rápida" na mensagem, se houver. Por padrão, esta função é activada com a combinação ALT + Q. Após a abertura deste artigo, o foco será automaticamente colocado no primeiro item, e após o fechamento, o foco retornará para a última mensagem vista. Também corrigimos um problema em que todos os itens de um artigo não eram lidos na janela de visualização rápida, mesmo que contivessem texto.
### Versão 1.1.7

Adicionada tradução turca

## Tradução Portuguesa:
Equipa Portuguesa do NVDA: Ângelo Abrantes <ampa4374@gmail.com> e Rui Fontes <Rui Fontes <rui.fontes@tiflotecnia.com>
14-08-2021
