/**
 * HTML5 + AJAX navigation for merenbach.com
 */

(function($) {
	"use strict";

	var isInited = false;

	function _isWindowHistorySupported() {
		return window.hasOwnProperty('history');
	}

	function isPushStateSupported() {
		return (_isWindowHistorySupported() && window.history.pushState);
	}

	function isReplaceStateSupported() {
		return (_isWindowHistorySupported() && window.history.replaceState);
	}

    /**
     * Push a new uri to the window history.  Does the following:
     *
     * - Replace the contents of the address bar with a new uri (supplied)
     * - Push a new state object to the top of the history with the following:
     *   - The current (soon-to-be-old) page uri
     *   - The current (soon-to-be-old) page title
     *
     * When (if) this state is popped, these will again replace the (then-current) state.
     *
     * @param uri
     *        the new uri to push.
     */
	function pushUriState(uri, title) {
		var oldUri = window.location.href;
        var oldTitle = document.title;
		if (isPushStateSupported() && isReplaceStateSupported()) {
			var stateObj = {uri: oldUri, title: oldTitle};
            // args to method: current state object, title (ignored), and (new) display uri
            if (isInited === true) {
                window.history.pushState(stateObj, '', uri);
            } else {
                window.history.replaceState(stateObj, '', uri);
            }
		}
	}

	/**
	 * @param state
	 *        the state of the event.
	 * @param isPopState
	 *        `true` if we are popping state, `false` otherwise.
	 */
	var ajaxLoadAssets = function(uri, isPopState) {
        if (isInited === true) {
			$.get(uri + '?requestType=xhr', function(text) {
                // var title = text.match("<title>(.*?)</title>")[0];
				var $parsed = $(text);
                var title = $parsed.filter('title').text();
                console.log("new title = " + title);

                $('.navbar-inner .nav').first().replaceWith($parsed.find('.navbar-inner .nav').first());
				// $('.navbar-search .search-query').replaceWith($parsed.find('.navbar-search .search-query'));
                // var $navbar = $('#navbar');
                // $navbar.filter('.active').first().removeClass('active');
                
                // var $newNavbar = $parsed.find('#navbar');
                // var newActive = $newNavbar.find('.active');
                // $navbar.filter()
                $('#breadcrumbs').replaceWith($parsed.find('#breadcrumbs'));
                $('#content').replaceWith($parsed.find('#content'));
                
    			if (isPopState !== true) {
    				pushUriState(uri, title);
                    document.title = title;
    			}
			});
            
		} else {
			pushUriState(uri, document.title);
		}
	};

	// Bind the pop state event to handle the back button
	$(window).bind('popstate', function(e) {
        var ev = e.originalEvent;
		if (isInited === true && ev.hasOwnProperty('state') && ev.state !== null) {
            ajaxLoadAssets(ev.state.uri, true/*, ev.state.title*/);
		}
	});
    
    // Rewrite all internal links
	$('a[href^="/"]').live('click', function(e) {
		e.preventDefault();
		ajaxLoadAssets($(this).prop('href'), false);
	});

    ajaxLoadAssets(window.location.href);
	isInited = true;
    // pushUriState('http://www.merenbach.dev/asd');

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
			if () {
				window.history.pushState(args, null, q); // pass args which has our data
			}
		}
	});*/

})(jQuery);
