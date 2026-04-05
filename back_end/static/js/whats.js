// document.getElementById('contactForm').addEventListener('submit', async (e) => {
//     e.preventDefault();

//     const formData = new FormData(e.target);
//     const response = await fetch('/send_email', {
//         method: 'POST',
//         body: formData
//     });

//     const result = await response.text();
//     document.getElementById('response').innerHTML = result;
// })

// function sendWhats(title, price) {
//   const phone = 5511948573463;

//   const formattedPrice = parseFloat(price).toFixed(2).replace('.', ',');

//   const text = `Olá! Me chamo (seu nome).\nVim pelo site da *Solielle* e gostaria de comprar o livro *${title}* por R$${formattedPrice}.\nPoderia me ajudar com a compra?`;

//   const msgFormated = encodeURIComponent(text);
//   const url = `https://wa.me/${phone}/?text=${msgFormated}`;
  
//   window.open(url, '_blank');
// }


function finalizePurchase() {
  if (cart.length === 0) {
    alert("Seu carrinho está vazio! Adicione algum livro antes de finalizar a compra 🌸");
    return;
  }

  const phone = 5511948573463;

  // total real
  const total = cart.reduce((sum, b) => sum + b.price * b.quantity, 0);
  const totalFormatted = total.toFixed(2).replace('.', ',');

  // lista de itens com quantidades
  const bookList = cart
    .map(b => `*${b.title}* — ${b.quantity}x — R$${(b.price * b.quantity).toFixed(2).replace('.', ',')}`)
    .join('\n');

  const text = 
  `Olá! Me chamo (seu nome) e vim pelo site da *Solielle*.

Gostaria de finalizar minha compra com os seguintes livros:

${bookList}

*Total:* R$${totalFormatted}

Poderiam me ajudar com o pagamento e envio?`;

  const msgFormated = encodeURIComponent(text);
  const link = `https://wa.me/${phone}?text=${msgFormated}`;
  window.open(link, '_blank');
}
