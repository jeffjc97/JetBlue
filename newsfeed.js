var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);


multiples = 0;
scroll = 500;

document.addEventListener("scroll", function() {
	if($(document).scrollTop() > (multiples + 1) * scroll) {
		last = $('._5jmm').last();
		if(!last.next().hasClass('swag')) {
			$("<div class='swag'>SWAGG</div>").insertAfter(last);
		}
		multiples++;
	}
});