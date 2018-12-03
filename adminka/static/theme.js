$('document').ready(function() {
        loadTheme();
        
});
var url = document.URL + 'static/json/data.json';
        console.log(url)
var lastData = '';
function loadTheme() { 
    
    $.getJSON(url, function(data) {
        console.log(data);
        if(data.theme == 1) {
            themeOne(data);
            lastData = data.theme;
        }else if(data.theme == 2) {
            themeSecond(data);
            lastData = data.theme;
        }else if(data.theme == 3) {
            themeThird();
            lastData = data.theme;
        }

        /*setInterval(function(){
            $.getJSON('http://test/static/json/data.json', function(data) {
                console.log("+")
                if(data.theme !== lastData){
                    loadTheme();
                }
            })
        }, 1000);*/
    })

}

function themeOne(data) {
    var header = "";
    var content = "";
    header += "<header class='header1'><div class='head-left-item'>";
    header +="<img src='static/img/logo.png' alt='logo'><div><h3>НҰР ОТАН</h3>"
    header +="<p>ПАРТИЯСЫ САЙЛАУАЛДЫ<br>БАҒДАРЛАМАСЫ</p></div></div>";
    header += "<div class='head-right-item'><div class='arrows'>";
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/right-arrow.png' alt='right-arrow'></div>";
    header += "<div class='menu-buttons'><button>Главная</button><button class='active'>Информационный блок</button></div></div></header>";

    content += "<div class='wrapper'><div class='container'><ul>";
    content += "<li class='card test1'>";
    content += "<img src=" + data.img1 + " alt='image'><div class='info '><h2>" + data.title1 + "</h2>";
    content += "<p>" + data.text1 + "</p></div></li>"; 
    content += "<li class='card test2'>";
    content += "<img src=" + data.img2 + " alt='image'><div class='info '><h2>" + data.title2 + "</h2>";
    content += "<p>" + data.text2 + "</p></div></li>";
    content += "<li class='card test3'>";
    content += "<img src=" + data.img3 + " alt='image'><div class='info '><h2>" + data.title3 + "</h2>";
    content += "<p>" + data.text3 + "</p></div></li>";
    content += "</ul></div></div>";
    var themeOne = header+content;

    $('.themeContent').html(themeOne);
    buttonClick();
}

function themeSecond(data) {
    console.log(data);
    var header = "";
    var content = "";
    header += "<header class='header2'><div class='head-left-item'><div class='menu-buttons'><button class='active'>Главная</button>";
    header +="<button >Информационный блок</button></div></div><div class='head-right-item'>"
    header +="<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/right-arrow.png' alt='right-arrow'>";
    header += "</div></header>";

    content += "<div class='wrapper2'><ul><li><h2>" + data.title1 + "</h2><img src='static/img/right.png' alt=''></li>"
    content += "<li><h2>" + data.title1 + "</h2><img src='static/img/right.png' alt=''></li>";
    content += "<li><h2>" + data.title2 + "</h2><img src='static/img/right.png' alt=''></li>";
    content += "<li><h2>" + data.title3 + "</h2><img src='static/img/right.png' alt=''></li>"; 
    content += "<li><h2>" + data.title4 + "</h2><img src='static/img/right.png' alt=''></li>";
    content += "</ul></div>";

    var themeSecond = ""
    themeSecond += "<div class='themeSecondFon'><div class='themeOverlay'></div><div class='left-sidebar'><img src='static/img/logo.png' alt='logo'>";
    themeSecond += "<h2>Академия политического менеджмента</h2></div>"
                
           
    themeSecond += header+content;
    themeSecond += "</div></div>"
    $('.themeContent').html(themeSecond);
    buttonClick();
}
var blockNum = ''
function buttonClick(e) {
    var blocks = document.querySelectorAll('.card');
    for(var i = 0; i < blocks.length; i++) {
        blocks[i].onclick = function(e) {
            for(var j = 0; j < blocks.length; j++) {
                blocks[j].classList.remove('block-active');
            }
            this.classList.toggle('block-active');
            console.log(this.className);
            if(this.className == "card test1 block-active") {
               blockNum = '1';
            }else if(this.className == "card test2 block-active") {
                blockNum = '2';
            }else if(this.className == "card test3 block-active") {
                blockNum = '3';
            }
            sendAjaxForm( 'block-num', 'http://0.0.0.0:8888/button/' + blockNum + '/');
            console.log('http://0.0.0.0:8888/button/'+blockNum);
            setTimeout(() => {
                this.classList.remove('block-active')
            },5000);
        }
    }
}
function sendAjaxForm(blockNum, url) {
$.ajax({
url: url, //url страницы (action_ajax_form.php)
type: "POST", //метод отправки
dataType: "html", //формат данных
data: $(blockNum).serialize(), // Сеарилизуем объект
success: function(response) { //Данные отправлены успешно
console.log('+')

},
error: function(response) { // Данные не отправлены
console.log(blockNum);
}
});
}
