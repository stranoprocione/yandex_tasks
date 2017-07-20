$(document).ready(function() {
	$('html').click(function(e){
		if (e.target.id == "button") {
			$('.main').css({"visibility":"hidden"});
			$('#counter').html(0);
			return;
		}
		if ($('.main').css("visibility") === "hidden") {
			var w = window.innerWidth - 100;
			var h = window.innerHeight - 100;
			var rT = Math.random()*h;
			var rL = Math.random()*w;
  			$('.main').css({"visibility":"visible", "margin-top":rT, "margin-left":rL});
		} else {
   			$('#counter').html(+$('#counter').html()+1);
		}
	});
	$('html').contextmenu(function() {
		$('#counter').html(0);
	});
});
