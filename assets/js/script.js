//Block Hovering
$(function(){
	$('.block-work').hover(
		function(){//Hover in
		$(this).find('.hover').slideDown('slow');
		},
		function(){//Hover out
		$(this).find('.hover').slideUp('slow');
		});
});
