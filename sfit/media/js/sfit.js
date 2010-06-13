var processing;

function load_data(data)
{
	graph = jQuery.parseJSON(data);

	$.get("/media/js/sfit-draw.pjs", function(code) {
		canvas = $("#canvas")[0];
		processing = Processing(canvas, code);
                //calling from JS to PJS:
		processing.setData(graph);
	}); 
}

function saved(output)
{
	alert("saved! " + output);
}

function save()
{
	alert("saving data: " + data[0]);
	// String data[] = processing.getData();
	// $.post("save.php", { edges_h: data[0], edges_v: data[1], edges_d_se: data[2], edges_d_sw: data[3] }, saved, "json");
}

$(document).ready(function()
{
	url = "/grid/api/tshirt";
	$.ajax({
		url: url,
		success: load_data
	});
	$('#save').bind('click', save);
});

