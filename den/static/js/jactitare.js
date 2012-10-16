(function($) {

	$('a[href^="/"]').click(function(e) {
		e.preventDefault();
		var h = $(this).prop('href');
		$.get(h, function(data) {
			var $parsed = $(data);
			$('.navbar-inner .nav').first().replaceWith($parsed.find('.navbar-inner .nav').first());
			$('.navbar-search .search-query').replaceWith($parsed.find('.navbar-search .search-query'));
			$('#content').replaceWith($parsed.find('#content'));
		});
	});

	/*$.get(q + '&requestType=xhr', function(data) {
		var $parsed = $(data);
		$('#events_list_partial').replaceWith($parsed.find('#events_list_partial'));
		$('#list_title_partial').replaceWith($parsed.find('#list_title_partial'));
		$('#subscribe_link').replaceWith($parsed.find('#subscribe_link'));
		if (has_sidebar) {
			$('#calendar_grid_partial').replaceWith($parsed.find('#calendar_grid_partial'));
		}
		update_links();
		if (pop_state_event && has_sidebar) update_categories(args.categories); // check/uncheck boxes
		if (!pop_state_event) {
			if (args.hasOwnProperty('d')) {
				flash_day(args.d);
			}
			debug('pushing state', safe_stringify(args));
			if (window.history && window.history.pushState) {
				window.history.pushState(args, null, q); // pass args which has our data
			}
		}
	});*/

})(jQuery);
