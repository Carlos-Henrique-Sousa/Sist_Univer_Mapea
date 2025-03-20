from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    EscolaViewSet, TurmaViewSet, ProfessorViewSet, PDTViewSet, AlunoViewSet,
    MapeamentoViewSet, PosicaoAlunoViewSet, NotasViewSet, FaltaViewSet,
    EventoEscolarViewSet, ProfessorCursoViewSet, MaterialDeEstudoViewSet, AtividadeViewSet
)

router = DefaultRouter()
router.register(r'escolas', EscolaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'pdt', PDTViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'mapeamentos', MapeamentoViewSet)
router.register(r'posicoes-aluno', PosicaoAlunoViewSet)
router.register(r'notas', NotasViewSet)
router.register(r'faltas', FaltaViewSet)
router.register(r'eventos', EventoEscolarViewSet)
router.register(r'professor-curso', ProfessorCursoViewSet)
router.register(r'materiais', MaterialDeEstudoViewSet)
router.register(r'atividades', AtividadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
