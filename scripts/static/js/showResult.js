window.addEventListener("DOMContentLoaded", function () {
    var container = document.querySelector('.container');
    var mydate = new Date();

    showResult();

    function showResult() {
        var image = document.createElement("img");
        var mytime = mydate.toLocaleTimeString();
        image.src = "/static/images/web_image.jpg?"+mytime;
        container.appendChild(image);
    }

}, false);
