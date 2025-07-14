const letras = ['A', 'B', 'C', 'D'];
const cartas = [...letras, ...letras]; // 4 pares = 8 cartas
cartas.sort(() => 0.5 - Math.random());

const tabuleiro = document.getElementById('game-board');
let primeiraCarta = null;
let bloqueiaClique = false;

cartas.forEach(letra => {
  const carta = document.createElement('div');
  carta.className = 'card';
  carta.innerHTML = `
    <div class="card-inner">
      <div class="card-front">?</div>
      <div class="card-back">
        <img src="/static/img/libras/${letra.toUpperCase()}.png" alt="${letra}">
      </div>
    </div>
  `;
  carta.dataset.letra = letra;
  carta.addEventListener('click', () => {
    if (bloqueiaClique || carta.classList.contains('flipped')) return;

    carta.classList.add('flipped');
    if (!primeiraCarta) {
      primeiraCarta = carta;
    } else {
      if (carta.dataset.letra === primeiraCarta.dataset.letra) {
        primeiraCarta = null;
      } else {
        bloqueiaClique = true;
        setTimeout(() => {
          carta.classList.remove('flipped');
          primeiraCarta.classList.remove('flipped');
          primeiraCarta = null;
          bloqueiaClique = false;
        }, 1000);
      }
    }
  });
  tabuleiro.appendChild(carta);
});
