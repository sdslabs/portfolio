//Block Hovering
$('.block-work').hover(
	function(){//Hover in
	$(this).find('.hover').slideDown('slow');
	},
	function(){//Hover out
	$(this).find('.hover').slideUp('slow');
	});
$('.block-work .excerpt a').click( function(e){
	e.preventDefault();
	console.log('hi');
	$(this).parent().parent().next().toggle('fast');
});
