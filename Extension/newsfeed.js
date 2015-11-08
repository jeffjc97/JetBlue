//Allows injection of jQuery into Facebook's feed
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


multiples = 0;
scroll = 1500;
// req = false;

var option;
var airports;
url = "https://ancient-fjord-1030.herokuapp.com/query/"

chrome.storage.sync.get('airports', function(result) {
		airports = result['airports'].join('&');
})

chrome.storage.sync.get('option', function(result) {
		option = result['option'];
})

/*
Runs on page load and every certain amount of scroll distance. Grabs all user content on the page and parses it for locations.
If a location is found, the data is sent to ther server. If it matches a destination, that destination is offered. Otherwise,
the destination is offered based on preference in the options.
*/
function injectAd(){
	var placed = false;
	$(".userContent").each(function() {
		console.log($(this).innerHTML);
		var knwlInstance = new Knwl('english');
		knwlInstance.init($(this).html());
		var places = knwlInstance.get('places');
		for (var ii = 0; ii < places.length; ii++) {
			for (var key in places[ii]) {
				if (key !== 'found') {
					if (key !== 'preview' && !$(this).closest("._5jmm").next().hasClass('jetblue-wrapper') && !placed) {
						console.log(key +" **** " + places[ii][key]);
						placed = true;
						// req = true;
						obj = $(this);
						chrome.runtime.sendMessage({airport:airports, option:option}, function(response) { 
							if(response.status == "success") {
								result = response.result;
								console.log(result);
								// console.log("closest");
								// console.log(obj.closest("._5jmm"));
								for (var i = result.length - 1; i >= 0; i--) {
									var price = "" + result[i].price;
									if(price.indexOf(".") >= 0 && price.substring(price.indexOf("."),price.length).length == 2){
										result[i].price = price.substring(0, price.indexOf("."));
									}
								};
								$("<div class='jetblue-wrapper'>\
									<div class='header-text'>JetBlue Travel Suggestions</div>\
									<div id='" + result[0].g_id + "' class='jb jb-1'>\
										<a target='_blank' href='https://ancient-fjord-1030.herokuapp.com/details/" + result[0].g_id +"'><img class='image' src='" + result[0].img_url + "'></a>\
										<div class='loc'>"+result[0].city+" ("+result[0].date+")</div>\
										<div class='price'>as low as $"+result[0].price+"</div>\
									</div>\
									<div id='" + result[1].g_id + "' class='jb jb-2'>\
										<a target='_blank' href='https://ancient-fjord-1030.herokuapp.com/details/" + result[1].g_id +"'><img class='image' src='" + result[1].img_url + "'></a>\
										<div class='loc'>"+result[1].city+" ("+result[1].date+")</div>\
										<div class='price'>as low as $"+result[1].price+"</div>\
									</div>\
									<div id='" + result[2].g_id + "' class='jb jb-3'>\
										<a target='_blank' href='https://ancient-fjord-1030.herokuapp.com/details/" + result[2].g_id +"'><img class='image' src='" + result[2].img_url + "'></a>\
										<div class='loc'>"+result[2].city+" ("+result[2].date+")</div>\
										<div class='price'>as low as $"+result[2].price+"</div>\
									</div>\
									</div>").insertAfter(obj.closest("._5jmm"));
							}
							else {
								console.log("error");
							} 
						});
					}
				}
			}
		}
	});
}

$(document).ready(function(){
	injectAd();

	document.addEventListener("scroll", function(){
		if($(document).scrollTop() > (multiples + 1) * scroll) {
			injectAd();
			multiples++;
		}
	});
});
