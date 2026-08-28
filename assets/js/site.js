/* Maalik Creative Engineers — site behaviour
   Progressive enhancement only: every page works with JS disabled. */
(function () {
  'use strict';

  /* ---- sticky header compression ---- */
  var t = false;
  function onScroll() {
    document.body.classList.toggle('scrolled', window.scrollY > 40);
    t = false;
  }
  window.addEventListener('scroll', function () {
    if (!t) { t = true; window.requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  /* ---- mega menu: hover on pointer devices, tap on touch ---- */
  document.querySelectorAll('.has-mega').forEach(function (li) {
    var link = li.querySelector('.nav-link');
    var mega = li.querySelector('.mega');
    if (!link || !mega) return;
    link.addEventListener('click', function (e) {
      if (window.matchMedia('(hover:hover)').matches) return;
      e.preventDefault();
      var open = mega.classList.contains('open');
      document.querySelectorAll('.mega.open').forEach(function (m) { m.classList.remove('open'); });
      if (!open) mega.classList.add('open');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.has-mega')) {
      document.querySelectorAll('.mega.open').forEach(function (m) { m.classList.remove('open'); });
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.mega.open').forEach(function (m) { m.classList.remove('open'); });
      closeMobile();
    }
  });

  /* ---- mobile navigation ---- */
  var mnav = document.querySelector('.mobile-nav');
  function closeMobile() {
    if (mnav) { mnav.classList.remove('open'); document.body.style.overflow = ''; }
  }
  var burger = document.querySelector('.burger');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      mnav.classList.add('open'); document.body.style.overflow = 'hidden';
    });
  }
  var mclose = document.querySelector('.mn-close');
  if (mclose) mclose.addEventListener('click', closeMobile);

  document.querySelectorAll('.acc-h').forEach(function (b) {
    b.addEventListener('click', function () { b.parentElement.classList.toggle('open'); });
  });

  /* ---- reveal on scroll ---- */
  var rv = document.querySelectorAll('.rv');
  if (rv.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    rv.forEach(function (el) { io.observe(el); });
  } else {
    rv.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---- product index filtering (shareable URLs, Section 4.5) ---- */
  var index = document.querySelector('[data-index]');
  if (index) {
    var items = Array.prototype.slice.call(index.querySelectorAll('[data-item]'));
    var countEl = document.querySelector('[data-count]');
    var emptyEl = document.querySelector('[data-empty]');
    var search = document.querySelector('[data-search]');
    var state = {};

    function readURL() {
      var p = new URLSearchParams(location.search);
      ['domain', 'platform', 'environment', 'function', 'manufacturer'].forEach(function (k) {
        state[k] = p.get(k) || '';
      });
      if (search) search.value = p.get('q') || '';
    }
    function writeURL() {
      var p = new URLSearchParams();
      Object.keys(state).forEach(function (k) { if (state[k]) p.set(k, state[k]); });
      if (search && search.value.trim()) p.set('q', search.value.trim());
      var qs = p.toString();
      history.replaceState(null, '', qs ? location.pathname + '?' + qs : location.pathname);
    }
    function apply() {
      var q = search ? search.value.trim().toLowerCase() : '';
      var shown = 0;
      items.forEach(function (el) {
        var ok = true;
        Object.keys(state).forEach(function (k) {
          if (!state[k]) return;
          var v = el.getAttribute('data-' + k) || '';
          if (v.split('|').indexOf(state[k]) === -1) ok = false;
        });
        if (ok && q) {
          ok = (el.getAttribute('data-search') || '').toLowerCase().indexOf(q) !== -1;
        }
        el.classList.toggle('hide', !ok);
        if (ok) shown++;
      });
      if (countEl) countEl.textContent = shown;
      if (emptyEl) emptyEl.classList.toggle('hide', shown !== 0);
      document.querySelectorAll('[data-facet]').forEach(function (c) {
        var k = c.getAttribute('data-facet'), v = c.getAttribute('data-value') || '';
        c.classList.toggle('on', (state[k] || '') === v);
      });
      writeURL();
    }
    document.querySelectorAll('[data-facet]').forEach(function (c) {
      c.addEventListener('click', function () {
        var k = c.getAttribute('data-facet'), v = c.getAttribute('data-value') || '';
        state[k] = (state[k] === v) ? '' : v;
        apply();
      });
    });
    if (search) search.addEventListener('input', apply);
    var reset = document.querySelector('[data-reset]');
    if (reset) reset.addEventListener('click', function () {
      Object.keys(state).forEach(function (k) { state[k] = ''; });
      if (search) search.value = '';
      apply();
    });
    readURL();
    apply();
  }

  /* ---- generic list filtering (partners, insights) ---- */
  document.querySelectorAll('[data-listfilter]').forEach(function (root) {
    var key = root.getAttribute('data-listfilter');
    var items = root.querySelectorAll('[data-' + key + ']');
    root.querySelectorAll('[data-lf]').forEach(function (c) {
      c.addEventListener('click', function () {
        var v = c.getAttribute('data-lf');
        root.querySelectorAll('[data-lf]').forEach(function (x) { x.classList.remove('on'); });
        c.classList.add('on');
        items.forEach(function (el) {
          var val = el.getAttribute('data-' + key) || '';
          el.classList.toggle('hide', !!v && val.split('|').indexOf(v) === -1);
        });
      });
    });
  });

  /* ---- forms -------------------------------------------------------
     Everything posts to one serverless route, which verifies the captcha,
     scans any attachment and delivers to info@maaliksoft.com. */
  function fieldValues(form) {
    var out = {};
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === 'file' || el.type === 'submit') return;
      out[el.name] = el.value;
    });
    return out;
  }

  function readFile(input) {
    return new Promise(function (resolve, reject) {
      var f = input && input.files && input.files[0];
      if (!f) return resolve(null);
      if (f.size > 25 * 1024 * 1024) {
        return reject(new Error('That file is over the 25 MB limit.'));
      }
      var r = new FileReader();
      r.onload = function () { resolve({ name: f.name, data: r.result }); };
      r.onerror = function () { reject(new Error('That file could not be read.')); };
      r.readAsDataURL(f);
    });
  }

  function setStatus(form, text, kind) {
    var box = form.querySelector('[data-form-status]');
    if (!box) return;
    box.textContent = text || '';
    box.className = 'form-status' + (kind ? ' is-' + kind : '');
  }

  document.querySelectorAll('form[data-form]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.checkValidity()) { f.reportValidity(); return; }

      var btn = f.querySelector('button[type=submit]');
      var label = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.innerHTML = 'Sending&hellip;'; }
      setStatus(f, '', '');

      readFile(f.querySelector('input[type=file]')).then(function (file) {
        var payload = fieldValues(f);
        payload.route = f.getAttribute('data-form') || 'General enquiry';
        payload.captcha_token =
          (f.querySelector('[name="cf-turnstile-response"]') || {}).value || '';
        if (file) payload.file = file;
        return fetch('/api/enquiry', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }).then(function (res) {
        return res.json().then(function (j) { return { ok: res.ok && j.ok, body: j }; });
      }).then(function (r) {
        if (btn) { btn.disabled = false; btn.innerHTML = label; }
        if (window.turnstile) { try { window.turnstile.reset(); } catch (err) {} }
        if (!r.ok) {
          setStatus(f, r.body && r.body.error
            ? r.body.error
            : 'The message could not be sent. Email info@maaliksoft.com directly.', 'error');
          return;
        }
        var ok = f.parentElement.querySelector('.form-ok');
        if (ok) { ok.classList.add('show'); ok.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
        f.reset();
      }).catch(function (err) {
        if (btn) { btn.disabled = false; btn.innerHTML = label; }
        setStatus(f, err && err.message
          ? err.message
          : 'The message could not be sent. Email info@maaliksoft.com directly.', 'error');
      });
    });
  });

  /* ---- expandable model tables on small screens ---- */
  document.querySelectorAll('[data-expand]').forEach(function (b) {
    var target = document.querySelector(b.getAttribute('data-expand'));
    if (!target) return;
    b.addEventListener('click', function () {
      var open = target.classList.toggle('is-open');
      target.querySelectorAll('tr.extra').forEach(function (r) { r.classList.toggle('hide', !open); });
      b.querySelector('span').textContent = open ? 'Show fewer' : b.getAttribute('data-label');
    });
  });


  /* ---- colour theme -------------------------------------------------
     Stored choice wins; with nothing stored the page follows the
     operating system, which is why no attribute is set by default. */
  var KEY = 'mce-theme';
  function systemTheme() {
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }
  function currentTheme() {
    return document.documentElement.getAttribute('data-theme') || systemTheme();
  }
  function applyTheme(next, animate) {
    var root = document.documentElement;
    if (animate) {
      root.classList.add('theme-anim');
      window.setTimeout(function () { root.classList.remove('theme-anim'); }, 420);
    }
    root.setAttribute('data-theme', next);
    try { localStorage.setItem(KEY, next); } catch (e) {}
    document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
      b.setAttribute('aria-label', next === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    });
  }
  document.querySelectorAll('[data-theme-toggle]').forEach(function (b) {
    b.setAttribute('aria-label', currentTheme() === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    b.addEventListener('click', function () {
      applyTheme(currentTheme() === 'light' ? 'dark' : 'light', true);
    });
  });
  /* Track the OS while the visitor has not made an explicit choice. */
  var mq = window.matchMedia('(prefers-color-scheme: light)');
  var onMq = function () {
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) {}
    if (stored !== 'light' && stored !== 'dark') {
      document.documentElement.removeAttribute('data-theme');
    }
  };
  if (mq.addEventListener) mq.addEventListener('change', onMq);
  else if (mq.addListener) mq.addListener(onMq);


  /* ---- hero video ---- */
  document.querySelectorAll('.hero-video').forEach(function (v) {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      v.removeAttribute('autoplay'); v.pause(); v.remove(); return;
    }
    v.autoplay = false;
    v.pause();
    var hero = v.closest('.hero');
    v.addEventListener('playing', function () {
      if (v.parentElement) v.parentElement.classList.add('is-playing');
    });
    if (hero) {
      hero.addEventListener('mouseenter', function () {
        var p = v.play();
        if (p && p.catch) p.catch(function () { v.remove(); });
      });
      hero.addEventListener('mouseleave', function () {
        v.pause();
        if (v.parentElement) v.parentElement.classList.remove('is-playing');
      });
    }
  });

  /* ---- current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
