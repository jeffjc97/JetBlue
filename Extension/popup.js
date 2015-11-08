/*
Responsible for maintaining state of the extension. On interaction with the user will update the chrome storage object with relevant fields.
*/

document.addEventListener('DOMContentLoaded', function(){
	var airports;
	var option;

	chrome.storage.sync.get('airports', function(result) {
		console.log("pulling up results");
		airports = result['airports'];
		console.log(airports);
		if(airports != undefined) {
			$(".js-selector").select2().select2("val", airports);
		}
		else {
			$(".js-selector").select2();
		}
	});

	chrome.storage.sync.get('option', function(result) {
		console.log("setting options");
		option = result['option'];
		console.log(option);
		if(option != undefined) {
			$('.opt-button-group').find('[option="' + option + '"]').addClass("selected");
		}
		else {
			option = 0;
			chrome.storage.sync.set({'option':0, 'airports':airports}, function() {
				$('.opt-button-group').find('[option="0"]').addClass("selected")
			});
		}
	})

	$(".js-selector").on("change", function() {
	    var $this = $(this);
	    chrome.storage.sync.get('airports', function(result) {
			airports = result['airports'];
			chrome.storage.sync.set({'option':option, 'airports':$this.select2("val")});
			console.log(airports);
		});
	});

	$('.opt-button').click(function() {
		$('.opt-button-group').find('.selected').removeClass('selected');
		option = $(this).attr("option");
		chrome.storage.sync.set({'option':option, 'airports':airports}, function() {
			console.log("New option: ", option);
		});
		$(this).addClass("selected");
	})
})
