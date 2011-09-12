var enter_key = 13;

var HOST = "";

$(document).ready(function() {
	if($("#host").val() != "") {
		HOST = $("#host").val();
		newInputLine();
		$("#terminal").bind("click", function(){
			$(".readLine.active").focus();
		});
		$("#host").bind("change", function(){
			HOST = $("#host").val();
			clearConsole();
		});
	}
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

var storeCommand = [];

function processInput(value){
	if(value.length > 0) {
		args = value.split(" ");
		if(args.length > 0) {
			switch(args[0]) {
				case "stats":
					storeCommand.length = 0;
					args.length > 0 ? sendCommand({'host' : HOST, 'command' : 'stats', 'args' : joinArgs(args, 1, " ")}) : sendCommand({'host' : HOST, 'command' : 'stats'});
					break;
				case "delete":	
				case "get":
					storeCommand.length = 0;
					if(args.length > 0) {
						sendCommand({'host' : HOST, 'command' : args[0].toLowerCase(), 'args' : joinArgs(args, 1, " ")});
					}
					break;
				case "set":	
				case "add":
				case "replace":
				case "append":
				case "prepend":
				case "cas":
					storeCommand.length = 0;
					if(args.length > 0) {
						if(storeCommand.length == 0) {
							storeCommand.push(args[0]);
							storeCommand.push(joinArgs(args, 1, " "));
							newInputLine();
						}
					}
					break;
				case "clear":
					storeCommand.length = 0;
					clearConsole();
					break;
				case "help":
					storeCommand.length = 0;
					printHelp();
					break;
				default:
					if(storeCommand.length > 0) {
						sendCommand({'host' : HOST, 'command' : storeCommand[0].toLowerCase(), 'args' : storeCommand[1].toLowerCase(), 'value' : args.join(" ")});
					}
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
	$("div#terminal").append($('<pre>').html('[set|add|replace|append|prepend] &lt;key&gt; &lt;flags&gt; &lt;exp_time&gt; &lt;bytes&gt; [no_reply]\\r\\n&lt;data block&gt;\\r\\n'));
	$("div#terminal").append($('<pre>').html('	- \"set\" means \"store this data\".'));
	$("div#terminal").append($('<pre>').html('	- \"add\" means \"store this data, but only if the server *doesn\'t* already hold data for this key\".'));
	$("div#terminal").append($('<pre>').html('	- \"replace\" means \"store this data, but only if the server *does* already hold data for this key\".'));
	$("div#terminal").append($('<pre>').html('	- \"append\" means \"add this data to an existing key after existing data\".'));
	$("div#terminal").append($('<pre>').html('	- \"prepend\" means \"add this data to an existing key before existing data\".'));
	$("div#terminal").append($('<br>'));
	$("div#terminal").append($('<pre>').html('cas &lt;key&gt; &lt;flags&gt; &lt;exptime&gt; &lt;bytes&gt; &lt;cas unique&gt; [no_reply]\\r\\n&lt;data block&gt;\\r\\n'));
	$("div#terminal").append($('<pre>').html(' 	- means "store this data but only if no one else has updated since I last fetched it.".'));
	$("div#terminal").append($('<br>'));
	$("div#terminal").append($('<pre>').html('get &lt;key&gt;*		Retrieves values in cache. * means one or more key strings separated by whitespace'));
	$("div#terminal").append($('<pre>').html('delete &lt;key&gt; [noreply]	Explicit deletion of items'));
	$("div#terminal").append($('<pre>').html('stats			General statistics'));
	$("div#terminal").append($('<pre>').html('stats items		Returns information about item storage per slab'));
	$("div#terminal").append($('<pre>').html('stats settings		Returns details of the settings of the running memcached'));
	$("div#terminal").append($('<pre>').html('stats sizes		Returns information about the general size and count of all items stored in the cache'));
	$("div#terminal").append($('<pre>').html('stats slabs		Returns information about each of the slabs'));
	$("div#terminal").append($('<pre>').html('clear			Clear the console screen'));
	newInputLine();
}