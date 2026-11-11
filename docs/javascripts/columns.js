/* Скрытие столбцов стран в матрицах: выбор запоминается в браузере */
(function () {
  var KEYS = [['Россия', 'Россия', 'Russia'], ['Сербия', 'Сербия', 'Serbia'], ['ЕС', 'ЕС', 'EU'], ['Англия', 'Англия', 'England'], ['ОАЭ', 'ОАЭ', 'UAE'], ['Грузия', 'Грузия', 'Georgia'], ['Индия', 'Индия', 'India']];
  var EN = document.documentElement.lang === 'en';
  var LS = 'hidden-country-cols';
  function load() { try { return JSON.parse(localStorage.getItem(LS) || '[]'); } catch (e) { return []; } }
  function save(v) { try { localStorage.setItem(LS, JSON.stringify(v)); } catch (e) {} }
  function colOf(th) {
    var t = th.textContent;
    for (var i = 0; i < KEYS.length; i++) if (t.indexOf(KEYS[i][0]) >= 0 || t.indexOf(KEYS[i][2]) >= 0) return KEYS[i][0];
    return null;
  }
  function apply(hidden) {
    document.querySelectorAll('.matrix table').forEach(function (tb) {
      var ths = tb.querySelectorAll('thead th');
      ths.forEach(function (th, idx) {
        var k = colOf(th); if (!k) return;
        var off = hidden.indexOf(k) >= 0;
        tb.querySelectorAll('tr').forEach(function (tr) {
          var c = tr.children[idx]; if (c) c.style.display = off ? 'none' : '';
        });
      });
    });
  }
  function init() {
    var tables = document.querySelectorAll('.matrix table');
    if (!tables.length) return;
    var present = {};
    tables.forEach(function (tb) { tb.querySelectorAll('thead th').forEach(function (th) { var k = colOf(th); if (k) present[k] = 1; }); });
    var names = KEYS.filter(function (k) { return present[k[0]]; });
    if (names.length < 2) return;
    var hidden = load();
    var box = document.createElement('div');
    box.className = 'col-toggle';
    box.appendChild(document.createTextNode(EN ? 'Show columns: ' : 'Показать столбцы: '));
    names.forEach(function (k) {
      var lab = document.createElement('label');
      var cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = hidden.indexOf(k[0]) < 0;
      cb.addEventListener('change', function () {
        var h = load().filter(function (x) { return x !== k[0]; });
        if (!cb.checked) h.push(k[0]);
        save(h); apply(h);
        document.querySelectorAll('.col-toggle input').forEach(function (o) { if (o.dataset.k === k[0]) o.checked = cb.checked; });
      });
      cb.dataset.k = k[0];
      lab.appendChild(cb); lab.appendChild(document.createTextNode(' ' + (EN ? k[2] : k[1])));
      box.appendChild(lab);
    });
    tables.forEach(function (tb) {
      var host = tb.closest('.matrix');
      if (!host) return;
      var prev = host.previousElementSibling;
      if (!prev || !prev.classList.contains('col-toggle')) host.parentNode.insertBefore(box.cloneNode(true), host);
    });
    // клонированные элементы теряют обработчики — навешиваем заново
    document.querySelectorAll('.col-toggle').forEach(function (b) {
      b.querySelectorAll('input').forEach(function (cb) {
        var key = cb.dataset.k;
        cb.checked = hidden.indexOf(key) < 0;
        cb.addEventListener('change', function () {
          var h = load().filter(function (x) { return x !== key; });
          if (!cb.checked) h.push(key);
          save(h); apply(h);
          document.querySelectorAll('.col-toggle input').forEach(function (o) { if (o.dataset.k === key) o.checked = cb.checked; });
        });
      });
    });
    apply(hidden);
  }
  // клик по плашке ведёт по ссылке «Далее»
  document.addEventListener('click', function (ev) {
    if (ev.target.closest('a')) return;
    var td = ev.target.closest('td');
    var more = td && td.querySelector('a.more');
    if (more) window.location.href = more.href;
  });
  // явный переключатель языка RU | EN в шапке (ссылки берём из выпадающего списка Material)
  function langSwitch() {
    var links = document.querySelectorAll('.md-header__option .md-select__link');
    var inner = document.querySelector('.md-header__inner');
    if (!links.length || !inner || document.querySelector('.lang-switch')) return;
    var box = document.createElement('div'); box.className = 'lang-switch';
    links.forEach(function (l) {
      var a = document.createElement('a'); a.href = l.href; a.textContent = l.textContent.trim().toUpperCase();
      if (l.getAttribute('hreflang') === document.documentElement.lang || (l.getAttribute('lang') === document.documentElement.lang)) a.className = 'active';
      box.appendChild(a);
    });
    var search = inner.querySelector('.md-search') || inner.lastChild;
    inner.insertBefore(box, search);
  }
  document.addEventListener('DOMContentLoaded', langSwitch);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
