$(function() {

	for (var i=1; i < len; i++){
		if (i < 10) {
			var src = '../static/images/pdxcg_0' +i+ '.jpg';
		} else {
			var src = '../static/images/pdxcg_' +i+ '.jpg';
		}
		$('.gallery').append('<li><img src="' + src + '" /></li>');
	}

	var $list = $('img');
	$list.on('click', function(e) {
		target = e.target;
		var srcPic = target.getAttribute('src');
		$('#image_show img').attr('src', srcPic);
		$('#image_show').toggleClass('display_none display_img');
	});
});