from rest_framework import serializers
from .models import (
    Escola, Turma, Professor, PDT, Aluno, Mapeamento, PosicaoAluno,
    Notas, Falta, EventoEscolar, ProfessorCurso, MaterialDeEstudo, Atividade
)

class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class PDTSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDT
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class MapeamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapeamento
        fields = '__all__'

class PosicaoAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosicaoAluno
        fields = '__all__'

class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'

class FaltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falta
        fields = '__all__'

class EventoEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoEscolar
        fields = '__all__'

class ProfessorCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorCurso
        fields = '__all__'

class MaterialDeEstudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialDeEstudo
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__'
