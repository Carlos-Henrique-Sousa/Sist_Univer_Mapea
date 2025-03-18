import torch
from classical_nn import neuralNet
from .quantum_circuit import Processamento_quantico
from transformers import pipeline

modelo_npl = pipeline("text-generation", model="gpt4")

class QuantumAI:
  def __init__(self):
    self.rede_neural = neuralNet()
    
  def analisar_aluno(self, alunos):
    """Alalisar a media das notas dos alunos e a dificuldade de visão, e a internet como um todo para personalizar a resposta"""
    analise = []
    for aluno in alunos:
      descricao = f"{aluno['nome']} com as medias {media_humanas} em humanas, {media_linguagens} em linguagens e  com a media {media_exatas} em exatas"
      analise.append(descricao)
      
      return "".join(analise)
    
  def gerar_resposta(self, prompt, alunos):
    dados_alunos = self.analisar_alunos(alunos)
    interpretacao = modelo_nlp(f"Baseado nos alunos: {dados_alunos}. {prompt}", max_length=100)[0]["generated_text"]
        
    resultado_quantico = processar_quantico([0.5, 0.8])

    return {
        "interpretacao": interpretacao,
        "resultado_quantico": resultado_quantico
    }