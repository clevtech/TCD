
var ekran = document.getElementById("ekran").innerText;
var lang = document.getElementById("ekran").innerText;
console.log(lang);
console.log(ekran);
var namespace = '/disp/' + ekran + "/" + lang + "/data.json?";
var path = location.protocol + '//' + document.domain + ':' + location.port + namespace


$('document').ready(function() {
      loadData();
});

var lastData = ''

function loadData() {

  	$.getJSON(path  + new Date().getTime(), function(data) {
        console.log(data)
  		var out = '';
  		if(data.ekran == 1){
	      	out += "<div class='layout-center'>";
	      	out += "<img src=" + data.dichki[1].img + ">";
	      	out += "</div>";
	      	lastData = data.id;
  		}else if(data.ekran == 2){
          out += "<div class='layout-left'>";
          out += "<img src="+ data.dochki[1].log +" alt='' />"
	        out += "<img src="+ data.dochki[1].img + ">";
	        out += "</div>";
	        out += "<div class='layout-right'>";
	        out += "<span></span>";
	        out += "<h1>" + data.dochki[1].title + "</h1>";
	        out += "<p>" + data.dochki[1].text + "</p>";
	        out += "</div>";
	        lastData = data.id;
  		}
  		else if(data.ekran == 3){
  			out += "<video controls loop muted autoplay";
  			out += " src=" + data.dochki[1].video + " width='100%' height='100%'>";
            out += "Sorry, your browser doesn't support embedded videos."
            out += "</video>"
            lastData = data.id;
  		}else{
  			loadData();
  		}
    	$('.wrapper-content').html(out);
    	setInterval(function(){
    		$.getJSON(path  + new Date().getTime(), function(data) {
  				if(data.id !== lastData){
   					loadData();
  				}
  			})
  		}, 1000);
    })
}
