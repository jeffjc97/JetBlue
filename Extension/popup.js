document.addEventListener('DOMContentLoaded', function(){
	var airports;
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


	
	$(".js-selector").on("change", function() {
	    var $this = $(this);
	    chrome.storage.sync.get('airports', function(result) {
			airports = result['airports'];
			chrome.storage.sync.set({'airports':$this.select2("val")});
			console.log(airports);
		});
	});
})
