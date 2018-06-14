window.addEventListener("DOMContentLoaded", function () {
    try { 
        document.createElement("canvas").getContext("2d"); 
    } catch (e) {
        alert("not support canvas!") 
    }

    var canvas = document.getElementById("canvas"),
        context = canvas.getContext("2d");

    var browse = document.getElementById('browse');
    browse.addEventListener('change',imgBrowse,false);

    $('#local').on('click', function () {
        $.post('/upload', { "img": canvas.toDataURL().substr(22) }, function (data, status) {
            // alert(status!="success"?"process erroe":data== "yes"?"upload complete":data);
            window.location.href="/result";
        }, "text");
    });

    function imgBrowse() {
        var browse = document.getElementById("browse");
        var file = browse.files[0];//获取input输入的图片
        if (!/image\/\w+/.test(file.type)) {
            alert("请确保文件为图像类型");
            return false;
        }//判断是否图片，在移动端由于浏览器对调用file类型处理不同，虽然加了accept = 'image/*'，但是还要再次判断
        var reader = new FileReader();
        reader.readAsDataURL(file);//转化成base64数据类型
        reader.onload = function (e) {
            drawToCanvas(e.target.result);
        }
    }

    function drawToCanvas(imgData) {
        var img = new Image;
        img.src = imgData;
        img.onload = function () {//必须onload之后再画
            var width = img.width;
            var height = img.height;
            canvas.width = img.width;
            canvas.height = img.height;
            context.drawImage(img, 0, 0, img.width, img.height);
            strDataURI = canvas.toDataURL();//获取canvas base64数据
        }
    }
}, false);
