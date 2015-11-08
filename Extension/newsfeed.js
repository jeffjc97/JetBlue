var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


multiples = 0;
scroll = 1500;
req = false;

var airports;
url = "https://ancient-fjord-1030.herokuapp.com/query/"

chrome.storage.sync.get('airports', function(result) {
		airports = result['airports'].join('&');
})

function injectAd(){
	$(".userContent").each(function() {
		console.log($(this).innerHTML);
		var knwlInstance = new Knwl('english');
		knwlInstance.init($(this).html());
		var places = knwlInstance.get('places');
		for (var ii = 0; ii < places.length; ii++) {
			for (var key in places[ii]) {
				if (key !== 'found') {
					if (key !== 'preview' && !$(this).closest("._5jmm").next().hasClass('jetblue-wrapper') && !req) {
						console.log(key +" **** " + places[ii][key]);
						req = true;
						obj = $(this);
						chrome.runtime.sendMessage({airport:airports}, function(response) { 
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
									<div class='jb jb-1'>\
										<img class='image' src='" + result[0].img_url + "'>\
										<div class='loc'>"+result[0].city+" ("+result[0].date+")</div>\
										<div class='price'>as low as $"+result[0].price+"</div>\
									</div>\
									<div class='jb jb-2'>\
										<img class='image' src='" + result[0].img_url + "'>\
										<div class='loc'>"+result[0].city+" ("+result[0].date+")</div>\
										<div class='price'>as low as $"+result[0].price+"</div>\
									</div>\
									<div class='jb jb-3'>\
										<img class='image' src='" + result[0].img_url + "'>\
										<div class='loc'>"+result[0].city+" ("+result[0].date+")</div>\
										<div class='price'>as low as $"+result[0].price+"</div>\
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
						// responseObj = {
						// 	"img_url":"https://en.wikipedia.org/wiki/Boston#/media/File:Boston_Back_Bay_reflection.jpg",
						// 	"city":"Boston",
						// 	"price":"500",
						// 	"date":"11/7/2015",
						// 	"savings":"400"
						// };

						// $("<div class='jetblue-wrapper'>\
						// <div class='header-text'>JetBlue Travel Suggestions</div>\
						// <div class='jb jb-1'>\
						// 	<img class='image' src='"+responseObj.img_url+"'>\
						// 	<div class='loc'>"+responseObj.city+"</div>\
						// 	<div class='price'>No more than "+responseObj.price+"</div>\
						// </div>\
						// <div class='jb jb-2'>\
						// 	<img class='image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Egretta_garzetta_2015-06-17.jpg/1000px-Egretta_garzetta_2015-06-17.jpg'>\
						// 	<div class='loc'>Jamaica</div>\
						// 	<div class='price'>as low as $20</div>\
						// </div>\
						// <div class='jb jb-3'>\
						// 	<img class='image' src='https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Egretta_garzetta_2015-06-17.jpg/1000px-Egretta_garzetta_2015-06-17.jpg'>\
						// 	<div class='loc'>Japan</div>\
						// 	<div class='price'>as low as $30</div>\
						// </div>\
						// </div>").insertAfter($(this).closest("._5jmm"));	
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
