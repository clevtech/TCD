window.onload  = function() {
     var namespace = '/test';
     var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

      socket.on('my_response', function(msg) {

        Block(msg);
      }
      )



       function Block(data) {
            let test = data.test
            let content = document.getElementsByClassName('wrapper2')[0];

            var ul = document.createElement('ul');

            for(var i = 0;i < test.length; i++) {

                ul.innerHTML += "<li><h2>" + test[i].title +"</h2><img src='" + test[i].img + "' alt=''></li>";
            }
            content.appendChild(ul);

        }

}






