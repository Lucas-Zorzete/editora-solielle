async function checkNews() {
    const res = await fetch('/api/novidades');
    const data = await res.json();

    const moreRecent = data[0];

    const lastVisit = localStorage.getItem("ultimaVisita");

    if (!lastVisit || new Date(lastVisit) < new Date(moreRecent.data)) {
        document.getElementById('btn-novidades').style.display = 'block';

        // guarda o tipo para se localizar
        localStorage.setItem('tipoNovidade', moreRecent.tipo);
    }
}

function toNews() {
    const type = localStorage.getItem('tipoNovidade');

    let id = '';

    if (type === 'book') id = 'catalog';
    if (type === 'author') id = 'authors';
    if (type === 'post') id = 'posts';
    if (type === 'launch') id = 'blog';
    if (type === 'recommendation') id = 'blog';
    if (type === 'article') id = 'blog';

    document.getElementById(id).scrollIntoView({
        behavior: 'smooth'
    });

    localStorage.setItem('ultimaVisita', new Date().toISOString());
    
    document.getElementById('btn-novidades').style.display = 'none';
}