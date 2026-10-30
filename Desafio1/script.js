// script.js: Lógica, cálculos e tratamento de erro
let currentNum = '0';
let previousNum = '';
let currentOp = null;

function addNum(num) {
  if (currentNum === '0') currentNum = num;
  else currentNum += num;
  updateDisplay();
}

function setOp(op) {
  currentOp = op;
  previousNum = currentNum;
  currentNum = '0';
  updateDisplay();
}

function compute() {
  const n1 = parseFloat(previousNum);
  const n2 = parseFloat(currentNum);
  if (isNaN(n1) || isNaN(n2)) return;

  // TRATAMENTO DE DIVISÃO POR ZERO
  if (currentOp === '÷' && n2 === 0) {
    alert("❌ Erro: Não é possível dividir por zero!");
    clearAll();
    return;
  }

  let res = 0;
  if (currentOp === '+') res = n1 + n2;
  if (currentOp === '-') res = n1 - n2;
  if (currentOp === '×') res = n1 * n2;
  if (currentOp === '÷') res = n1 / n2;

  currentNum = res.toString();
  currentOp = null;
  previousNum = '';
  updateDisplay();
}

function clearAll() {
  currentNum = '0';
  previousNum = '';
  currentOp = null;
  updateDisplay();
}

function updateDisplay() {
  document.getElementById('current').innerText = currentNum;
  document.getElementById('previous').innerText = previousNum + (currentOp ? ' ' + currentOp : '');
}