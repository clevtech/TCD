//отслеживаем клик вызываем функцию и заменяем все то что было у нас в class = container и заменяем его соими значениями + block
$(document).ready(function() {
        $.ajaxSetup({
        url: "http://0.0.0.0:8888/static/json/data.json",
        crossDomain:true,
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
        console.log(data, '+');
        themeOne(data);


    })

}

function themeOne(data) {
    var header = "";
    var content = "";
    var block = "";
    console.log(data.num)
    header += "<header class='header1'><div class='head-left-item'>";
    header +="<img src='static/img/logo.png' alt='logo'><div><h3>НҰР ОТАН</h3>"
    header +="<p>ОСНОВНОЙ ТЕКСТ<br>БАҒДАРЛАМАСЫ</p></div></div>";
    header += "<div class='head-right-item'><div class='arrows'>";
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/right-arrow.png' alt='right-arrow'></div>";
    header += "<div class='menu-buttons'><button>Главная</button><button class='active'>Информационный блок</button></div></div></header>";

    content += "<div class='wrapper'><div class='container'><ul>";

    if(data.num == '1')
    {
        $('.container').remove();
        for(var i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+ i + "'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";

        console.log(data.num);



    }

    }
    if(data.num == '2'){

        for(var i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+ i + "'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";
        console.log(data.num);



    }

    }
    if(data.num == '3'){
        $('.container').remove();

        for(var i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+ i + "'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";
        console.log(data.num);

    }

    }
    else
    {

    console.error('err')

    }
    content += block;
    content += "</ul></div></div>";
    var themeOne = header+content;

    $('.themeContent').html(themeOne);
    buttonClick();


    }

function MyClick(data){
 $(".container").click(function() {
      $.ajaxSetup({
        url: "http://0.0.0.0:8888/static/json/data.json",
        crossDomain:true,
        cache: false,
        dataType: "json",
                        });
 setTimeout(function(){
    $.getJSON('http://0.0.0.0:8888/static/json/data.json', function(data) {
     console.log("NEW JSON")
        if(data.num != 0){
            themeOne(data);



        }

            })

}, 2000);
});
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
            MyClick();
            if(this.className == "card test0 block-active")       {
                blockNum = '1';
            }else if(this.className == "card test1 block-active") {
                blockNum = '2';
            }else if(this.className == "card test2 block-active") {
                blockNum = '3';
            }else if(this.className == "card test3 block-active") {
                blockNum = '4';
            }else if(this.className == "card test4 block-active") {
                blockNum = '5';
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


