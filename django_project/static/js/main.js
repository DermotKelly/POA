// myapp/static/myapp/js/main.js
function changeHeroImage() {
    var heroImage = document.getElementById('heroImage');
    heroImage.src = "{% static 'images/portlaoise.jpg' %}";
}
