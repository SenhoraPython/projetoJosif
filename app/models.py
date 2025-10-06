from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class PerfilUsuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Perfil de usuário")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuário"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, null=True, blank=True)  # <-- aqui
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(unique=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    perfil = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome



class Aula(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    video_aula = models.URLField(verbose_name="Link do Vídeo")
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"


class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    url_jogo = models.URLField(verbose_name="Link do Jogo")
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Jogo"
        verbose_name_plural = "Jogos"


class Progresso(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True, blank=True)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField()
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.aula or self.jogo}"

    class Meta:
        verbose_name = "Progresso"
        verbose_name_plural = "Progressos"


class Pergunta(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    texto = models.TextField()
    imagem_sinal = models.ImageField(upload_to="sinais/", null=True, blank=True)
    alternativa_correta = models.CharField(max_length=255)

    def __str__(self):
        return self.texto[:50]

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"


class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='alternativas')
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"


class Comentario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.aula.titulo}"

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

        

# class Contribuicao(models.Model):
#     nome = models.CharField(max_length=100)
#     email = models.EmailField()
#     tipo = models.CharField(max_length=50)
#     mensagem = models.TextField()
#     data_envio = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.nome} ({self.tipo})"