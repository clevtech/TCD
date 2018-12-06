
 $( document ).ready(function() {
    $("#btn").click(
		function(){
			sendAjaxForm('result_form', 'ajax_form', './admin.py');
			return false;
		}
	);
});

function sendAjaxForm(result_form, ajax_form) {
    jQuery.ajax({
        url:     "http://0.0.0.0:8888/", //url страницы (action_ajax_form.php)
        type:     "POST", //метод отправки
        dataType: "json", //формат данных
        data: jQuery("#"+ajax_form).serialize(),  // Сеарилизуем объект
        success: function(response) { //Данные отправлены успешно
        var	result = $.parseJSON(response);
        console.log(response)
        	document.getElementById(result_form).innerHTML = "Имя: "+result.block+"<br>Телефон: "+result.phone;
    	},
    	error: function(response) { // Данные не отправлены
    		document.getElementById(result_form).html;
    		  var out = '';
    		  var i = 0;
                while(i < 5){
                        out +=   "<li style= 'display: list-item;' class= 'mjs-nestedSortable-leaf' id= 'menuItem_'>";
                        out +=  "<div class='menuDiv'>";
                        out +=   "<span title= 'Click to show/hide children' class='disclose ui-icon ui-icon-minusthick'>";
                        out +=  "<span></span>";
                        out +=  "</span>";
                        out +=  "<span title= 'Click to show/hide item editor' data-id='7' class='expandEditor ui-icon ui-icon-triangle-1-n'>";
                        out +=  "<span></span>";
                        out += "</span>";
                        out += "<span>";
                        out += "<span data-id='7' class='itemTitle'>f</span>";
                        out += "<span title='Click to delete item.' data-id='7' class='deleteMenu ui-icon ui-icon-closethick'>";
                        out += "<span></span>";
                        out += "</span>";
                        out += "</span>";
                        out += "<div id='menuEdit7' class='menuEdit hidden'>";
                        out +=  "<p>Content or form, or nothing here. Whatever you want.</p>";
                        out += "</div>";
                        out += "</div>";
                        out += "</li>";
                        $('#90').html(out);
                        i++;
                        }
                        alert('bye!');





    	}
 	});
}
