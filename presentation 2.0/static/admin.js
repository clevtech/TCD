$('document').ready(function() {
        /*$.ajaxSetup({
        url: "http://localhost:8888/static/data.json",
        cache: false,
        dataType: "json",
                        });*/

		loadData();

});
var lastData = ''
function loadData() {
  	$.getJSON('http://0.0.0.0:8888/static/json/data.json', function(data) {
  	    console.log(data);
  		var out = '';
  		if(data.theme == 2){
	      	out += "<div class='layout-center'>";
	      	out += "<img src="+ data.img1 +">";
	      	out += "</div>";
	      	lastData = data.theme;
  		}else if(data.theme == 1){
  			out += "<div class='layout-left'>";
	        out += "<img src="+ data.img1 + ">";
	        out += "</div>";
	        out += "<div class='layout-right'>";
	        out += "<span></span>";
	        out += "<h1>" + data.title1 + "</h1>";
	        out += "<p>" + data.text1 + "</p>";
	        out += "</div>";
	        lastData = data.theme;
  		}
  		else if(data.theme == 3){
  			out += "<video loop muted autoplay";
  			out += " src=" + data.video + " width='100%' height='100%'>";
            out += "Sorry, your browser doesn't support embedded videos."
            out += "</video>"
            lastData = data.theme;
  		}else{
  			loadData();
  		}
    	$('.wrapper-content').html(out);
    	setInterval(function(){
    		$.getJSON('http://0.0.0.0:8888/static/json/data.json', function(data) {
  				if(data.theme !== lastData){

   					loadData();
  				}
  			})
  		}, 500);
    })
}
