from rest_framework import viewsets
import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Escola, Turma, Professor, PDT, Aluno, Mapeamento, PosicaoAluno,
    Notas, Falta, EventoEscolar, ProfessorCurso, MaterialDeEstudo, Atividade
)
from .serializers import (
    EscolaSerializer, TurmaSerializer, ProfessorSerializer, PDTSerializer,
    AlunoSerializer, MapeamentoSerializer, PosicaoAlunoSerializer, NotasSerializer,
    FaltaSerializer, EventoEscolarSerializer, ProfessorCursoSerializer,
    MaterialDeEstudoSerializer, AtividadeSerializer
)

class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class PDTViewSet(viewsets.ModelViewSet):
    queryset = PDT.objects.all()
    serializer_class = PDTSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MapeamentoViewSet(viewsets.ModelViewSet):
    queryset = Mapeamento.objects.all()
    serializer_class = MapeamentoSerializer

class PosicaoAlunoViewSet(viewsets.ModelViewSet):
    queryset = PosicaoAluno.objects.all()
    serializer_class = PosicaoAlunoSerializer

class NotasViewSet(viewsets.ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer

class FaltaViewSet(viewsets.ModelViewSet):
    queryset = Falta.objects.all()
    serializer_class = FaltaSerializer

class EventoEscolarViewSet(viewsets.ModelViewSet):
    queryset = EventoEscolar.objects.all()
    serializer_class = EventoEscolarSerializer

class ProfessorCursoViewSet(viewsets.ModelViewSet):
    queryset = ProfessorCurso.objects.all()
    serializer_class = ProfessorCursoSerializer

class MaterialDeEstudoViewSet(viewsets.ModelViewSet):
    queryset = MaterialDeEstudo.objects.all()
    serializer_class = MaterialDeEstudoSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    
class QuantumOtmizationClass(APIView):
    def post(self, request):
        result = subprocess.run(
            ['dotnet', 'run', '--project', 'QuantumML'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode('utf-8')
        return Response({"Result":output})