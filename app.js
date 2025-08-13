(function(){
// Router simple para app.html
const menu = document.querySelectorAll('.menu a[data-view]');
const views = document.querySelectorAll('.view');
const title = document.getElementById('view-title');

function setActive(view){
views.forEach(v=>v.classList.remove('active'));
document.getElementById('view-'+view).classList.add('active');
menu.forEach(m=>m.classList.remove('active'));
document.querySelector('.menu a[data-view="'+view+'"]').classList.add('active');
title.textContent = view.charAt(0).toUpperCase()+view.slice(1);
history.replaceState(null, '', '#'+view);

// Inicializar componentes específicos por vista
if(view === 'dashboard') {
  initDashboard();
}
}

function initRoute(){
const hash = (location.hash||'#dashboard').replace('#','');
const exists = document.getElementById('view-'+hash);
setActive(exists ? hash : 'dashboard');
}

window.addEventListener('hashchange', initRoute);
menu.forEach(a=>a.addEventListener('click', ()=> setActive(a.dataset.view)));
initRoute();

// Funcionalidad específica del Dashboard
function initDashboard() {
// Animar contadores KPI
animateCounters();

// Inicializar gráfico simple
initSimpleChart();

// Animar barras de progreso
animateProgressBars();
}

function animateCounters() {
const counters = document.querySelectorAll('[data-animate="counter"]');
counters.forEach(counter => {
const valueEl = counter.querySelector('.kpi__value');
const target = parseInt(valueEl.dataset.target);
const isPayment = valueEl.textContent.includes('/');
  
let current = 0;
const increment = target / 50;
const timer = setInterval(() => {
  current += increment;
  if(current >= target) {
    current = target;
    clearInterval(timer);
  }
  
  if(isPayment) {
    valueEl.textContent = `${Math.floor(current)}/220`;
  } else {
    valueEl.textContent = `$${Math.floor(current).toLocaleString()}`;
  }
}, 30);
});
}

function initSimpleChart() {
const canvas = document.getElementById('cash-flow-chart');
if(!canvas) return;

const ctx = canvas.getContext('2d');
const width = canvas.width;
const height = canvas.height;

// Limpiar canvas
ctx.clearRect(0, 0, width, height);

// Datos de ejemplo
const data = [180, 220, 160, 240, 200, 280];
const labels = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'];

// Configuración
const padding = 40;
const chartWidth = width - 2 * padding;
const chartHeight = height - 2 * padding;
const barWidth = chartWidth / data.length * 0.6;
const maxValue = Math.max(...data);

// Estilo
ctx.fillStyle = getComputedStyle(document.body).getPropertyValue('--primary-solid').trim();
ctx.font = '12px Inter';

// Dibujar barras
data.forEach((value, index) => {
const barHeight = (value / maxValue) * chartHeight;
const x = padding + (index * chartWidth / data.length) + (chartWidth / data.length - barWidth) / 2;
const y = height - padding - barHeight;

// Barra con gradiente
const gradient = ctx.createLinearGradient(0, y, 0, y + barHeight);
gradient.addColorStop(0, '#8b654e');
gradient.addColorStop(1, '#a0734f');
ctx.fillStyle = gradient;

ctx.fillRect(x, y, barWidth, barHeight);

// Etiquetas
ctx.fillStyle = getComputedStyle(document.body).getPropertyValue('--sub').trim();
ctx.textAlign = 'center';
ctx.fillText(labels[index], x + barWidth/2, height - 10);
});
}

function animateProgressBars() {
// Animar barra de ocupación
const occupancyFill = document.querySelector('.occupancy-fill');
if(occupancyFill) {
setTimeout(() => {
  occupancyFill.style.width = occupancyFill.dataset.percentage + '%';
}, 500);
}

// Animar barras de categorías
const categoryFills = document.querySelectorAll('.category-fill');
categoryFills.forEach((fill, index) => {
setTimeout(() => {
  const width = fill.style.width;
  fill.style.width = width;
}, 200 * (index + 1));
});
}

// Función para refrescar actividad
window.refreshActivity = function() {
const refreshBtn = document.querySelector('[onclick="refreshActivity()"]');
const icon = refreshBtn.querySelector('.refresh-icon');
icon.style.transform = 'rotate(360deg)';

// Simular carga
setTimeout(() => {
icon.style.transform = 'rotate(0deg)';
toast('Actividad actualizada');
}, 500);
};

// Controles de gráfico
document.addEventListener('click', (e) => {
if(e.target.matches('[data-period]')) {
const buttons = document.querySelectorAll('[data-period]');
buttons.forEach(btn => btn.classList.remove('btn--primary'));
e.target.classList.add('btn--primary');
toast(`Vista cambiada a ${e.target.textContent}`);
}
});

// Tabs
document.querySelectorAll('.tabs').forEach(group=>{
const tabs = group.querySelectorAll('.tab');
tabs.forEach(tab=>{
tab.addEventListener('click', ()=>{
tabs.forEach(t=>t.classList.remove('active'));
group.parentElement.querySelectorAll('.tab__content').forEach(c=>c.classList.remove('active'));
tab.classList.add('active');
const id = tab.dataset.tab;
const content = group.parentElement.querySelector('#tab-'+id);
if(content) {
  content.classList.add('active');
  
  // Reactivar animaciones cuando se muestra el tab
  if(id === 'categorias') {
    setTimeout(() => animateProgressBars(), 100);
  }
}
});
});
});

// Modal helpers
window.openModal = id => {
const el = document.getElementById(id);
el.style.display = 'flex';
el.setAttribute('aria-hidden','false');
};
window.closeModal = id => {
const el = document.getElementById(id);
el.style.display = 'none';
el.setAttribute('aria-hidden','true');
};

// Toast
const toastEl = document.getElementById('toast');
window.toast = (msg) => {
toastEl.textContent = msg;
toastEl.style.display = 'block';
setTimeout(()=> toastEl.style.display = 'none', 2000);
};

// Demo add row to table
window.demoAddRow = (tableId) => {
const t = document.getElementById(tableId).querySelector('tbody');
const now = new Date().toISOString().slice(0,10);
const desc = document.querySelector('#view-gastos input[placeholder="Descripción"]').value || 'Gasto demo';
const monto = document.querySelector('#view-gastos input[type="number"]').value || '0';
const cat = document.querySelector('#view-gastos select').value;
const tr = document.createElement('tr');
tr.innerHTML = `<td>${now}</td><td>${desc}</td><td>${cat}</td><td>$${monto}</td>`;
t.prepend(tr);
toast('Gasto agregado (mock)');
};

// Demo add card negocio
window.demoAddCard = () => {
const grid = document.getElementById('negocios-grid');
const inputs = document.querySelectorAll('#view-negocios .form-row input');
const [nombre,cat,contacto] = Array.from(inputs).map(i=>i.value);
const div = document.createElement('div');
div.className='card';
div.innerHTML = `<h3>${nombre||'Negocio demo'}</h3><p>${cat||'Servicio'}</p><small>${contacto||''}</small>`;
grid.prepend(div);
toast('Negocio publicado (mock)');
};

// Theme toggle
const toggle = document.getElementById('toggleTheme');
if(toggle){
toggle.addEventListener('click', ()=>{
document.body.classList.toggle('light');
localStorage.setItem('theme', document.body.classList.contains('light') ? 'light' : 'dark');
});

// Cargar tema guardado
const savedTheme = localStorage.getItem('theme');
if(savedTheme === 'light') {
document.body.classList.add('light');
}
}

// Efectos de hover para mejorar interactividad
document.addEventListener('mouseover', (e) => {
if(e.target.matches('.kpi')) {
e.target.style.transform = 'translateY(-2px)';
}
});

document.addEventListener('mouseout', (e) => {
if(e.target.matches('.kpi')) {
e.target.style.transform = 'translateY(0)';
}
});

})();