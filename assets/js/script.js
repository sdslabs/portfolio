History.Adapter.bind(window,'statechange',function(){ // Note: We are using statechange instead of popstate
	var state = History.getState();
	$.get(state.url, function(html){
		$('main')[0].innerHTML=$(html).filter('main')[0].innerHTML;
		$('title')[0].innerText=$(html).filter('title')[0].innerText;
	})
});
//Someone clicked on a link in the left pane
$('nav a').click(function(e){
	var link = e.target.getAttribute('href');//Should be relative
	History.pushState(null, null, link);
	e.preventDefault();
});