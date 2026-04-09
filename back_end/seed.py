def seed_db():
    from back_end.database import db_session, engine
    from back_end.models import Base, Book, Author, Post, Launch, Recommendation, Article
    from datetime import datetime, timezone, timedelta

    Base.metadata.create_all(bind=engine)

    db_session.query(Book).delete()
    db_session.query(Author).delete()
    db_session.query(Post).delete()
    db_session.query(Launch).delete()
    db_session.query(Recommendation).delete()
    db_session.query(Article).delete()

    now = datetime.now(timezone.utc)

    livro1 = Book(
        title="Fragmentos de Mim",
        author="Gabrielle Côrrea",
        genre="Poesias",
        synopsis="O livro Fragmentos de Mim reúne poemas que registram as emoções e descobertas de uma jovem de quinze anos enquanto ela tenta entender a si mesma. Cada texto funciona como um retrato de seus conflitos, afetos e inseguranças, revelando o amadurecimento emocional típico da adolescência. É uma obra que busca conexão com o leitor ao revisitar experiências e sentimentos comuns a essa fase da vida.",
        price=24.99,
        cover="static/img/Fragmentos_de_Mim.jpg",
        link="https://www.amazon.com.br/Fragmentos-Mim-Poemas-menina-quinze-ebook/dp/B0F9YZYW2J/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2GZXCQZP7HIXH&dib=eyJ2IjoiMSJ9.C2nDNw4IqyFGk4xf-MUxxw.4kDo_5v3pToatPEX1NaLnDiNSf9PrWbJGmYktfBsKAY&dib_tag=se&keywords=fragmentos+de+mim+poemas+de+uma+menina+de+quinze+anos&qid=1751930379&sprefix=fragmentos+de+mim+poemas+de+uma+menina+de+quinze+anos%2Caps%2C185&sr=8-1",
        created_at=now - timedelta(hours=36)
    )

    livro2 = Book(
        title="Onde o Tempo faz a Curva",
        author="Thalita Monteiro",
        genre="Memórias",
        synopsis="Este livro revela, de forma franca, a trajetória de quem cresceu entre traumas, instabilidade emocional e a luta diária contra a depressão. Entre relatos de autodestruição, confusão interna e solidão, também surgem momentos de resistência: amizades que seguraram a dor, o apoio imperfeito da mãe e a escrita como refúgio quando nada mais fazia sentido. Não é uma história de superação idealizada, mas um testemunho real de quem já se sentiu quebrado, exausto e sem saída — e ainda assim encontrou pequenos motivos para continuar.",
        price=12.50,
        cover="static/img/Onde_o_Tempo_faz_a_Curva.jpg",
        link="https://www.amazon.com.br/Onde-Tempo-Curva-Thalita-Monteiro-ebook/dp/B0FDZ9DHQS/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2NGPKH5138FFE&dib=eyJ2IjoiMSJ9._RZdKZAd-ggoMF-Z0ONPxQ.rssaxnx5zK22jSir0mCkK_Ndz-DaSbC1CHIgAvZ7VUs&dib_tag=se&keywords=Onde+o+tempo+faz+a+curva&qid=1775266324&sprefix=onde+o+tempo+faz+a+curv%2Caps%2C207&sr=8-1",
        created_at=now - timedelta(hours=35)
    )

    livro3 = Book(
        title="Check-in Mental",
        author="Gabrielle Corrêa",
        genre="Transtornos",
        synopsis="Na Residência Psique, um refúgio voltado à saúde mental, hóspedes enfrentam seus traumas e emoções profundas sob o olhar sensível de Luna, a recepcionista que narra histórias de dor, superação e empatia. Um retrato humano sobre reconstrução interior e o poder de ouvir e ser ouvido.",
        price=24.99,
        cover="static/img/Check-in_Mental.jpg",
        link="https://www.amazon.com.br/Check-Mental-Cada-quarto-luta/dp/6598927609/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=184FXV4KXPHHX&dib=eyJ2IjoiMSJ9.K8VqxLGGGaNGswV_krLh1OVKJbBdg7w6pANXSGN8QnIiHN1LQLlSJDbDc3YjR1JpC-PditQWozMPLe9tZSQZv0c_VXomK_UtTVZGgNLTPEoJCzamcyP-XZiojZ3TqwcVK0UcMdbMepjn2tGuJlS9b5RwbzEypR3Jlm_EGo6ZJRRKY5WDiaoPDTMGJCuqh4hoBpg8CDY9fcj2aPdKKjZDUxG-uZzPoMphfxG-bb2fUjFtMa3Siygf6e6eU9C6ic66p3-rZF7TSP0LEKOayE-UL1JhgBWp4uNk1jMW8A3CzFU.dM_4HjLWym1_ErvuIWU51jYIb02tRaEB5-n8gWFlfZw&dib_tag=se&keywords=check-in+Mental&qid=1767725697&sprefix=check-in+mental%2Caps%2C209&sr=8-1&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9",
        created_at=now
    )

    autor1 = Author(
        name= 'Thalita Monteiro',
        avatar= 'static/img/avatar_thalita.jpeg',
        pet= 'static/img/Garfield_Solielle.png',
        width = 75,
        emoji= '🏵️',
        bio= 'O coração das palavras, que vive a escrita intensamente, trazendo emoção, drama e paixão pela literatura.<br><br> Ama escrever, se emociona com histórias e, na Solielle, cuida dos textos com carinho e respeito, para que as palavras cheguem a quem precisa lê-las.',
        account= '@zthaliii',
        link = 'https://www.instagram.com/zthaliii/?hl=pt-br',
        created_at=now - timedelta(hours=34)
    )

    autor2 = Author(
        name= 'Gabrielle Côrrea',
        avatar= 'static/img/avatar_bibi.jpeg',
        pet= 'static/img/Snoopy_Solielle.png',
        width = 88,
        emoji= '🌸',
        bio= 'A criativa sensível que transforma sentimentos em imagens e formas com doçura e olhar artístico.<br><br> Ama criar em traços e palavras, encontrou na arte um refúgio e um jeito de dar voz ao que sente. Na Solielle, transforma emoções em criações que acolhem e inspiram.',
        account= '@bibi_gbmc',
        link = 'https://www.instagram.com/bibi_gbmc/?hl=pt-br',
        created_at=now - timedelta(hours=33)
    )

    autor3 = Author(
        name= 'Sofia Mendes',
        avatar= 'static/img/avatar_sofia.jpeg',
        pet= 'static/img/Pooh_Solielle.png',
        width = 65,
        emoji= '🌻',
        bio= 'A mente inquieta e comunicativa, cheia de ideias e estratégias para levar histórias mais longe.<br><br> Ama desenhar e escrever, encontrou na criação uma forma de se expressar e se sentir em paz. Cuida das palavras e ideias para que transmitam verdade e acolhimento.',
        account= '@soffi_mgs',
        link = 'https://www.instagram.com/soffi_mgs/?hl=pt-br',
        created_at=now - timedelta(hours=32)
    )

    post1 = Post(
        title='Lançamentos do mês', excerpt='Confira os livros que chegam às prateleiras este mês.', cover='static/img/lançamentos.png', created_at=now - timedelta(hours=31)
    )

    post2 = Post(
        title='Listas e recomendações dos autores', excerpt= '“3 motivos para continuar escrevendo”, “Como criar personagem marcante?”...', cover='static/img/recomendações.png', created_at=now - timedelta(hours=30)
    )

    post3 = Post(
        title='Artigos que inspiram os autores', excerpt='Confira as reflexões, curiosidades e textos curtos que estimulam os autores.', cover='static/img/artigos.png', created_at=now - timedelta(hours=29)
    )

    launch1 = Launch(
        title='A Casa Onde Dormem as Mulheres', 
        author='Thalita Monteiro', 
        genre='Realismo Social • Feminilidade', 
        cover='static/img/a_Casa_Onde_Dormem_as_Mulheres.jpg',
        bio= "Em A Casa Onde Dormem as Mulheres, vítimas de violências e perdas encontram refúgio para curar suas feridas e reencontrar a própria voz. A obra é um relato poético sobre dor, resistência, perdão e renascimento feminino.",
        created_at=now - timedelta(hours=28)
    )

    recommendation1 = Recommendation(
        title="3 erros comuns na auto diagramação",
        text="1️⃣ Ignorar os erros de repetição de palavras.<br><strong>ex: A personagem olhou... olhou... e continuou olhando...</strong><br>Às vezes, as palavras insistem em voltar — e isso não é um erro. A repetição pode carregar hesitação, emoção ou intensidade. O problema nasce quando ela perde o sentido e se torna apenas eco vazio.<br>Então, a dica é: <strong>não apague toda repetição: escute o que ela quer dizer.</strong> Se houver intenção, é estilo. Se não, é ruído.<br><br>2️⃣ Não prestar atenção no ritmo da leitura<br><strong>Frases longas demais... que perdem o fôlego... e cansam o leitor</strong><br>Quando o texto se alonga demais, o fôlego se perde. O ritmo é a respiração da escrita — é ele que guia, embala e dá vida às palavras.<br>Entre pausas e batidas, o bom escritor encontra o compasso certo: frases que dançam, não tropeçam.<br><strong>Revisar o ritmo é cuidar do pulso do texto.</strong><br><br>3️⃣ Confiar demais no corretor automático<br><strong>Porque 'concerteza' só parece certo até você reler com calma.</strong><br>O corretor automático é útil, mas não infalível. Ele enxerga letras, não intenções. Corrige a forma, mas ignora o sentido.<br>Palavras erradas podem escapar disfarçadas de acerto. Só o olhar humano percebe o que soa estranho, o que falta ou sobra.<br><strong>Revisar com atenção é ouvir o texto</strong> — algo que nenhuma máquina consegue fazer.",
        created_at=now - timedelta(hours=27)
    )

    recommendation2 = Recommendation(
        title="5 dicas de escrita para iniciantes",
        text="1️⃣ Escreva com frequência<br><strong>Porque a escrita é como um músculo: quanto mais você pratica, mais forte ela fica.</strong><br>Não espere o momento ideal ou o cenário perfeito — escreva no ônibus, no intervalo, à noite, quando der. Cada texto é um passo na tua evolução. Mesmo que pareça simples ou ruim, é prática. E prática vira voz.<br><strong>Escrever sempre é o caminho para descobrir o seu próprio estilo.</strong><br><br>2️⃣ Leia bastante<br><strong>Ler é o alimento da escrita.</strong><br>Quem lê, respira ritmo, aprende cadência e reconhece o que funciona — e o que não. Ler amplia o olhar e te ensina, sem perceber, como palavras podem tocar, mover e construir mundos.<br><strong>Quanto mais você lê, mais referências carrega na alma da sua escrita.</strong><br><br>3️⃣ Não espere pela ideia perfeita<br><strong>A perfeição é o maior inimigo do começo.</strong><br>Não existe ideia pronta, existe vontade de começar. O texto nasce imperfeito — e é justamente no processo que ele se lapida. Deixe vir o que tem agora, porque o resto se revela escrevendo.<br><strong>Ideias boas nascem do movimento, não da espera.</strong><br><br>4️⃣ Mostre, não conte<br><strong>Em vez de dizer que o personagem estava triste, mostre-o segurando as lágrimas.</strong><br>Escrever é criar imagens, não relatórios. Faça o leitor sentir o que o personagem sente, ver o que ele vê. É na sugestão, e não na explicação, que mora a força da narrativa.<br><strong>Mostre com gestos, silêncios e detalhes — é assim que o texto ganha vida.</strong><br><br>5️⃣ Escreva o que você sente<br><strong>Porque emoção verdadeira atravessa a página.</strong><br>O leitor reconhece quando o texto vem de um lugar honesto. Não escreva para impressionar — escreva para expressar. O que você sente é matéria-prima poderosa, e é ela que torna sua escrita única.<br><strong>Palavras sinceras sempre encontram quem as entenda.</strong>",
        created_at=now - timedelta(hours=26)
    )

    recommendation3 = Recommendation(
        title="Como criar um personagem marcante",
        text="1️⃣ Dê um traço único<br><strong>Algo pequeno, mas inesquecível.</strong><br>Um hábito, uma mania, uma forma de falar — detalhes que fazem o leitor reconhecer o personagem de longe. Às vezes, é um gesto; outras, uma frase que só ele diria.<br><strong>É no detalhe que nasce a identidade.</strong><br><br>2️⃣ Crie uma contradição<br><strong>Porque ninguém é feito de uma coisa só.</strong><br>Um personagem marcante guarda conflitos dentro de si: força e fragilidade, coragem e medo, bondade e impulsos sombrios. São essas fissuras que o tornam humano.<br><strong>Contradições dão profundidade e verdade.</strong><br><br>3️⃣ Conheça o que ela teme e deseja<br><strong>Todo personagem vive entre dois polos: aquilo que persegue e aquilo que foge.</strong><br>Desejo é motor. Medo é limite. Quando você sabe os dois, sabe também como ela age, erra, cresce e se transforma.<br><strong>É o eixo emocional de qualquer história.</strong><br><br>4️⃣ Dê a ela uma memória<br><strong>Uma lembrança capaz de doer ou aquecer.</strong><br>Memórias moldam atitudes — uma perda, uma promessa, um cheiro de infância. Quando o leitor conhece essa marca, entende a alma do personagem.<br><strong>Memória é ferida e bússola ao mesmo tempo.</strong><br><br>5️⃣ Deixe que ela surpreenda você<br><strong>Se tudo que o personagem faz é previsível, ele está morto.</strong><br>Escreva até o momento em que ela toma decisões que você não planejou, porque personagens vivos têm vontade própria. Eles respiram, reagem, escapam do roteiro.<br><strong>Personagens marcantes são aqueles que se rebelam nas suas mãos.</strong>",
        created_at=now - timedelta(hours=25)
    )

    recommendation4 = Recommendation(
        title="Processo de preparação de um texto para publicação",
        text="1️⃣ A Revisão<br><strong>O cuidado com a forma.</strong><br>É aqui que o texto passa pelo pente-fino linguístico: acentuação, concordância, ortografia, repetição, digitação, pontuação. A revisão garante que tudo esteja dentro da norma culta e compreensível.<br>Ela não mexe no estilo nem no conteúdo, apenas limpa as falhas que escapam ao autor.<br><strong>🔍 Exemplo:</strong> corrigir “foi os meninos” para “foram os meninos”.<br><br>2️⃣ A Leitura Crítica<br><strong>O olhar que mergulha no conteúdo.</strong><br>Analisa estrutura, coesão, clareza, desenvolvimento de ideias e consistência dos personagens. Aqui nascem sugestões de cortes, acréscimos, mudanças de ordem, ajustes de enredo.<br>A leitura crítica não altera diretamente o texto — ela guia o autor com um diagnóstico profundo.<br><strong>🔍 Exemplo:</strong> apontar que o final de um romance está apressado e precisa respirar mais.<br><br>3️⃣ O Copydesk<br><strong>O refinamento da voz.</strong><br>Vai além da revisão: reescreve trechos para torná-los mais claros, fluidos e adequados ao estilo da publicação. Ajusta escolhas de palavras, uniformiza termos e eleva a comunicação sem alterar o conteúdo essencial.<br>É o processo que dá polimento e acabamento ao texto.<br><strong>🔍 Exemplo:</strong> transformar “ele fez um monte de coisas legais” em “ele realizou diversas atividades interessantes”, mantendo o sentido, mas aprimorando a linguagem.",
        created_at=now - timedelta(hours=24)
    )

    recommendation5 = Recommendation(
        title="Dicas para destravar a escrita",
        text="1️⃣ Observe o mundo como se fosse um cenário<br><strong>O cotidiano esconde histórias — basta abrir o olhar.</strong><br>Quando estou no carro, costumo observar tudo ao redor e imaginar detalhes que poderiam existir em uma narrativa. Perguntas simples despertam possibilidades: “E se aquela casa velha escondesse algo?” ou “Aquele homem pichando a calçada… o que será que ele quer dizer com isso?”.<br>Quando você passa a enxergar o mundo não só como ele é, mas como ele poderia ser, sua imaginação começa a trabalhar. Personagens, conflitos e mistérios surgem onde antes havia rotina.<br><strong>Treinar esse olhar amplia a percepção e torna a mente mais criativa.</strong><br><br>2️⃣ Brinque com palavras novas<br><strong>Cada palavra desconhecida pode ser uma porta para novas ideias.</strong><br>Em vez de apenas buscar o significado, tente encaixar a palavra em diferentes frases: num poema, numa discussão, num bilhete. Esse pequeno jogo faz você sentir a sonoridade, o tom e a intenção por trás dela.<br>A palavra deixa de ser apenas um termo solto e passa a fazer parte do seu vocabulário de verdade. Quanto mais você experimenta, mais natural se torna usá-la no dia a dia — e sua escrita cresce junto.<br><strong>Explorar palavras é expandir horizontes.</strong><br><br>3️⃣ A escrita começa na curiosidade<br><strong>Mesmo sem escrever nada, você já está criando.</strong><br>Cada detalhe que chama sua atenção — um gesto, uma conversa, uma casa diferente, uma palavra nova — vira matéria-prima para sua imaginação. Antes de ser texto, a escrita é observação. Antes de virar história, ela é pergunta.<br><strong>É nesse olhar curioso, quase brincalhão, que a escrita nasce.</strong>",
        created_at=now - timedelta(hours=23)
    )

    recommendation6 = Recommendation(
        title="3 plataformas úteis para escritores",
        text="1️⃣ LanguageTool<br><strong>Seu aliado para revisar com segurança.</strong><br>Um corretor gramatical inteligente que aponta erros de ortografia, pontuação e até estilo. Ideal para quem quer entregar textos mais limpos e corretos.<br><strong>Dica extra:</strong> você pode usar direto no navegador ou instalar a extensão para revisar automaticamente.<br><br>2️⃣ Inkarnate<br><strong>Mapas que dão vida às suas histórias.</strong><br>Com ele, você cria mapas incríveis para fantasia, ficção ou RPG — reinos inteiros com visual profissional. Ótimo para quem trabalha com worldbuilding.<br><strong>Dica:</strong> a versão gratuita já oferece muitas ferramentas úteis.<br><br>3️⃣ World Anvil<br><strong>Organize seu universo fictício como um mestre.</strong><br>Uma plataforma completa para guardar personagens, reinos, cronologias, sistemas de magia e tudo que compõe seu mundo. Para escritores de fantasia e ficção científica, é ouro puro.<br><strong>Dica:</strong> funciona como um “Notion” voltado para mundos imaginários.<br><br><strong>“Todos somos aprendizes em um ofício onde ninguém jamais se torna mestre.” – Ernest Hemingway</strong><br><br>Uma lembrança poderosa de que a escrita é um caminho infinito. Não importa o quanto você evolua, sempre haverá algo novo para aprender, experimentar e descobrir.<br><strong>Escritores crescem porque permanecem curiosos.</strong>",
        created_at=now - timedelta(hours=22)
    )

    recommendation7 = Recommendation(
        title="Como criar o hábito de leitura",
        text="1️⃣ Comece com 10 minutos por dia<br><strong>Porque ler pouco é melhor do que não ler — e é assim que o hábito nasce.</strong><br>Não precisa começar com capítulos longos ou metas rígidas. Dez minutos já ensinam o cérebro a entrar no ritmo sem pressão. Com o tempo, esses 10 viram 15, 20, 30… naturalmente.<strong>O importante não é a quantidade, é a constância.</strong><br><br>2️⃣ Escolha temas que você realmente gosta<br><strong>A leitura só vira hábito quando vira prazer.</strong><br>Esqueça a obrigação de ler clássicos ou livros que outros consideram “melhores”. Comece por aquilo que conversa contigo: fantasia, romance, terror, mistério, poesia, desenvolvimento pessoal…<strong>Quando você lê pelo desejo, o cérebro volta sozinho para o livro.</strong><br><br>3️⃣ Tenha um livro sempre por perto<br><strong>Conveniente = constante.</strong><br>Se o livro está longe, você adia. Se está por perto, você lê. Deixe um no criado-mudo, outro na mochila, salve um e-book no celular para momentos vazios — fila, ônibus, intervalo.<strong>Facilitar o acesso transforma leitura em hábito diário.</strong><br><br>4️⃣ Crie um momento de leitura<br><strong>Rituais transformam ações em hábitos.</strong><br>Escolha um horário: antes de dormir, durante o café, no transporte, no intervalo da escola ou do trabalho. Aos poucos, o cérebro entende que aquele é “o momento de ler”.<strong>Quando vira ritual, não depende mais de motivação — vira parte de você.</strong><br><br>5️⃣ Desconecte um pouco<br><strong>Trocar 10 minutos de redes por leitura já muda tudo.</strong><br>Esse tempo pequeno se acumula: em uma semana, quase duas horas; em um mês, um livro inteiro. E a leitura oferece o que as redes não oferecem: foco, calma e profundidade.<strong>Você não precisa de mais tempo — só de um pouco menos de distração.</strong><br><br><strong>Lembre-se:</strong><br>A leitura é construída, não herdada. Quanto mais você lê, mais natural — e transformadora — ela se torna.",
        created_at=now - timedelta(hours=21)
    )

    recommendation8 = Recommendation(
        title="Quais são e como funcionam os serviços da empresa?",
        text="1️⃣ Diagramação<br><strong>Organizamos o conteúdo do seu livro para ficar bonito e fácil de ler.</strong><br>Escolhemos fontes que combinam com a proposta da obra e cuidamos de margens, espaçamento e alinhamento para dar conforto na leitura. Também estruturamos páginas, cabeçalhos e sumário de forma clara e funcional.<strong>No final, o livro fica com um visual profissional e com a sua identidade.</strong><br><br>2️⃣ Capa<br><strong>Criamos capas que chamam atenção e representam bem a história.</strong><br>Fazemos capa completa para livro físico (frente, lombada e verso) e também para e-book. O design é personalizado: escolhemos tipografia, cores e composição de acordo com o gênero e a proposta do livro. Podemos incluir ilustrações ou editar imagens conforme o briefing.<strong>Você recebe tudo pronto para publicar ou imprimir.</strong><br><br><strong>Diferencial:</strong><br>Cada capa é pensada com cuidado, equilibrando estética e significado.<br><br><strong>Prazo:</strong><br>De 7 a 15 dias úteis (depende da complexidade).<br><br>3️⃣ Divulgação<br><strong>Ajudamos seu livro a chegar nas pessoas certas.</strong><br>Criamos teasers, sinopses e materiais de divulgação para antes, durante e depois do lançamento. Também planejamos estratégias de engajamento (como sorteios, reels e interações) e podemos apoiar parcerias com influenciadores literários.<strong>Tudo é feito de forma personalizada, sem fórmulas prontas.</strong><br><br><strong>Diferencial:</strong><br>Divulgação feita com cuidado real, pensando no leitor e não só em números.<br><br>4️⃣ Contato<br><strong>Fale com a gente de forma simples.</strong><br>Se quiser orçamento, tirar dúvidas ou conversar sobre seu projeto, é só chamar. Pode mandar direct ou e-mail.<br><strong>Estamos disponíveis para te ajudar.</strong>",
        created_at=now - timedelta(hours=20)
    )

    article1 = Article(
        img="static/img/artigo1.png",
        caption="Para alguns, é só um caderno e uma caneta. Para outros, é o único jeito de manter a sanidade. 🖋✨",
        created_at=now - timedelta(hours=19)
    )

    article2 = Article(
        img="static/img/artigo2.png",
        caption="Nem toda escrita precisa de aplausos. Às vezes, é só a alma pedindo para respirar entre as linhas. 📝💛",
        created_at=now - timedelta(hours=18)
    )

    article3 = Article(
        img="static/img/artigo3.png",
        caption="✨ Quantas vezes você já imaginou segurar sua própria história impressa? Sentir o peso dos seus personagens, das suas palavras, do seu sonho realizado?",
        created_at=now - timedelta(hours=17)
    )

    article4 = Article(
        img="static/img/artigo4.png",
        caption="📝✨ Quando o coração fala mais alto que a razão… Essa é uma das declarações mais intensas da literatura, capaz de tocar até os sentimentos mais adormecidos 💛",
        created_at=now - timedelta(hours=16)
    )

    article5 = Article(
        img="static/img/artigo5.png",
        caption="Algumas perdas podem ser encontradas no tempo certo, outras, jamais deveriam ter sido deixadas para trás. Uma lembrança de sabedoria direto da Terra Média com Gandalf, o Cinzento. ✨",
        created_at=now - timedelta(hours=15)
    )

    article6 = Article(
        img="static/img/artigo6.png",
        caption="📚 Da nossa editora pra você, que escreve, sente, sonha e segue mesmo com frio na barriga. O show é seu. 💫",
        created_at=now - timedelta(hours=14)
    )

    article7 = Article(
        img="static/img/artigo7.png",
        caption="📚✨ A leitura é um refúgio, um encontro consigo mesmo e com o mundo. Infelizmente, nem todos descobrem esse prazer — mas quem descobre, nunca mais vive sem. 💛",
        created_at=now - timedelta(hours=13)
    )

    article8 = Article(
        img="static/img/artigo8.png",
        caption="💛 Setembro Amarelo também é momento de ler.",
        created_at=now - timedelta(hours=12)
    )

    article9 = Article(
        img="static/img/artigo9.png",
        caption="⏳✨ Cada etapa importa, cada pausa também faz parte. Respeitar o processo é acreditar que o tempo trabalha a nosso favor. 🌻",
        created_at=now - timedelta(hours=11)
    )

    article10 = Article(
        img="static/img/artigo10.png",
        caption="Todo autor já começou com um rascunho duvidoso, um texto no bloco de notas ou um sonho guardado no peito. Aqui, a gente acredita em vozes novas.",
        created_at=now - timedelta(hours=10)
    )

    article11 = Article(
        img="static/img/artigo11.png",
        caption="Leitura da semana: A Menina que Roubava Livros 💛 Um lembrete de que as palavras podem mudar destinos.",
        created_at=now - timedelta(hours=9)
    )

    article12 = Article(
        img="static/img/artigo12.png",
        caption="Porque toda boa história merece conforto, café, marcações coloridas e aquele clima aconchegante que só quem ama ler entende. 📚☕",
        created_at=now - timedelta(hours=8)
    )

    article13 = Article(
        img="static/img/artigo13.png",
        caption="No íntimo dos pequenos esforços diários, o sucesso deixa de ser destino e passa a ser construção. 💛🧠",
        created_at=now - timedelta(hours=7)
    )

    article14 = Article(
        img="static/img/artigo14.png",
        caption="A força da escrita floresce no íntimo. Somos feitos de silêncio, de sombra e de palavras que resistem ao caos que nos confina.",
        created_at=now - timedelta(hours=6)
    )

    article15 = Article(
        img="static/img/artigo15.png",
        caption="“Entre gestos simples e sabores que aquecem, o Natal lembra que o amor cabe nos detalhes. Que a leveza nos encontre — e que a gente saiba levar consigo o que realmente importa.”🎄💛",
        created_at=now - timedelta(hours=5)
    )

    article16 = Article(
        img="static/img/artigo16.jpeg",
        caption="📖✨ Na Solielle, acreditamos no poder das palavras para transformar finais — e vidas. ✍️ C. S. Lewis",
        created_at=now - timedelta(hours=4)
    )

    article17 = Article(
        img="static/img/artigo17.png",
        caption="✨ Na literatura, não há pressa. Cada voz tem seu tempo, cada palavra seu brilho. Na Solielle, acreditamos em histórias autênticas — exatamente como quem as escreve. 📚🌿",
        created_at=now - timedelta(hours=3)
    )

    article18 = Article(
        img="static/img/artigo18.png",
        caption="Essa frase faz parte do livro Fragmentos de Mim, da jovem autora Gabrielle Corrêa, uma obra sensível que transforma sentimentos e vivências da adolescência em poesia. 📖",
        created_at=now - timedelta(hours=2)
    )

    article19 = Article(
        img="static/img/artigo19.png",
        caption="Resiliência é a força silenciosa que nos faz recomeçar, mesmo quando tudo parece difícil. 🌿✨ É cair, aprender, se reconstruir… e ainda florescer mais forte.",
        created_at=now - timedelta(hours=1)
    )

    db_session.add_all([livro1, livro2, livro3])
    db_session.add_all([autor1, autor2, autor3])
    db_session.add_all([post1, post2, post3])
    db_session.add_all([launch1])
    db_session.add_all([recommendation1, recommendation2, recommendation3, recommendation4, recommendation5, recommendation6, recommendation7, recommendation8])
    db_session.add_all([article1, article2, article3, article4, article5, article6, article7, article8, article9, article10, article11, article12, article13, article14, article15, article16, article17, article18, article19])
    db_session.commit()

    print("Banco populado! 👍")