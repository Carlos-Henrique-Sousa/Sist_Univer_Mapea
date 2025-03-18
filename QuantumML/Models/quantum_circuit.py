from qiskit import QuantumCircuit, Aer, execute

def Processamento_quantico(dados):
  """Executa um circuito quântico para processar probabilidades."""
  qc = QuantumCircuit(2, 2)
  
  if dados[0] > 0.5:
    qc.h(0)
  if dados[1] > 0.5:
    qc.x(1)
    
  qc.cx(0, 1)
  qc.measure([0, 1], [0,1])
  
  simulador = Aer.get_backend('qasm_simulator')
  resultado = execute(qc, backend=simulador, shots=1).result()
  contagem = resultado.get_counts()
  
  return list(contagem.keys()[0])