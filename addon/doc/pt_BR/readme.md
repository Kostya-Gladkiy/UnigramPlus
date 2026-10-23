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
* A função de gravação de mensagem de voz foi significativamente modernizada. iniciar e enviar a gravação de uma mensagem de voz são acompanhados por sons distintos, enquanto o Unigram 13.0 e posteriores anunciam sozinhos uma gravação cancelada. além disso, quando essas operações são realizadas, o foco permanece na mesma posição e não salta para o botão de gravação ou o campo de edição.
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

> `Unigram (não documentado)` identifica atalhos implementados no código-fonte atual do Unigram, mas ainda não relacionados no Shortcuts.md oficial.

> [!TIP]
> You can customize UnigramPlus shortcuts from NVDA menu > Preferences > Input gestures.

### Navegação entre chats

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

### Texto selecionado na área de digitação

| Atalho | Categoria | Ação |
|---|---|---|
| **Ctrl+Z** | Unigram | Undo |
| **Ctrl+Y** | Unigram | Redo |
| **Ctrl+Shift+Z** | Unigram (não documentado) | Refazer |
| **Alt+X** | Unigram (não documentado) | Converter quatro dígitos hexadecimais selecionados em seu caractere correspondente |
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
| **Ctrl+Shift+Down** | Unigram (não documentado) | Próxima pasta |
| **Ctrl+Shift+Up** | Unigram (não documentado) | Pasta anterior |

### Ações de mensagens

| Atalho | Categoria | Ação |
|---|---|---|
| **Space** | UnigramPlus | Play or stop the focused voice or video message, or open media attached to the message |
| **Ctrl+C** | UnigramPlus | Copy the message if it contains text. If the focus is on a link, the link will be copied |
| **ALT+Q** | UnigramPlus | Pressione o botão "Visão instantânea", se estiver contido na mensagem actual |
| **ALT+Delete** | UnigramPlus | Excluir uma mensagem ou conversa |
| **Shift+Delete** | UnigramPlus | Excluir mensagem ou conversa de ambos os lados |
| **Delete** | Unigram (não documentado) | Excluir a mensagem selecionada ou em foco |
| **Ctrl+ALT+C** | UnigramPlus | Abrir comentários |
| **Enter** | UnigramPlus | Responder à mensagem |
| **ALT+F** | UnigramPlus | Encaminhar mensagem |
| **Backspace** | UnigramPlus | Editar mensagem |
| **ALT+Shift+R** | UnigramPlus | Marcar conversa como lida |
| **Ctrl+Space** | UnigramPlus | Alternar para o modo de seleção |
| **Unassigned** | UnigramPlus | Salvar arquivo como... |
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
| **Ctrl+Shift+S** | Unigram (não documentado) | Abrir o seletor de figurinhas |
| **Ctrl+O** | Unigram (não documentado) | Abrir o seletor de arquivos para enviar documentos |
| **Ctrl+N** | UnigramPlus | Press "New conversation" button |
| **Arrow Up** | Unigram | Edit last sent message |
| **Ctrl+Arrow Up** | Unigram | Reply to last sent message |
| **Esc / Alt+Arrow Left** | Unigram | Go back |
| **Alt+Arrow Right** | Unigram | Redo go back |

### Mensagens de voz e mídia

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
| **Ctrl+Shift+W** | Unigram (não documentado) | Parar reprodução de mídia |
| **Ctrl+F4** | Unigram (não documentado) | Close current window |
| **Ctrl+L** | Unigram (não documentado) | Bloquear o Unigram |
| **Ctrl+M** | Unigram (não documentado) | Minimizar o Unigram |
| **Ctrl+J** | Unigram (não documentado) | Abrir downloads |
| **ALT+T** | UnigramPlus | Anunciar o nome e o status de uma conversa aberta |
| **NVDA+Alt+V** | UnigramPlus | Abrir informações de versão do Unigram e do UnigramPlus em uma janela somente leitura |
| **ALT+M** | UnigramPlus | Abrir menu de navegação |
| **ALT+Shift+M** | UnigramPlus | Abrir as configurações do Unigram |
| **ALT+Shift+P** | UnigramPlus | Abrir o perfil da conversa atual |
| **ALT+L** | UnigramPlus | Enable automatic reading of new messages in the current chat |
| **ALT+H** | UnigramPlus | Show a list of all UnigramPlus shortcuts |
| **ALT+U** | UnigramPlus | Alternar anúncios da barra de progresso |
| **ALT+Shift+L** | UnigramPlus | Copiar dados de transmissão para a área de transferência |
| **NVDA+ALT+U** | UnigramPlus | Open UnigramPlus settings window |
<!-- shortcut-table-end -->

