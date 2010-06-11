function callback(data)
{
	alert("it worked");
}

$(document).ready(function() {
	/*url = "http://172.29.17.90:8080/api/netjs/griff/";*/
	url = "data.html";
	url = "http://localhost:8080/api/netjs/griff/";
	$.ajax({
		url: url,
		success: function(data) { 
        $('.result').html(data); alert("ok: " + data); 
        }
	});
});

