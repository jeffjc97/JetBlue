var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


multiples = 0;
scroll = 500;

document.addEventListener("scroll", function() {
	if($(document).scrollTop() > (multiples + 1) * scroll) {
		last = $('._5jmm').last();
		if(!last.next().hasClass('swag')) {
			$("<div class='col-md-4 image-container-col'>\
				<img class='display-image-bottom img-responsive img-thumbnail' src='http://weknowyourdreams.com/images/paradise/paradise-01.jpg'/>\
				<div class='display-image-top'>CHEAP PRICE OF 19.99!\
				</div>\
				</div>").insertAfter(last);		}
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