## Lista de alterações:

### Versão 5.8.6

* A barra de espaço volta a reproduzir, abrir e baixar a mídia de uma mensagem no Unigram 13.0 e versões posteriores. Desde o Unigram 13.0, o conteúdo de uma mensagem com foto, vídeo, GIF, arquivo, música ou de uma mensagem de voz é o próprio botão que faz isso. O Unigram 13.0.1 devolveu a esse botão o identificador que o UnigramPlus procura, exceto nas mensagens de voz, em que o identificador foi para o botão de transcrição, por isso a barra de espaço não fazia nada em uma mensagem de voz. Agora o UnigramPlus reconhece o botão próprio de uma mensagem de voz pelo progresso de download que ele informa. O Unigram 13.1.1 ainda não tem nenhuma ação para a barra de espaço em uma mensagem fora do modo de seleção, por isso o UnigramPlus pressiona esse botão: a barra de espaço reproduz ou pausa uma mensagem de voz ou uma música, abre uma foto, um vídeo ou um GIF no visualizador e baixa ou abre um arquivo.
* Depois que a barra de espaço reproduz uma mensagem de voz ou uma música ou baixa um arquivo, o foco permanece na mensagem, e o próximo Escape não o leva mais de volta para lá. Só o visualizador precisa disso, mas no Unigram 13.0 e versões posteriores um arquivo ou uma música é tão largo quanto uma foto, por isso o UnigramPlus o confundia com uma.
* A barra de espaço não abre mais figurinhas nem prévias de links. O Unigram 13.0.1 deu a elas o mesmo identificador dos botões de mídia, mas elas são links. Em uma prévia de link que mostra uma foto ou um vídeo, a barra de espaço continua abrindo a foto ou o vídeo.
* As setas para a direita e para a esquerda em uma mensagem com vários anexos de mídia, como um álbum, voltam a anunciar cada foto, vídeo, arquivo ou música no Unigram 13.0 e versões posteriores. Desde o Unigram 13.0, cada anexo contém apenas o botão próprio do seu conteúdo, por isso o UnigramPlus não encontrava mais o que diferencia uma foto de um vídeo e anunciava a palavra provisória "Медіа" para cada anexo. Agora ele procura dentro desse botão: um vídeo tem ali o seu próprio botão de download, um arquivo ou uma música o seu título, e uma foto nenhum dos dois.
* O Ctrl+Space agora também funciona na lista de conversas, onde antes não fazia nada. Assim como nas mensagens, a primeira vez que é pressionado ativa o modo de seleção com a conversa em foco pelo menu de contexto da conversa e, depois disso, cada pressionamento seleciona ou desmarca a conversa em foco, como a barra de espaço faz no Unigram. Em seguida, o UnigramPlus anuncia se a conversa está selecionada. Desmarcar a última conversa selecionada encerra o modo de seleção. Enquanto a lista de conversas está no modo de seleção, o UnigramPlus também diz "Seleccionado" antes do nome de uma conversa selecionada quando o foco chega a ela, como faz com as mensagens.
* Foi adicionado o Alt+Shift+M, que abre as configurações do Unigram no Unigram 13.1 e versões posteriores, como faz o UnigramPlusRussianMod. O Unigram 13.1 moveu as configurações do painel lateral para uma aba abaixo da lista de conversas. O Alt+Shift+M seleciona essa aba e depois move o foco para o início das configurações: para a primeira das suas outras contas ou, se você estiver conectado a apenas uma conta, para "Adicionar conta". Nas versões do Unigram anteriores à 13.1, e numa janela estreita que mostra apenas a conversa aberta, o UnigramPlus anuncia "Configurações indisponíveis".

### Versão 5.8.5

