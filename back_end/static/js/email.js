(function(){
    emailjs.init("6huNoMAGZ9sUHeLg0")
})();

function sendEmail(e) {
    e.preventDefault();

    const params = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    emailjs.send("service_1uz6asx", "template_w8zfxh2", params)
    .then(function(response) {
        alert("Mensagem enviada com sucesso! 💌")
    }, function(error) {
        alert("Erro ao enviar. Tente novamente.")
        console.log(error)
    }); 
}   