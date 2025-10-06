let answered = false;

    function checkAnswer(element, isCorrect) {
      if (answered) return;

      answered = true;
      if (isCorrect) {
        element.classList.add('correct');
        alert('✔️ Resposta correta!');
      } else {
        element.classList.add('wrong');
        alert('❌ Resposta errada!');
      }
    }