* Alt+M volta a abrir o menu de navegação no Unigram 13.1 e versões posteriores. O Unigram 13.1 substituiu o painel lateral por um menu que abre a partir do mesmo botão, e esse botão não é mais um botão de alternância, por isso o UnigramPlus não o encontrava e anunciava "Menu de navegação indisponível".
* Corrigido o Ctrl+Space no modo de seleção do Unigram. Nesse modo, o menu de contexto de uma mensagem selecionada não tem o comando Selecionar, por isso o UnigramPlus percorria o menu sem encontrá-lo e a mensagem continuava selecionada. Agora o Ctrl+Space funciona como no Unigram 13.1.1: a primeira vez que é pressionado ainda ativa o modo de seleção pelo menu de contexto e, depois disso, cada pressionamento seleciona ou desmarca a mensagem em foco, como a barra de espaço faz no Unigram. Em seguida, o UnigramPlus anuncia se a mensagem está selecionada. Desmarcar a última mensagem selecionada encerra o modo de seleção.
* No modo de seleção, a barra de espaço e Enter em uma mensagem agora a selecionam ou desmarcam, como no Unigram, em vez de reproduzir sua mídia ou procurar Responder no menu de contexto, e o Backspace não procura mais Editar lá.
* Atualizada a compatibilidade com o NVDA 2026.3. O UnigramPlus não usa mais partes obsoletas da API do NVDA, que o NVDA ainda suporta, mas pode remover em uma versão futura: as caixas de mensagem da verificação de atualizações, a forma antiga de abrir as configurações do UnigramPlus e uma constante de tecla usada ao avançar ou retroceder em mensagens de voz.
* Atualizadas as traduções polonesa e vietnamita.

### Versão 5.8.4

* Com a opção "Mover automaticamente o foco para a lista de conversas ao iniciar o Unigram" ativada, o foco agora permanece na janela pop-up que o Unigram mostra ao iniciar, como o pedido para entrar em um grupo aberto a partir de um link de convite. Desde a versão 5.6.1, o UnigramPlus movia o foco da janela pop-up para a lista de conversas atrás dela, e a janela pop-up acabava sendo ignorada.
* Atualizada a tradução vietnamita.

### Versão 5.8.3

* Removido o tratamento de Enter e espaço que o UnigramPlus adicionou à lista de categorias de configurações do Unigram na versão 4.8.0. No Unigram 13.0 e posteriores, cada categoria de configurações é um botão que se abre sozinho com Enter ou espaço, e o foco vai para esse botão, e não para o item de lista que o complemento tratava, por isso esse tratamento não tinha mais efeito ali. Agora, ao abrir uma categoria, o foco permanece nela, como no próprio Unigram, em vez de ser movido para dentro da categoria. Esse tratamento também afetava outras listas de abas, como as abas Emoji, GIFs e Figurinhas, onde interceptava Enter e espaço; agora essas teclas também chegam ao Unigram nesses locais.
* Nas configurações do Unigram, Alt+1 agora move o foco para a categoria de configurações aberta, ou para a primeira categoria se nenhuma estiver aberta. Antes, ele procurava a lista de categorias em uma posição fixa da página de configurações e depois tentava mover o foco para um elemento que não pode receber o foco no Unigram 13.0.
* Removido código que não podia mais ser executado, sem nenhuma mudança no uso. Antes do Unigram 9.5, alguns itens de lista eram anunciados por um nome de classe interno, que o UnigramPlus substituía por um nome legível; o Unigram 9.5 renomeou essas classes, então essas substituições nunca mais se aplicaram. Também foi removido o tratamento que abria a explicação de um quiz em uma janela separada, desativado desde a versão 5.2.0.
* Atualizadas as traduções polonesa e vietnamita.

### Versão 5.8.2

