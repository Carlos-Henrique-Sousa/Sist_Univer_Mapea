from django.db import models

# Create your models here.

class Escola(models.Model):
  cnpj = models.CharField(max_length=16, unique=True)
  nome = models.CharField(max_length=255, unique=True)
  email = models.EmailField(unique=True)
  senha = models.CharField(max_length=255)

  def __str__(self):
      return self.nome

class Turma(models.Model):
  escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
  nome = models.CharField(max_length=50)
  ano = models.IntegerField()

  def __str__(self):
      return f"{self.nome} - {self.ano}°"

class Professor(models.Model):
  nome = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  senha = models.CharField(max_length=255)
  escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

  def __str__(self):
      return self.nome
  
class PDT(models.Model):
  professor = models.OneToOneField(Professor, on_delete=models.CASCADE)
  turma = models.OneToOneField(Turma, on_delete=models.CASCADE)

  def __str__(self):
      return f"PDT: {self.Professor.nome} - Turma: {self.turma.nome}"
  
class Aluno(models.Model):
  nome = models.CharField(max_length=255)
  email =  models.EmailField(unique=True)
  senha = models.CharField(max_length=255)
  turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
  dificuldade_visao = models.IntegerField(choices=[(0, "Normal"), (1, "Leve"), (2, "Moderada"), (3, "Severa")])
  media_humanas = models.FloatField()
  media_exatas = models.FloatField()
  media_linguagens = models.FloatField()
  foto = models.ImageField(upload_to="alunos_fotos/", blank=True, null=True)

  def __str__(self):
      return self.nome

class Mapeamento(models.Model):
    turma = models.OneToOneField(Turma, on_delete=models.CASCADE)
    filas = models.IntegerField()
    colunas = models.IntegerField()
    tipo_agrupamento = models.CharField(
        max_length=10,
        choices=[("sozinho", "Sozinho"), ("dupla", "Dupla"), ("trio", "Trio")]
    )

    def __str__(self):
        return f"Mapeamento da turma {self.turma.nome}"

class PosicaoAluno(models.Model):
    mapeamento = models.ForeignKey(Mapeamento, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    fila = models.IntegerField()
    coluna = models.IntegerField()

    def __str__(self):
        return f"{self.aluno.nome} na posição ({self.fila}, {self.coluna})"


class Notas(models.Model):
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
  materia = models.CharField(max_length=100)
  global_nota = models.FloatField()
  parcial1_nota = models.FloatField(null=True, blank=True)
  parcial2_nota = models.FloatField(null=True, blank=True)
  
  def __str__(self):
     return f"{self.aluno.nome} - {self.materia}"
   
   
class Falta(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    aula = models.CharField(max_length=100)
    justificativa = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.aluno.nome} - {self.data} - {self.aula}"
  

class EventoEscolar(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=255)
    capa = models.ImageField(upload_to="evento_capa/", blank=True, null=True)
    
    def __str__(self):
       return self.titulo
   
class ProfessorCurso(models.Model):
    professor = models.OneToOneField(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.professor
   
class MaterialDeEstudo(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='materiais/', blank=True, null=True)  

    def __str__(self):
        return self.titulo

class Atividade(models.Model):
    professor = models.ForeignKey(ProfessorCurso, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_entrega = models.DateTimeField()

    def __str__(self):
        return self.titulo
 