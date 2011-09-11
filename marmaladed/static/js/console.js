var enter_key = 13;

$(document).ready(function() {
	newInputLine();
	$("#terminal").bind("click", function(){
		$(".readLine.active").focus();
	});
});

function joinArgs(array, start, sep) {
	//ok, this is pretty bad function
	joined_string = "";
	for (var i=start; i < array.length; i++) {
		joined_string += array[i] + (i < (array.length-1) ? sep : "");
	}
	return joined_string;
}

function sendCommand(args) {
	$.post("/console/command", args, function(data) {
		$(".line.active").append($("<pre>").text(data));
		newInputLine();
	});
}

function processInput(value){
	if(value.length > 0) {
		args = value.split(" ");
		if(args.length > 0) {
			switch(args[0]) {
				case "stats":
					args.length > 0 ? sendCommand({'command' : 'stats', 'args' : joinArgs(args, 1, " ")}) : sendCommand({'command' : 'stats'});
					break;
				case "delete":
					if(args.length > 0) {
						sendCommand({'command' : 'delete', 'args' : joinArgs(args, 1, " ")});
					}
					break;
				case "clear":
					clearConsole();
					break;
				case "help":
					printHelp();
					break;
			}
		}
	} else {
		newInputLine();
	}
}

function newInputLine() {
	activeInput = $(".readLine.active");
	if(activeInput.length > 0) {
		activeInput.unbind("keydown");
		activeInput.removeClass("active");
		activeInput.attr("disabled", "disabled");
		activeDiv = $(".line.active");
		activeDiv.removeClass("active");
	}
	$("div#terminal").append($('<div>').attr("class", "line active").html('<span class="prompt"> &gt;</span><input type="text" class="readLine active">'));
	activeInput = $(".readLine.active");
	bindInput(activeInput);
	activeInput.focus();
}

function bindInput(obj) {
	obj.bind("keydown", function(ev) {
		switch (ev.keyCode) {
			case enter_key:
				processInput(this.value);
			break;
		}
	});
}

function clearConsole() {
	$("div#terminal").html("");
	newInputLine();
}

function printHelp() {
	$("div#terminal").append($('<p>').html('memcached commands'));
	$("div#terminal").append($('<pre>').html('delete &lt;key&gt; [noreply]	Explicit deletion of items.'));
	$("div#terminal").append($('<pre>').html('stats			General statistics'));
	$("div#terminal").append($('<pre>').html('stats items		Returns information about item storage per slab'));
	$("div#terminal").append($('<pre>').html('stats settings		Returns details of the settings of the running memcached'));
	$("div#terminal").append($('<pre>').html('stats sizes		Returns information about the general size and count of all items stored in the cache'));
	$("div#terminal").append($('<pre>').html('stats slabs		Returns information about each of the slabs'));
	$("div#terminal").append($('<p>').html('marmaladed commands'));
	$("div#terminal").append($('<pre>').html('clear	Clear the console screen'));
	newInputLine();
}