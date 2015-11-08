// chrome.runtime.onInstalled.addListener(function (object) {
//     chrome.tabs.create({url: "popup.html"}, function (tab) {
//         console.log("Options launched!");
//     });
// });

var url = "https://ancient-fjord-1030.herokuapp.com/query/";


chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
	a = request.airport
	o = request.option
	$.ajax({
	    url: url + a + '/option/' + o,
		type: 'GET',
	    success: function(result) {
	    	sendResponse({status:"success", result:result})
    	},
	   	error: function(result) {
	   		sendResponse({status:"error"})
   		}
	})
	return true
});