////var element = document.getElementById('{{text}}');
////alert('warning!');
////element.color = 'red';
////alert('good!');
//
//
//$('section.demo').html('<div id = 'tree'><li style="display: list-item;" class="mjs-nestedSortable-leaf" id="menuItem_7"> <div class="menuDiv"><span title="Click to show/hide children" class="disclose ui-icon ui-icon-minusthick"><span></span></span><span title="Click to show/hide item editor" data-id="7" class="expandEditor ui-icon ui-icon-triangle-1-n"><span></span></span><span> <span data-id="7" class="itemTitle">f</span><span title="Click to delete item." data-id="7" class="deleteMenu ui-icon ui-icon-closethick"><span></span></span></span><div id="menuEdit7" class="menuEdit hidden"><p>Content or form, or nothing here. Whatever you want.</p> </div></div></li></div>')
////var str = '<div id = 'tree'><li style="display: list-item;" class="mjs-nestedSortable-leaf" id="menuItem_7"> <div class="menuDiv"><span title="Click to show/hide children" class="disclose ui-icon ui-icon-minusthick"><span></span></span><span title="Click to show/hide item editor" data-id="7" class="expandEditor ui-icon ui-icon-triangle-1-n"><span></span></span><span> <span data-id="7" class="itemTitle">f</span><span title="Click to delete item." data-id="7" class="deleteMenu ui-icon ui-icon-closethick"><span></span></span></span><div id="menuEdit7" class="menuEdit hidden"><p>Content or form, or nothing here. Whatever you want.</p> </div></div></li></div>'
//
//              ('document').ready(function() {
//        /*$.ajaxSetup({
//        url: "http://localhost:8888/static/data.json",
//        cache: false,
//        dataType: "json",
//                        });*/
                        function setHeadline(num){
                        num = num || 1;
                        $("#90").html($('#headline'+num).html());

                        var out = '';

                        out +=   "<li style= 'display: list-item;' class= 'mjs-nestedSortable-leaf' id= 'menuItem_7'>";
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

                        alert('bye!');

}

