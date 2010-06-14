var processing;

function load_data(data)
{
	graph = new Array(4);
	graph[0] = (data.edges_h);
	graph[1] = (data.edges_v);
	graph[2] = (data.diag_se);
	graph[3] = (data.diag_sw);

	$.get("/media/js/sfit-draw.pjs", function(code) {
		canvas = $("#canvas")[0];
		processing = Processing(canvas, code);
                //calling from JS to PJS:
		processing.setData(graph);
		processing.setCell(4);
	}); 
}

function saved(output)
{
}

function save()
{
	data = processing.getData();
	url = "/grid/api/tshirt/";
	// url = "http://erase.net/dump/save.php";
	// $.post(url, { edges_h: "" + data[0], edges_v: "" + data[1], diag_se: "" + data[2], diag_sw: "" + data[3], cell: "0" }, saved);
	/*
	data_dict = { edges_h: data[0], edges_v: data[1], diag_se: data[2], diag_sw: data[3], cell: "0" };
	alert("lengths: " + data[0].length + ", " + data[1].length + ", " + data[2].length + ", " + data[3].length);
	$.ajax({
		type: 'POST',
		url: url,
		data: data_dict,
		success: saved
	});
	*/
	input = document.getElementById("edges_h"); input.value = data[0];
	input = document.getElementById("edges_v"); input.value = data[1];
	input = document.getElementById("diag_se"); input.value = data[2];
	input = document.getElementById("diag_sw"); input.value = data[3];
	input = document.getElementById("cell"); input.value = 0;
	form = document.getElementById("form"); form.submit();
}

$(document).ready(function()
{
	url = "/grid/api/tshirt/last/";
	// url = "/media/js/data.html";
	$.ajax({
		url: url,
		success: load_data
	});
	$('#save').bind('click', save);
});

