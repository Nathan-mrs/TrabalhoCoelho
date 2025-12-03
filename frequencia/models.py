from django.db import models

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
    
class frequencia(models.Model):
    aluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=False)

    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        return f"{self.aluno.nome} - {self.data} - {status}"