* Corrigidos erros do NVDA na nova versão beta do Unigram em WinUI 3. Desde a versão 5.5.6, um erro era registrado sempre que se voltava ao Unigram ou se digitava com um editor de método de entrada (IME), como os de chinês, japonês ou coreano. A versão UWP do Unigram não era afetada.
* O UnigramPlus não interfere mais nos anúncios de foco do Telegram Desktop quando o complemento Telegram Desktop não está instalado.
* Removida a notificação que o UnigramPlus dava ao cancelar a gravação de uma mensagem de voz ou de vídeo. O Unigram 13.0 e posteriores anunciam sozinhos uma gravação cancelada, seja com Ctrl+D ou com o botão de cancelar, então ela deixa de ser ouvida duas vezes. Uma gravação que demora a aparecer na conversa também não é mais anunciada como cancelada. O início e o envio de uma gravação continuam sendo anunciados, e a opção correspondente agora se chama "Notificação ao iniciar ou enviar a gravação de uma mensagem de voz".
* Atualizadas as traduções polonesa e vietnamita.

### Versão 5.8.1

* Removida a solução alternativa para a duração das chamadas. O Unigram 12.10 e posteriores anunciam sozinhos a duração de uma mensagem de chamada, então o UnigramPlus não a acrescenta mais e ela deixa de ser ouvida duas vezes.
* Corrigido o complemento não iniciar em versões antigas do NVDA que não fornecem o módulo utils.security.
* Removidas importações que o complemento não usa mais.
* Atualizada a tradução vietnamita.

### Versão 5.8.0

* As verificações periódicas em segundo plano do complemento não são mais executadas no laço principal do NVDA, então a navegação pelos chats, a digitação e a fala não ficam mais travadas enquanto o Unigram responde.
* Todos os comportamentos adicionados depois da versão 5.4 agora podem ser ativados ou desativados nas configurações do UnigramPlus, reunidos sob um único título: como o botão de gravar mensagem de voz é anunciado, o texto formatado das mensagens com ALT+C, o rótulo do botão de identidade do perfil, o anúncio de responder e editar no campo de mensagem, o anúncio suprimido de "lista" antes das mensagens, o estado ao vivo do microfone e da câmera durante uma chamada e a contagem de não lidas ao trocar de pasta de chats. Cada um mantém o comportamento atual por padrão, e cada rótulo informa qual comportamento da versão 5.4 ele restaura.
* Corrigida a barra de espaço não reproduzir mensagens de voz, músicas e arquivos.
* Corrigido o Enter não responder a uma mensagem, o Backspace não editá-la, o ALT+C não mostrar o texto dela e o ALT+D não voltar para ela.
* Corrigido o ALT+E não fechar o reprodutor de áudio.
* Corrigido o Ctrl+ALT+Esquerda e o Ctrl+ALT+Direita não avançarem nem retrocederem a reprodução da mensagem de voz, inclusive quando a seta é pressionada novamente com os modificadores ainda pressionados.
* O cancelamento de uma gravação de voz é anunciado cerca de um segundo e meio depois de ela parar, em vez de cinco segundos depois.
* Com a opção do botão de gravação da versão 5.4 selecionada, o foco permanece no campo de mensagem quando a gravação começa, enquanto o Tab continua alcançando o botão de gravar.
* Corrigidos vários atalhos que falhavam silenciosamente quando faltava na árvore do Unigram um elemento que eles esperavam encontrar: ALT+3, ALT+4, ALT+5, ALT+6, ALT+Q, ALT+T, ALT+Shift+L, ALT+Shift+P, Shift+Delete, a navegação por mídias e os controles de chamada.
* A conversão de uma mensagem de voz em texto não inicia mais uma thread nova a cada meio segundo enquanto espera, e desiste em vez de esperar para sempre.

### Versão 5.7.3

* NVDA+Alt+V agora mostra a versão do UnigramPlus em uma nova linha.

### Versão 5.7.2

* NVDA+Alt+V agora abre as informações de versão em uma janela somente leitura e com várias linhas.

### Versão 5.7.1

* Corrigido o tratamento dos botões de reação do Unigram 12.10.2 como mensagens, para que os atalhos de navegação entre mensagens não substituam mais sua ação nativa de alternância.

### Versão 5.7.0

* Foram restaurados os anúncios ao alternar pastas com uma contagem diferente de zero de não lidas, mantendo as proteções do rastreador de progresso de transferência de arquivos.
* A lista de atalhos foi atualizada a partir do código-fonte atual do Unigram e foram identificados os atalhos integrados que ainda não constam no Shortcuts.md oficial.

### Versão 5.6.9

