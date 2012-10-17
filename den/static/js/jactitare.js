

(function($) {
	"use strict";

	var isInited = false;
    // var domain = 'www.merenbach.dev'

	function isStateSupported() {
		return window.history;
	}

	function isPushStateSupported() {
		return (isStateSupported() && window.history.pushState);
	}

	function isReplaceStateSupported() {
		return (isStateSupported() && window.history.replaceState);
	}

	function isPopStateSupported() {
		return (isStateSupported() && window.history.popState);
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
	function pushUriState(uri) {
		var href = window.location.href;
		if (isPushStateSupported() && isReplaceStateSupported()) {
			var stateObj = {uri: href, title: document.title};
			if (isInited === true) {
                console.log("pushing state " + stateObj + " for uri " + uri);
				window.history.pushState(stateObj, '', uri);
			} else {
                console.log("replacing state " + stateObj + " for uri " + uri);
				window.history.replaceState(stateObj, '', uri);
			}
			// var stateChangeMethod = (isInited === true) ? window.history.pushState : window.history.replaceState;
			// stateChangeMethod({uri : window.location.href} /* current state object */, null /* title */, uri /* new display uri */);
		}
	}

	function internalLinkClicked(e) {
		console.log("internal link clicked");
		e.preventDefault();
		var href = $(this).prop('href');
		loadPaneRequest(href, false);
	};


	/**
	 * @param state
	 *        the state of the event.
	 * @param isPopState
	 *        `true` if we are popping state, `false` otherwise.
	 */
	var loadPaneRequest = function(uri, isPopState, title) {
        console.log("URI=" + uri);
        if (isInited === true/* && uri.indexOf(domain) !== -1*/) {
            // uri = uri.substring(uri.indexOf(domain) + domain.length);
            // console.log("NEW URI = " + uri);
            console.log("IS INITED; ispopstate = " + isPopState);
			$.get(uri + '?requestType=xhr', function(data) {
				var $parsed = $(data);
                var title = $parsed.filter('title').text();
                console.log("title = " + title);
                document.title = title;
				// $('.navbar-inner .nav').first().replaceWith($parsed.find('.navbar-inner .nav').first());
				// $('.navbar-search .search-query').replaceWith($parsed.find('.navbar-search .search-query'));
                $('#content').replaceWith($parsed.find('#content'));
			});
            
			if (isPopState !== true) {
				pushUriState(uri);
			} else if (title) {
                document.title = title;
			}
		} else {
			pushUriState(uri);
		}
	};


	// handle back button presses, the event.state object should have been
	// populated in refresh_panes() using the pushState
	function thisPopStateEvent(e) {
        var ev = e.originalEvent;
		if (isInited === true && ev.hasOwnProperty('state') && ev.state !== null) {
			loadPaneRequest(ev.state.uri, true, ev.state.title);
		}
	}


	$(window).bind('popstate', thisPopStateEvent);
	$('a[href^="/"]').live('click', internalLinkClicked);

    loadPaneRequest(window.location.href);
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
