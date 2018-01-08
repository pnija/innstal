/* To avoid CSS expressions while still supporting IE 7 and IE 6, use this script */
/* The script tag referencing this file must be placed before the ending body tag. */

/* Use conditional comments in order to target IE 7 and older:
	<!--[if lt IE 8]><!-->
	<script src="ie7/ie7.js"></script>
	<!--<![endif]-->
*/

(function() {
	function addIcon(el, entity) {
		var html = el.innerHTML;
		el.innerHTML = '<span style="font-family: \'icomoon\'">' + entity + '</span>' + html;
	}
	var icons = {
		'icon-history': '&#xe900;',
		'icon-business': '&#xe901;',
		'icon-file': '&#xe902;',
		'icon-settings-work-tool': '&#xe903;',
		'icon-twitter': '&#xe904;',
		'icon-fb-logo': '&#xe905;',
		'icon-google-plus': '&#xe906;',
		'icon-paper-plane': '&#xe907;',
		'icon-map-marker': '&#xe908;',
		'icon-envelop': '&#xe909;',
		'icon-user-1': '&#xe90a;',
		'icon-search': '&#xe90b;',
		'icon-eye': '&#xe90c;',
		'icon-left-arrow': '&#xe90d;',
		'icon-right-arrow': '&#xe90e;',
		'icon-user': '&#xe90f;',
		'icon-logout': '&#xe910;',
		'icon-home': '&#xe911;',
		'icon-game': '&#xe912;',
		'icon-reading': '&#xe913;',
		'0': 0
		},
		els = document.getElementsByTagName('*'),
		i, c, el;
	for (i = 0; ; i += 1) {
		el = els[i];
		if(!el) {
			break;
		}
		c = el.className;
		c = c.match(/icon-[^\s'"]+/);
		if (c && icons[c[0]]) {
			addIcon(el, icons[c[0]]);
		}
	}
}());