* Corrigido um erro que poderia ocorrer quando o NVDA entrava em uma área de trabalho segura, como em um aviso do UAC, enquanto o rastreamento de mensagens em segundo plano do UnigramPlus estava ativado.
* Corrigido o tratamento de linhas de tópicos de Mensagens salvas no Unigram 12.10.1+ como mensagens apenas porque seus resumos nativos contêm horários de envio ou recebimento.
* Removida a solução alternativa obsoleta para nomes de tópicos de Mensagens salvas; as versões atuais do Unigram agora fornecem nativamente nomes acessíveis para conversas de Mensagens salvas.
* Atualizada a compatibilidade com o NVDA 2026.2.
* Atualizadas as traduções para polonês e birmanês.

### Versão 5.6.8

* Corrigida a falha do Alt+C quando o WhatsApp Enhancer está instalado, causada por uma colisão de nomes de módulos auxiliares em appModules.

### Versão 5.6.7

* O atalho para anunciar as versões instaladas do Unigram e do UnigramPlus foi alterado de NVDA+Shift+V para NVDA+Alt+V para evitar conflitos de atalhos.
* Corrigido Shift+Delete para excluir conversas e sair de grupos ou canais nas versões atuais do Unigram, incluindo a confirmação automática da janela pop-up.

### Versão 5.6.6

* Adicionado NVDA+Shift+V para anunciar as versões instaladas do Unigram e do UnigramPlus.
* Removida a solução temporária para os botões em linha do Unigram 12.9 após o Unigram 12.9.1 corrigir os rótulos dos botões; isso evita travamentos da UIA em listas de bots, navegação por mensagens, reações e na lista de conversas.
* Atualizadas todas as traduções e manuais para a versão 5.6.6.

### Versão 5.6.5

* Corrigido Enter para responder a mensagens e Alt+Shift+R para marcar conversas como lidas nas versões atuais do Unigram.
* Removidos o modo de visualização web e sua configuração; Alt+C agora sempre abre o texto da mensagem na janela pop-up wx original.
* Atualizadas todas as traduções e os manuais para a versão 5.6.5.

### Versão 5.6.4

* Corrigido Shift+Delete usando o comando Delete nativo do Unigram e confirmando automaticamente a exclusão para ambos os lados.
* Alt+2 agora ativa primeiro o botão “Ir para o fim” do Unigram; o atalho Alt+End duplicado foi removido.
* Adicionada uma configuração para escolher entre a janela wx clássica (padrão) e a visualização web ao exibir o texto da mensagem com Alt+C.
* Agora é usado o texto acessível oficial das mensagens avançadas do Unigram, com uma correção temporária para botões em linha sem rótulo no Unigram 12.9.
* A lista de atalhos foi atualizada conforme a documentação oficial do Unigram 12.9.
* Adicionada uma correção temporária para que as linhas de tópicos de Mensagens salvas anunciem o título visível da conversa em vez de um nome de tipo do TDLib.

### Versão 5.6.3

