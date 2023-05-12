// ==================== horisontal.js ================
jQuery(function($){
	'use strict';

	$('.centered').each(function(){

		var $frame = $(this);
		var slideNum = $(this).data('slide');

		(function () {
			var $wrap  = $frame.parent();
	
			// Call Sly on frame
			$frame.sly({
				horizontal: 1,
				itemNav: 'centered',
				smart: 1,
				activateOn: 'click',
				mouseDragging: 1,
				touchDragging: 1,
				releaseSwing: 1,
				startAt: 0,
				scrollBar: $wrap.find('.scrollbar'),
				scrollBy: 1,
				speed: 300,
				elasticBounds: 1,
				easing: 'easeOutExpo',
				dragHandle: 1,
				dynamicHandle: 1,
				clickBar: 1,
	
				// Buttons
				prev: $wrap.find(`.prev[data-slide="${slideNum}"]`),
				next: $wrap.find(`.next[data-slide="${slideNum}"]`)
			});
		}());
	
	})
});