const letras = ['A', 'B', 'C', 'D'];
const cartas = [...letras, ...letras]; // 4 pares = 8 cartas
cartas.sort(() => 0.5 - Math.random());

const tabuleiro = document.getElementById('game-board');
let primeiraCarta = null;
let bloqueiaClique = false;
let paresAcertados = 0;

cartas.forEach(letra => {
  const carta = document.createElement('div');
  carta.className = 'card';
  carta.innerHTML = `
    <div class="card-inner">
      <div class="card-front">?</div>
      <div class="card-back">
        <img src="/static/img/libras/${letra}.png" alt="${letra}">
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
        paresAcertados += 1;

        // Verifica se o jogador terminou o jogo
        if (paresAcertados === letras.length) {
          mostrarFogos();
        }
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


// Função para exibir animação de fogos e redirecionar depois
function mostrarFogos() {
  const fogos = document.createElement('div');
  fogos.style.position = 'fixed';
  fogos.style.top = 0;
  fogos.style.left = 0;
  fogos.style.width = '100%';
  fogos.style.height = '100%';
  fogos.style.pointerEvents = 'none';
  fogos.style.zIndex = 9999;
  document.body.appendChild(fogos);

  for (let i = 0; i < 100; i++) {
    const bola = document.createElement('div');
    bola.style.position = 'absolute';
    bola.style.width = '10px';
    bola.style.height = '10px';
    bola.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
    bola.style.borderRadius = '50%';
    bola.style.left = Math.random() * window.innerWidth + 'px';
    bola.style.top = Math.random() * window.innerHeight / 2 + 'px';
    bola.style.opacity = 1;
    bola.style.transition = 'transform 3s ease-out, opacity 3s linear';
    fogos.appendChild(bola);

    setTimeout(() => {
      bola.style.transform = `translateY(${Math.random() * 300 - 150}px) translateX(${(Math.random() - 0.5) * 300}px) scale(0.5)`;
      bola.style.opacity = 0;
    }, 100);
  }

  // Mostra fogos por 3 segundos, depois exibe mensagem e redireciona
  setTimeout(() => {
    fogos.remove();
    alert("🎉 Parabéns! Você completou o jogo!");
    window.location.href = "/"; // Redireciona para a página principal
  }, 3000);
}
