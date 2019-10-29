const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setInterval(function () {
    $('#message').fadeOut();
},3000);
