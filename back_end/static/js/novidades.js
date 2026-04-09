async function checkNews() {
    const res = await fetch('/api/novidades');
    const data = await res.json();

    if (!data.length) return;

    const moreRecent = data[0]; // agora funciona corretamente

    const lastVisit = localStorage.getItem("ultimaVisita");

    if (!lastVisit || lastVisit !== moreRecent.data) {
        const btn = document.getElementById('btn-novidades');

        btn.style.display = 'block';

        localStorage.setItem('tipoNovidade', moreRecent.tipo);

        if (moreRecent.tipo === "book") {
            btn.innerText = "📚 Novo livro disponível!";
        } else if (moreRecent.tipo === "article") {
            btn.innerText = "📰 Novo artigo!";
        } else {
            btn.innerText = "✨ Novidades!";
        }
    }
}

function toNews() {
    const type = localStorage.getItem('tipoNovidade');

    let id = '';

    if (type === 'book') id = 'catalog';
    if (type === 'author') id = 'authors';

    if (
        type === 'post' ||
        type === 'launch' ||
        type === 'recommendation' ||
        type === 'article'
    ) {
        id = 'blog';
    }

    if (id) {
        document.getElementById(id).scrollIntoView({
            behavior: 'smooth'
        });
    }

    // salva a última novidade vista
    fetch('/api/novidades')
        .then(res => res.json())
        .then(data => {
            if (data.length) {
                localStorage.setItem('ultimaVisita', data[0].data);
            }
        });

    document.getElementById('btn-novidades').style.display = 'none';
}

window.onload = checkNews;  