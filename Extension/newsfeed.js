var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


multiples = 0;
scroll = 500;

var airports;
url = "https://ancient-fjord-1030.herokuapp.com/query/"

chrome.storage.sync.get('airports', function(result) {
		airports = result['airports'].join('&');
})

document.addEventListener("scroll", function() {
	if($(document).scrollTop() > (multiples + 1) * scroll) {
		var elm = document.getElementsByClassName("userContent");
		Array.prototype.forEach.call(elm, function(element) {
			//console.log(element.innerHTML);
			var knwlInstance = new Knwl('english');
			knwlInstance.init(element.innerHTML);
			var places = knwlInstance.get('places');
			for (var ii = 0; ii < places.length; ii++) {
				for (var key in places[ii]) {
					if (key !== 'found') {
						if (key !== 'preview' && !$(element).next().hasClass('jetblue-wrapper')) {
							console.log(key +" **** " + places[ii][key]);
							chrome.runtime.sendMessage({airport:airports}, function(response) { 
								if(response.status == "success") {
									console.log("DFSDFDS");
									result = response.result;
									console.log(result);
								}
								else {
									console.log(response.status);
									alert("uhoh");
								} 
							});
						}
					}
				}
			}
		});
		// last = $('._5jmm').last();
		// if(!last.next().hasClass('jetblue-wrapper')) {
		// 	console.log(airports);
		// 	chrome.runtime.sendMessage({airport:airports}, function(response) { 
		// 		if(response.status == "success") {
		// 			console.log("DFSDFDS");
		// 			result = response.result;
		// 			console.log(result);
		// 		}
		// 		else {
		// 			console.log(response.status);
		// 			alert("uhoh");
		// 		} 
		// 	});
			// $.ajax({
			// 	url: url + airports,
			// 	type: 'GET',
			// 	dataType: 'jsonp',
			// 	success: function(returned) {
			// 		console.log(airports);
			// 		console.log(returned);
			// 		$("<div class='jetblue-wrapper'>\
			// 		<div class='header-text'>JetBlue Travel Suggestions</div>\
			// 		<div class='jb jb-1'>\
			// 			<img class='image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Egretta_garzetta_2015-06-17.jpg/1000px-Egretta_garzetta_2015-06-17.jpg'>\
			// 			<div class='loc'>Bahamas</div>\
			// 			<div class='price'>as low as $50</div>\
			// 		</div>\
			// 		<div class='jb jb-2'>\
			// 			<img class='image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Egretta_garzetta_2015-06-17.jpg/1000px-Egretta_garzetta_2015-06-17.jpg'>\
			// 			<div class='loc'>Jamaica</div>\
			// 			<div class='price'>as low as $20</div>\
			// 		</div>\
			// 		<div class='jb jb-3'>\
			// 			<img class='image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Egretta_garzetta_2015-06-17.jpg/1000px-Egretta_garzetta_2015-06-17.jpg'>\
			// 			<div class='loc'>Japan</div>\
			// 			<div class='price'>as low as $30</div>\
			// 		</div>\
			// 		</div>").insertAfter(last);	
			// 	},
			// 	failure: function(returned) {
			// 		alert("Failed!!!!");
			// 	}
			// });
		}
		multiples++;
	}
});

if (document.createEvent) { // W3C
    var ev = document.createEvent('Event');
    ev.initEvent('resize', true, true);
    window.dispatchEvent(ev);
} else { // IE
    document.fireEvent('onresize');
}