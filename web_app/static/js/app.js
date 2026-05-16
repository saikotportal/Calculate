const numA = document.getElementById('numA');
const numB = document.getElementById('numB');
const resultEl = document.getElementById('result');
const expressionEl = document.getElementById('expression');
const historyList = document.getElementById('historyList');
const clearBtn = document.getElementById('clearHistory');

const SYMBOLS = {
  add: '+',
  subtract: '−',
  multiply: '×',
  divide: '÷',
  power: '^',
  modulo: '%',
};

window.addEventListener('DOMContentLoaded', loadHistory);

document.querySelectorAll('.op-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const op = btn.dataset.op;
    const a = numA.value.trim();
    const b = numB.value.trim();

    if (a === '' || b === '') {
      showError('Please enter both numbers.');
      return;
    }

    document.querySelectorAll('.op-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    setTimeout(() => btn.classList.remove('active'), 300);

    calculate(op, a, b);
  });
});

clearBtn.addEventListener('click', async () => {
  await fetch('/history', { method: 'DELETE' });
  renderHistory([]);
});

async function calculate(operation, a, b) {
  try {
    const res = await fetch('/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ operation, a, b }),
    });

    const data = await res.json();

    if (data.error) {
      showError(data.error);
      return;
    }

    const sym = SYMBOLS[operation];
    expressionEl.textContent = `${a} ${sym} ${b}`;
    resultEl.textContent = formatNumber(data.result);
    resultEl.classList.remove('error');
    renderHistory(data.history);
  } catch (err) {
    showError('Network error. Is the server running?');
  }
}

async function loadHistory() {
  try {
    const res = await fetch('/history');
    const data = await res.json();
    renderHistory(data.history || []);
  } catch (_) {}
}

function renderHistory(history) {
  if (!history.length) {
    historyList.innerHTML = '<li class="empty">No calculations yet.</li>';
    return;
  }
  historyList.innerHTML = '';
  [...history].reverse().forEach(entry => {
    const li = document.createElement('li');
    li.textContent = entry;
    historyList.appendChild(li);
  });
}

function showError(msg) {
  expressionEl.textContent = 'Error';
  resultEl.textContent = msg;
  resultEl.classList.add('error');
}

function formatNumber(n) {
  if (Number.isInteger(n)) return n.toString();
  return parseFloat(n.toPrecision(10)).toString();
}
