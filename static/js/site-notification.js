var guardian = guardian || {};
guardian.r2 = guardian.r2 || {};
guardian.r2.identity = guardian.r2.identity || {};

guardian.r2.identity.siteNotification = (function() {
	var notice_name,
		noticebar = {
			container: null,
			content: null,
			notice: null
		},
		notices = {
			'cookie': 'This site uses cookies. By continuing to browse the site you are agreeing to our use of cookies. <a title="Read our privacy policy" href="http://www.guardian.co.uk/info/cookies">Find out more here</a>'
		},
		max_show_count = 2;

	/**
     * Set checking cookies, then show notification if criteria is met
     *
     * @param {String} notice_to_show The notice lookup name
     * @return {Boolean} Returns whether the notice was shown
     */
	function notify(notice_to_show) {
		var notice_shown = false;
		notice_name = notice_to_show;
		setCookies();

		if (shouldShowNotice()) {
			if (!noticebar.container) {
				createNoticebar();
			}

			showNotice();
			notice_shown = true;
		}

		return notice_shown;
	}

	/**
     * Set a session cookie and persistant cookie
     * These are later use to see if the user has seen the bar in a previous session
     * TODO - make this able to handle multiple notices
     */
	function setCookies() {
		var cookie_name = 'noticebar_' + notice_name,
			show_count = jQuery.cookie(cookie_name) ? parseInt(jQuery.cookie(cookie_name)) : 0;

		if (show_count < max_show_count) {
			jQuery.cookie(cookie_name, show_count, { expires: 365, path: '/' });
		}
	}

	/**
     * Add one to the times shown cookie
	 */
	function addShowCount() {
		var cookie_name = 'noticebar_' + notice_name,
		show_count = jQuery.cookie(cookie_name) ? parseInt(jQuery.cookie(cookie_name)) + 1 : 0;
		jQuery.cookie(cookie_name, show_count, { expires: 365, path: '/' });
	}

	/**
     * Check cookies to see if you should show the notice
     *
     * @return {Boolean} Whether to show the notice
     */
	function shouldShowNotice() {
		var shouldShowBar = (!(jQuery.cookie('closed_noticebar_' + notice_name) && jQuery.cookie('closed_noticebar_' + notice_name) === 'true'))
							&& (parseInt(jQuery.cookie('noticebar_' + notice_name)) < max_show_count);
		
		return shouldShowBar;
	}

	/**
     * Set the DOM for the noticebar and store it in the var
     */
	function createNoticebar() {
		var wrapper = jQuery('.wrap'),
			margin_top = '-' + wrapper.css('margin-bottom');
			noticebar.notice = jQuery('<span></span>');
			noticebar.content = jQuery('<div class="identity-noticebar-content"><span class="hide-bar">Hide</span></div>');
			noticebar.container = jQuery('<div class="identity-noticebar col-12 edge"></div>').css({ 'margin-top': margin_top });

		noticebar.content.prepend(noticebar.notice);
		noticebar.container.prepend(noticebar.content).hide();

		noticebar.container.delegate('.hide-bar', 'click', removeBar);

        wrapper.prepend(noticebar.container);
	}

	/**
     * Remove the noticebar from the DOM
     */
	function removeBar() {
		noticebar.container.remove();
		jQuery.cookie('closed_noticebar_' + notice_name, 'true', { expires: 365 });
	}

	/**
     * Grab notice from notices and show it
     */
	function showNotice() {
		noticebar.notice.html(notices[notice_name]);
		noticebar.container.show();
		addShowCount();
	}

	return {
		notify: notify
	}
})();

guardian.r2.identity.siteNotification.notify('cookie');