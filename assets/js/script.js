//Block Hovering
$(document).ready(function(){
	$('.block-work').hover(
		function(){//Hover in
		$(this).find('.hover').slideDown('slow');
		},
		function(){//Hover out
		$(this).find('.hover').slideUp('slow');
		});
	$('.block-work .excerpt a').click( function(){
		$(this).parent().parent().next().toggle('fast');
	});
});
