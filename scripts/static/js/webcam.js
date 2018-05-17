window.addEventListener("DOMContentLoaded", function () {
    try { 
        document.createElement("canvas").getContext("2d"); 
    } catch (e) {
        alert("not support canvas!") 
    }

    var video = document.getElementById("video"),
        canvas = document.getElementById("canvas"),
        context = canvas.getContext("2d");
        navigator.getUserMedia = navigator.getUserMedia || 
                                 navigator.webkitGetUserMedia || 
                                 navigator.mozGetUserMedia || 
                                 navigator.msGetUserMedia;

    if (navigator.getUserMedia) {
        navigator.getUserMedia(
            { "video": true },
            function (stream) {
                if (video.mozSrcObject !== undefined) video.mozSrcObject = stream;
                else video.src = ((window.URL || window.webkitURL || window.mozURL || window.msURL) && window.URL.createObjectURL(stream)) || stream;
                video.play();
                // var promise = document.querySelector('video').play();
                // if (promise !== undefined) {
                //     video.play();
                // }
            },
            function (error) {
                alert("Video capture error: " + error.code);
            }
        );
    } else {
        alert("Native device media streaming (getUserMedia) not supported in this browser");
    }

    $('#snap').on('click', function () {
        context.drawImage(video, 0, 0, canvas.width = video.videoWidth, canvas.height = video.videoHeight);
        $.post('/upload', { "img": canvas.toDataURL().substr(22) }, function (data, status) {
            alert(status!="success"?"process erroe":data== "yes"?"upload complete":data);
        }, "text");
    });
}, false);
