window.addEventListener("DOMContentLoaded", function () {
    try { 
        document.createElement("canvas").getContext("2d"); 
    } catch (e) {
        alert("not support canvas!") 
    }

    var canvas = document.getElementById("canvas"),
        context = canvas.getContext("2d");
    var mydate = new Date();

    showResult();

    function showResult() {
        var image = document.createElement("img");
        var mytime = mydate.toLocaleTimeString();
        image.src = "/static/images/web_image.jpg?"+mytime;
        // container.appendChild(image);
        image.onload = function() {
            var width = image.width;
            var height = image.height;
            canvas.width = image.width;
            canvas.height = image.height;
            context.drawImage(image, 0, 0, image.width, image.height)
        }
    }

}, false);
