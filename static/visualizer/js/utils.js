

$(document).ready(function(){
	$('.expandable').on('click', function  (e) {
		var ctnDiv =  $(this).closest('div');
		if(ctnDiv.hasClass('col-lg-6')){
			ctnDiv.removeClass('col-lg-6');
			ctnDiv.addClass('col-lg-12');
			$(this).removeClass('fa-expand');
			$(this).addClass('fa-compress');
		}else if (ctnDiv.hasClass('col-lg-12')) {
			ctnDiv.removeClass('col-lg-12');
			ctnDiv.addClass('col-lg-6');
			$(this).removeClass('fa-compress');
			$(this).addClass('fa-expand');
		};
	});
});