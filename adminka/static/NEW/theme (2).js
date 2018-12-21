$('document').ready(function() {
        loadTheme();
        
});
var url = document.URL + 'static/json/data.json';

var lastData = '';
function loadTheme() { 
    
    $.getJSON(url, function(data) {
        
        if(data.theme == 1) {
            themeOne(data);
            lastData = data.theme;
        }else if(data.theme == 2) {
            themeSecond(data);
            lastData = data.theme;
        }else if(data.theme == 3) {
            themeThird(data);
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
    let header = "";
    let content = "";
    let block = "";
    let block2 = "";

    header += "<header class='header'><div class='head-left-item'>";
    header +="<img src='static/img/logo.png' alt='logo'><div><h3>НҰР ОТАН</h3>"
    header +="<p>ПАРТИЯСЫ САЙЛАУАЛДЫ<br>БАҒДАРЛАМАСЫ</p></div></div>";
    header += "<div class='head-right-item'><div class='arrows'>";
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img id='btn' src='static/img/homewhite.png' alt='home'><img src='static/img/right-arrow.png' alt='right-arrow'></div>";
    header += "<div class='menu-buttons'><span id='home' class='active1'>Главная</span><span id='info-btn'>Информационный блок</span></div></div></header>";

    content += "<div class='wrapper'><div class='container'><ul id='start-block'>";
    for(let i = 0; i < data.test.length; i++) {
        block += "<li class='card test"+i+"'>";
        block += "<img src="+ data.test[i].img +" alt='image'><div class='info'><h2>"+ data.test[i].title + "</h2>";
        block += "<p>"+ data.test[i].text +"</p></div></li>";
    }
    
    content += block;
    content += "</ul><ul id='inside-block'>";
    for(let i = 0; i < data.test2.length; i++) {
        console.log()
        block2 += "<li class='card'>";
        block2 += "<img src="+ data.test2[i].img + " alt='image'><div class='info'><h2>"+ data.test2[i].title +" </h2>";
        console.log(data.test2[i].title);
        block2 += "<p>"+ data.test2[i].text +"</p></div></li>";
    }

    content += block2;
    content += "</div></div>";
    var themeOne = header+content;

    $('.theme-content').html(themeOne);
    buttonClick();
}

function themeSecond(data) {
    let header = "";
    let content = "";
    let block = "";
    header += "<header class='header2'><div class='head-left-item'><div class='menu-buttons'><span class='active'>Главная</span>";
    header += "<span >Информационный блок</button></div></div><div class='head-right-item'>"
    header += "<img src='static/img/left-arrow.png' alt='left-arrow'><img src='static/img/homewhite.png'><img src='static/img/right-arrow.png' alt='right-arrow'>";
    header += "</div></header>";

    content += "<div class='wrapper2'><ul>"

    for(let i = 0; i < data.test.length; i++) {
        block += "<li><h2>"+ data.test[i].title +"</h2><img src='static/img/right.png' alt=''></li>";
    }

    content += block;
    content += "</ul></div>";

    var themeSecond = ""
    themeSecond += "<div class='theme-second-fon'><div class='theme-overlay'></div><div class='left-sidebar'><img src='static/img/logo.png' alt='logo'>";
    themeSecond += "<h2>Академия политического менеджмента</h2></div>"
           
    themeSecond += header+content;
    themeSecond += "</div></div>"
    $('.theme-content').html(themeSecond);

    buttonClick();
}

function themeThird(data) {
    let header = "";
    let content = "";

    header += "<header class='header3'><div class='left-item'><img src='static/img/logo.png' alt='logo'>";
    header += "<div class='logo-text'>Институт стратегических инициатив</div></div>";
    header += "<div class='right-item'><div class='menu-buttons'><span class='home'>Главная</span><span>Информационый блок</span></div>"
    header += "<div class='arrows'><img src='static/img/left.png' alt=''><img src='static/img/home' alt='home'><img src='static/img/right.png' alt=''></div></header>"
    
    content += "<div class='wrapper3'>";
    content += "<div class='big-block'><h3 class='text'>Lorem ipsum dolor.</h3>";
    content += "<span>next...</span></div>";
    content += "<div class='column-block'><div class='small-top-block'>";
    content += "<h3 class='text'>Lorem ipsum.</h3><span>next...</span></div>";
    content += "<div class='small-bottom-block'><h3 class='text'>Lorem ipsum dolor.</h3>";
    content += "<span>next...</span></div></div></div>"
    console.log(content);
    let themeThird = header + content;
    $(".theme-content").html(themeThird);
      
}

let blockNum = "";
function buttonClick(e) {
    let blocks = document.querySelectorAll('.card');
    let startBlock = document.getElementById('start-block');
    let insideBlock = document.getElementById('inside-block');
    let btn = document.getElementById('btn');
    let home = document.getElementById('home');
    let info = document.getElementById('info-btn');
    btn.onclick = (e) => {
        console.log('+');
        startBlock.style.display = 'flex';
        insideBlock.style.display = 'none';
        info.classList.remove('active1');
        home.classList.add('active1');
    }

    for(let i = 0; i < blocks.length; i++) {
        blocks[i].onclick = function(e) {
            for(let j = 0; j < blocks.length; j++) {
                blocks[j].classList.remove('block-active');
            }
            this.classList.toggle('block-active');

            if(this.className == "card test0 block-active") {
                console.log(startBlock);
                startBlock.style.display = 'none';
                insideBlock.style.display = 'flex';
                info.classList.add('active1');
                home.classList.remove('active1');
                this.classList.remove('block-active');
                blockNum = "block1";
            }else if(this.className == "card test1 block-active") {
                console.log("test2");
                blockNum = "block2";
            }else if(this.className == "card test2 block-active") {
                console.log("test3");
                blockNum = "block3";
            }
            setTimeout(() => {
                this.classList.remove('block-active')
            },5000);
        }
    }
}
