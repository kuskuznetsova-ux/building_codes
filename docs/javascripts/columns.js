/* Скрытие столбцов стран в матрицах: выбор запоминается в браузере */
(function () {
  var KEYS = [['Россия', '🇷🇺 Россия'], ['Сербия', '🇷🇸 Сербия'], ['ЕС', '🇪🇺 ЕС'], ['Англия', '🇬🇧 Англия'], ['ОАЭ', '🇦🇪 ОАЭ']];
  var LS = 'hidden-country-cols';
  function load() { try { return JSON.parse(localStorage.getItem(LS) || '[]'); } catch (e) { return []; } }
  function save(v) { try { localStorage.setItem(LS, JSON.stringify(v)); } catch (e) {} }
  function colOf(th) {
    var t = th.textContent;
    for (var i = 0; i < KEYS.length; i++) if (t.indexOf(KEYS[i][0]) >= 0) return KEYS[i][0];
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
    box.appendChild(document.createTextNode('Показать столбцы: '));
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
      lab.appendChild(cb); lab.appendChild(document.createTextNode(' ' + k[1]));
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
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
