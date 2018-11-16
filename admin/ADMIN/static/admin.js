$('document').ready(function() {
        $.ajaxSetup({
        url: "http://192.168.8.100:8888/",
        cache: false,
        dataType: "json",
                        });

		loadData();

});
var lastData = ''
function loadData() {
  	$.getJSON('http://192.168.8.100:8888/static/data.json', function(data) {
  	    console.log(data);
  		var out = '';
  		if(data._id == 1){
	      	out += "<div class='layout-center'>";
	      	out += "<a href="+ data.url +">LOL</a>";
	      	out += "</div>";
	      	lastData = data._id;
  		}else if(data._id == 2){
  			out += "<div class='layout-left'>";
	        out += "<a href="+ data.url +">";
	        out += "</div>";
	        out += "<div class='layout-right'>";
	        out += "<span></span>";
	        out += "<h1>" + data.title + "</h1>";
	        out += "<p>" + data.text + "</p>";
	        out += "</div>";
	        lastData = data._id;
  		}
  		else if(data._id == 3){
  			out += "<video loop muted autoplay";
  			out += "<a href="+ data.url +">";
            out += "Sorry, your browser doesn't support embedded videos."
            out += "</video>"
            lastData = data._id;
  		}else{
  			loadData();
  		}
    	$('.wrapper-content').html(out);
    	setInterval(function(){
    		$.getJSON('http://192.168.8.100:8888/static/data.json', function(data) {
  				if(data._id !== lastData){

   					loadData();
  				}
  			})
  		}, 500);
    })
}