* Corrigido um problema intermitente em que o NVDA anunciava “lista” antes de uma mensagem ao navegar com as setas para cima e para baixo.
* Adicionada uma configuração para o comportamento do Alt+[ que anuncia os cabeçalhos das mensagens após seu conteúdo; ela vem desativada por padrão.
* Adicionada uma notificação sonora opcional ao chegar ao fim de uma conversa.

### Versão 5.6.2

* Corrigido o Ctrl+Alt+Left/Right Arrow para retroceder e avançar em uma mensagem de voz durante a reprodução.
* Corrigido o Alt+I para acessar a lista integrada de resultados da pesquisa no chat.
* Adicionado o Alt+[ para alternar o anúncio dos cabeçalhos antes ou depois do conteúdo da mensagem. Quando os cabeçalhos ficam depois do conteúdo, os nomes dos arquivos são anunciados primeiro nas seções de arquivos.

### Versão 5.6.1

* Corrigido o acompanhamento do progresso de transferência de arquivos para parar em 100% e não criar mais uma nova thread a cada ciclo de verificação.
* Ao abrir o Unigram, o foco agora é movido automaticamente para a lista de conversas.
* Adicionado Ctrl+Alt+Up/Down para percorrer conversas com menções não lidas.

### Versão 5.6.0

* Corrigida a detecção de mensagens avançadas para que mensagens com figurinhas e emojis não sejam mais anunciadas incorretamente como mensagens avançadas.
* Ctrl+R agora usa o comportamento nativo do Unigram para gravar e enviar mensagens de voz, mantendo as notificações de início e fim da gravação do UnigramPlus.
* Traduções atualizadas.

### Versão 5.5.9

* Adicionado suporte a mensagens avançadas. Elas são anunciadas quando recebem foco e podem ser abertas com Alt+C em uma janela navegável.
* Links e conteúdo misto são preservados, e os links podem ser ativados na janela navegável.

### Versão 5.5.8

* Corrigidas as atualizações automáticas: as versões agora são obtidas com segurança do GitHub e o complemento baixado é validado antes da instalação.

* Compatibilidade restaurada com o Unigram 12.7, onde vários atalhos e anúncios haviam parado de funcionar.
* As mensagens de enquete voltam a anunciar a pergunta e as opções de resposta.
* A lista de tópicos do fórum volta a anunciar a prévia da última mensagem.
* Durante uma chamada individual, os atalhos para silenciar o microfone (ALT+A), ativar ou desativar a câmera (ALT+V) e encerrar a chamada (ALT+N) voltam a funcionar.
* ALT+End volta a ir para a mensagem mais recente do bate-papo.

### Versão 5.5.7

* A seção de atalhos de teclado foi reorganizada em tabelas por categoria e agora combina os atalhos do Unigram e do UnigramPlus.
* Ao gravar uma mensagem de voz ou de vídeo, o NVDA agora anuncia "Gravando uma mensagem de voz" ou "Gravando uma mensagem de vídeo" junto com o tempo decorrido, em vez de "Tn voice message".

### Versão 5.5.6

* Corrigido o botão de identidade no perfil de um grupo ou canal que anunciava "Identity root" ao passar pelo nome com a tecla Tab; agora ele anuncia o nome da conversa e o número de membros.
* O Ctrl+C não é mais processado duas vezes: copia o link quando o foco está sobre um link e, nos demais casos, deixa o Unigram copiar a mensagem.

### Versão 5.5.5

* Responder ou editar uma mensagem agora é anunciado no campo de entrada de mensagem, em vez do prompt de mensagem habitual.
* Corrigido o som de digitação que às vezes continuava tocando após fechar o aplicativo, depois que a outra pessoa parava de digitar ou após sair do chat; agora ele para assim que ninguém está digitando no chat aberto.
* Atualizada a localização birmanesa.

### Versão 5.5.4

* Corrigidos anúncios indesejados, como contadores de chats não lidos em pastas, por exemplo "Todos 535". O progresso de transferência de arquivos agora fica limitado aos controles de envio e download do Unigram e é ignorado fora das janelas do Unigram.
* Corrigida a convivência com o complemento de NVDA para Telegram Desktop, ativando o UnigramPlus apenas quando o aplicativo em execução é detectado como Unigram.
* Adicionado um botão nas configurações do UnigramPlus para abrir a pasta de sons incluída, facilitando substituir arquivos WAV usando os mesmos nomes.
* Adicionada uma opção para a seta para cima no campo de edição de mensagem que move o foco para a última mensagem focada.
* O chinês tradicional foi recriado como zh_TW e o chinês simplificado foi adicionado como zh_CN.

### Versão 5.5.3

* Adicionado o anúncio automático do progresso de envio e download de arquivos. Uma nova opção "Apenas durante o envio e download" foi adicionada à configuração de anúncio das barras de progresso e agora é a opção padrão. O atalho ALT+U alterna agora entre três estados: desativado, apenas durante envio/download, e anunciar todas as barras de progresso.
* Atualização do readme e das traduções.

### Versão 5.5.2

* Atualização do readme e das traduções.
* Alterado o som do indicador de digitação.

### Versão 5.5.1

* Corrigido o atalho para navegar pela lista de tópicos do grupo (ALT+6). Agora detecta corretamente a lista de tópicos ao abrir um grupo de fórum a partir da lista de conversas.
* Adicionado som indicador de digitação: um som é reproduzido em loop enquanto o outro lado está digitando na conversa e para quando ele termina. Esta funcionalidade é inspirada na funcionalidade equivalente do script Unigram para JAWS.

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
