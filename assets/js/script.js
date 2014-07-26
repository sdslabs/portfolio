//Block Hovering
$(document).ready(function(){
	$('.block-work').hover(
		function(){//Hover in
		$(this).find('.hover').slideDown(50);
		},
		function(){//Hover out
		$(this).find('.hover').slideUp(50);
		});
	$('.block-work .excerpt a').click( function(e){
		$(this).parent().parent().next().toggle('fast').css;
		e.stopPropagation();
	});
	$('html').click(function(e){
		if(e.target.className != 'full-content')
			$('.full-content').hide();
	})
	$('.block-work .full-content button').click( function(){
		$(this).parent().hide();
	});
});
