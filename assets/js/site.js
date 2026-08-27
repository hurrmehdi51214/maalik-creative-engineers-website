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

  /* ---- forms: no back end wired, confirm and preserve the enquiry ---- */
  document.querySelectorAll('form[data-form]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.checkValidity()) { f.reportValidity(); return; }
      var ok = f.parentElement.querySelector('.form-ok');
      if (ok) {
        ok.classList.add('show');
        ok.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      f.reset();
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

  /* ---- current year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
