$(document).ready(function() {
        $.ajaxSetup({
        url: "http://0.0.0.0:8888/static/json/data.json",
        cache: false,
        dataType: "json",
                        });
        console.log(themeOne)
		loadTheme();

});
var url = document.URL + 'static/json/data.json';
        console.log(url)
var lastData = '';
function loadTheme() { 
    
    $.getJSON(url, function(data) {
        console.log(data);
        themeOne(data);
        innerBlock(data);


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
    var block = "";
    header += "<header class='header1'><div class='head-left-item'>";
    header +="<img src='static/img/logo.png' alt='logo'><div><h3>НҰР ОТАН</h3>"
    header +="<p>ОСНОВНОЙ ТЕКСТ<br>БАҒДАРЛАМАСЫ</p></div></div>";
    header += "<div class='head-right-item'><div class='arrows'>";
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/right-arrow.png' alt='right-arrow'></div>";
    header += "<div class='menu-buttons'><button>Главная</button><button class='active'>Информационный блок</button></div></div></header>";

    content += "<div class='wrapper'><div class='container'><ul>";
    if(data.num == '0') {
        innerBlock();
    }
        else if(data.num == '1')
        {
            for(var i = 0; i < data.test.length; i++) {
            block += "<li class='card test"+ i + "'>";
            block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
            block += "<p>"+ data.test[i].text +"</p></div></li>";
            block += "<li class='card test"+ i + "'>";
            block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
            block += "<p>"+ data.test[i].text +"</p></div></li>";
            console.log('NUMBER 2');
        }
        }
        else if (data.num == '2')
        {
            for(var i = 0; i < data.test.length; i++) {
            block += "<li class='card test"+ i + "'>";
            block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
            block += "<p>"+ data.test[i].text +"</p></div></li>";
            console.log('NUMBER 2');
        }
        }
            else if (data.num == '3')
        {
            for(var i = 0; i < data.test.length; i++) {
            block += "<li class='card test"+ i + "'>";
            block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
            block += "<p>"+ data.test[i].text +"</p></div></li>";
            console.log('NUMBER 3');
        }
        }
        else{
        alert('bad!');
        }

    content += block;
    content += "</ul></div></div>";
    var themeOne = header+content;

    $('.themeContent').html(themeOne);
    buttonClick();
}

function innerBlock(data) {
        var block = ''
        for(var i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+ i + "'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";
        console.log('NUMBER 1');

}
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

            if(this.className == "card test0 block-active") {
                blockNum = '1';
            }else if(this.className == "card test1 block-active") {
                blockNum = '2';
            }else if(this.className == "card test2 block-active") {
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
type: "POST", //мжетод отправки
dataType: "html", //формат данных
data: $(blockNum).serialize(), // Сеарилизуем объект
success: function(response){

 //Данные отправлены успешно
console.log(blockNum)

},
error: function(response) { // Данные не отправлены
console.log(blockNum);
}
});
}


