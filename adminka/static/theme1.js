
    namespace = '/server'
    var socket = io.connect(location.protocol+ '//' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function() {
         console.log('connected');
    });
    socket.on('message', function(data) {
         console.log(data);
    });

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
//    console.log(data.num)
    header += "<header class='header1'><div class='head-left-item'>";
    header +="<img src='static/img/logo.png' alt='logo'><div><h3>НҰР ОТАН</h3>"
    header +="<p>ОСНОВНОЙ ТЕКСТ<br>БАҒДАРЛАМАСЫ</p></div></div>";
    header += "<div class='head-right-item'><div class='arrows'><button>";
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/right.png' alt='right-arrow'></div>";
    header += "<a href = {{name}}> google </a>";
    header += "<div class='menu-buttons'><button>Главная</button><button class='active'>Информационный блок</button></div></div></header>";


    content += "<div class='wrapper'><div class='container'><ul>";

        for(var i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+ i + "'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";
//        console.log(data.num);
//        console.log(data.test[Math.round(data.num)].ID);

    }







    content += block;
    content += "</ul></div></div>";
    var themeOne = header+content;

    $('.themeContent').html(themeOne);
    buttonClick(data);


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
            console.log("!");
            themeOne(data);



        }

            })

}, 500);
});
}



var blockNum = ''
function buttonClick(data) {

    var blocks = document.querySelectorAll('.card');
    for(var i = 0; i < blocks.length; i++) {
        blocks[i].onclick = function(e) {
            for(var j = 0; j < blocks.length; j++) {
                blocks[j].classList.remove('block-active');
            }
            this.classList.toggle('block-active');
            MyClick();
            console.log(i);

            if(this.className == "card test0 block-active")       {
                blockNum = data.test[0].ID;
                console.log(data);
            }else if(this.className == "card test1 block-active") {
                blockNum =  data.test[1].ID;
            }else if(this.className == "card test2 block-active") {
                blockNum =  data.test[2].ID;
            }else if(this.className == "card test3 block-active") {
                blockNum = data.test[3].ID;
            }else if(this.className == "card test4 block-active") {
                blockNum = data.test[4].ID;
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
namespace = '/server';
console.log(location.protocol);
console.log(document.domain);
console.log(location.port);
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);
console.log(socket)
socket.on('message', function() {
        socket.emit('my event', "my message");
        console.log(socket.emit)
        console.log(socket)
    });


}
