/* Modernizr 2.7.1 (Custom Build) | MIT & BSD
 * Build: http://modernizr.com/download/#-svg-load
 */function searchFestivals(e){var t=new RegExp(e,"gi");$("div.festival").find("h2").each(function(){var e=$(this).text(),n=t.test(e),r=$(this).parents("div.festival");n?n&&r.show():r.hide()})}function showDetail(e){e.toggleClass("closed");e.toggleClass("opened");e.children("p.detail_prompt").children("i.icon").toggleClass("ion-ios7-plus-outline");e.children("p.detail_prompt").children("i.icon").toggleClass("ion-ios7-plus")}window.Modernizr=function(e,t,n){function r(e){p.cssText=e}function i(e,t){return r(prefixes.join(e+";")+(t||""))}function s(e,t){return typeof e===t}function o(e,t){return!!~(""+e).indexOf(t)}function u(e,t,r){for(var i in e){var o=t[e[i]];if(o!==n)return r===!1?e[i]:s(o,"function")?o.bind(r||t):o}return!1}var a="2.7.1",f={},l=t.documentElement,c="modernizr",h=t.createElement(c),p=h.style,d,v={}.toString,m={svg:"http://www.w3.org/2000/svg"},g={},y={},b={},w=[],E=w.slice,S,x={}.hasOwnProperty,T;!s(x,"undefined")&&!s(x.call,"undefined")?T=function(e,t){return x.call(e,t)}:T=function(e,t){return t in e&&s(e.constructor.prototype[t],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(e){var t=this;if(typeof t!="function")throw new TypeError;var n=E.call(arguments,1),r=function(){if(this instanceof r){var i=function(){};i.prototype=t.prototype;var s=new i,o=t.apply(s,n.concat(E.call(arguments)));return Object(o)===o?o:s}return t.apply(e,n.concat(E.call(arguments)))};return r}),g.svg=function(){return!!t.createElementNS&&!!t.createElementNS(m.svg,"svg").createSVGRect};for(var N in g)T(g,N)&&(S=N.toLowerCase(),f[S]=g[N](),w.push((f[S]?"":"no-")+S));return f.addTest=function(e,t){if(typeof e=="object")for(var r in e)T(e,r)&&f.addTest(r,e[r]);else{e=e.toLowerCase();if(f[e]!==n)return f;t=typeof t=="function"?t():t,typeof enableClasses!="undefined"&&enableClasses&&(l.className+=" "+(t?"":"no-")+e),f[e]=t}return f},r(""),h=d=null,f._version=a,f}(this,this.document),function(e,t,n){function r(e){return"[object Function]"==d.call(e)}function i(e){return"string"==typeof e}function s(){}function o(e){return!e||"loaded"==e||"complete"==e||"uninitialized"==e}function u(){var e=v.shift();m=1,e?e.t?h(function(){("c"==e.t?k.injectCss:k.injectJs)(e.s,0,e.a,e.x,e.e,1)},0):(e(),u()):m=0}function a(e,n,r,i,s,a,f){function l(t){if(!d&&o(c.readyState)&&(w.r=d=1,!m&&u(),c.onload=c.onreadystatechange=null,t)){"img"!=e&&h(function(){b.removeChild(c)},50);for(var r in T[n])T[n].hasOwnProperty(r)&&T[n][r].onload()}}var f=f||k.errorTimeout,c=t.createElement(e),d=0,g=0,w={t:r,s:n,e:s,a:a,x:f};1===T[n]&&(g=1,T[n]=[]),"object"==e?c.data=n:(c.src=n,c.type=e),c.width=c.height="0",c.onerror=c.onload=c.onreadystatechange=function(){l.call(this,g)},v.splice(i,0,w),"img"!=e&&(g||2===T[n]?(b.insertBefore(c,y?null:p),h(l,f)):T[n].push(c))}function f(e,t,n,r,s){return m=0,t=t||"j",i(e)?a("c"==t?E:w,e,t,this.i++,n,r,s):(v.splice(this.i++,0,e),1==v.length&&u()),this}function l(){var e=k;return e.loader={load:f,i:0},e}var c=t.documentElement,h=e.setTimeout,p=t.getElementsByTagName("script")[0],d={}.toString,v=[],m=0,g="MozAppearance"in c.style,y=g&&!!t.createRange().compareNode,b=y?c:p.parentNode,c=e.opera&&"[object Opera]"==d.call(e.opera),c=!!t.attachEvent&&!c,w=g?"object":c?"script":"img",E=c?"script":w,S=Array.isArray||function(e){return"[object Array]"==d.call(e)},x=[],T={},N={timeout:function(e,t){return t.length&&(e.timeout=t[0]),e}},C,k;k=function(e){function t(e){var e=e.split("!"),t=x.length,n=e.pop(),r=e.length,n={url:n,origUrl:n,prefixes:e},i,s,o;for(s=0;s<r;s++)o=e[s].split("="),(i=N[o.shift()])&&(n=i(n,o));for(s=0;s<t;s++)n=x[s](n);return n}function o(e,i,s,o,u){var a=t(e),f=a.autoCallback;a.url.split(".").pop().split("?").shift(),a.bypass||(i&&(i=r(i)?i:i[e]||i[o]||i[e.split("/").pop().split("?")[0]]),a.instead?a.instead(e,i,s,o,u):(T[a.url]?a.noexec=!0:T[a.url]=1,s.load(a.url,a.forceCSS||!a.forceJS&&"css"==a.url.split(".").pop().split("?").shift()?"c":n,a.noexec,a.attrs,a.timeout),(r(i)||r(f))&&s.load(function(){l(),i&&i(a.origUrl,u,o),f&&f(a.origUrl,u,o),T[a.url]=2})))}function u(e,t){function n(e,n){if(e){if(i(e))n||(f=function(){var e=[].slice.call(arguments);l.apply(this,e),c()}),o(e,f,t,0,u);else if(Object(e)===e)for(p in h=function(){var t=0,n;for(n in e)e.hasOwnProperty(n)&&t++;return t}(),e)e.hasOwnProperty(p)&&(!n&&!--h&&(r(f)?f=function(){var e=[].slice.call(arguments);l.apply(this,e),c()}:f[p]=function(e){return function(){var t=[].slice.call(arguments);e&&e.apply(this,t),c()}}(l[p])),o(e[p],f,t,p,u))}else!n&&c()}var u=!!e.test,a=e.load||e.both,f=e.callback||s,l=f,c=e.complete||s,h,p;n(u?e.yep:e.nope,!!a),a&&n(a)}var a,f,c=this.yepnope.loader;if(i(e))o(e,0,c,0);else if(S(e))for(a=0;a<e.length;a++)f=e[a],i(f)?o(f,0,c,0):S(f)?k(f):Object(f)===f&&u(f,c);else Object(e)===e&&u(e,c)},k.addPrefix=function(e,t){N[e]=t},k.addFilter=function(e){x.push(e)},k.errorTimeout=1e4,null==t.readyState&&t.addEventListener&&(t.readyState="loading",t.addEventListener("DOMContentLoaded",C=function(){t.removeEventListener("DOMContentLoaded",C,0),t.readyState="complete"},0)),e.yepnope=l(),e.yepnope.executeStack=u,e.yepnope.injectJs=function(e,n,r,i,a,f){var l=t.createElement("script"),c,d,i=i||k.errorTimeout;l.src=e;for(d in r)l.setAttribute(d,r[d]);n=f?u:n||s,l.onreadystatechange=l.onload=function(){!c&&o(l.readyState)&&(c=1,n(),l.onload=l.onreadystatechange=null)},h(function(){c||(c=1,n(1))},i),a?l.onload():p.parentNode.insertBefore(l,p)},e.yepnope.injectCss=function(e,n,r,i,o,a){var i=t.createElement("link"),f,n=a?u:n||s;i.href=e,i.rel="stylesheet",i.type="text/css";for(f in r)i.setAttribute(f,r[f]);o||(p.parentNode.insertBefore(i,p),h(n,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};Modernizr.load({test:Modernizr.svg,nope:["static/css/no-svg.css"]});var removed=!1;$("a#remove_past").click(function(e){var t=$("div.past");e.preventDefault();if(!removed){t.hide();removed=!0;$(this).text("Show Past Festivals")}else{t.show();removed=!1;$(this).text("Remove Past Festivals")}});var classical=!1,folk=!1,otherFests=$("div.folk"),classicalFests=$("div.classical");$("p#just_classical").click(function(e){if(!classical){classicalFests.show();otherFests.hide();classical=!0;folk=!1;$(this).addClass("active");$("p#everything_else").removeClass("active");$("p#all_fests").removeClass("active")}else{otherFests.show();classical=!1;$(this).removeClass("active");$("p#all_fests").addClass("active")}});$("p#everything_else").click(function(e){if(!folk){classicalFests.hide();otherFests.show();folk=!0;classical=!1;$(this).addClass("active");$("p#just_classical").removeClass("active");$("p#all_fests").removeClass("active")}else{classicalFests.show();folk=!1;$(this).removeClass("active");$("p#all_fests").addClass("active")}});$("p#all_fests").click(function(e){if(!$(this).hasClass("active")){$(this).addClass("active");$("p#just_classical").removeClass("active");$("p#everything_else").removeClass("active");classicalFests.show();otherFests.show();folk=!1;classical=!1}});$("form#search_for_festival").on("submit",function(e){var t=$(this).children("input").val();searchFestivals(t);$("#filters").hide();$("#reset_results").show();return!1});$("p#full_results").on("click",function(){var e=$("p#all_fests");searchFestivals("");$("#filters").show();$("#reset_results").hide();$("form#search_for_festival").children("input").val("");if(!e.hasClass("active")){e.addClass("active");$("p#just_classical").removeClass("active");$("p#everything_else").removeClass("active");classicalFests.show();otherFests.show();folk=!1;classical=!1}});$("form#search_for_festival button").on("click",function(){var e=$(this).parent().siblings("input").val();searchFestivals(e)});$("p.detail_prompt").on("click",function(){var e=$(this).parent();showDetail(e)});$("div.headline h2").on("click",function(){var e=$(this).parent().siblings(".detail");showDetail(e)});