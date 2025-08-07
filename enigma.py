# %%
# Lista com os caracteres suportados
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z",
            "ç", " "]

# Dicionário que simula o refletor
refletor = {
    0: 14, 14: 0,
    1: 27, 27: 1,
    2: 20, 20: 2,
    3: 16, 16: 3,
    4: 12, 12: 4,
    5: 22, 22: 5,
    6: 9,   9: 6,
    7: 24, 24: 7,
    8: 13, 13: 8,
    10: 19, 19:10,
    11: 25, 25:11,
    15: 21, 21:15,
    17: 23, 23:17,
    18: 26, 26:18

}

roldana1 = []
roldana2 = []
roldana3 = []
mensagemd = []

# Cria as roldanas com base nas configurações informadas
def primeira_inicial(x):
    return [(i + x) % 28 for i in range(28)]

# Simula o giro das roldanas
def alterar_roldana(roldana):
  roldana = [0 if x == 27 else x + 1 for x in roldana]
  return roldana

# Solicita a configuração das roldanas
a = int(input("Digite a configuração da primeira roldana:"))
b = int(input("Digite a configuração da segunda roldana:"))
c = int(input("Digite a configuração da terceira roldana:"))

# Solicita a mensagem que será codificada ou decodificada
mensagemi = input("Digite a mensagem a ser codificada ou decodificada:")
roldana1 = primeira_inicial(a)
roldana2 = primeira_inicial(b)
roldana3 = primeira_inicial(c)


for letra in mensagemi:
  try:

    # Tenta encontrar o índice da letra no alfabeto (protege contra caracteres inválidos)
    i = alfabeto.index(letra.lower())
  except ValueError:
    # Se a letra não estiver no alfabeto, pula para a próxima
        continue

  # Caminho de ida pelos rotores
  entrada = i
  passo1 = roldana1[entrada]
  passo2 = roldana2[passo1]
  passo3 = roldana3[passo2]

  # Refletor redireciona o sinal
  refletido = refletor[passo3]

  # Caminho de volta pelos rotores (em ordem inversa)
  passo4 = roldana3.index(refletido)
  passo5 = roldana2.index(passo4)
  passo6 = roldana1.index(passo5)

  # Letra cifrada/decifrada é adicionada à mensagem final
  mensagemd.append(alfabeto[passo6])

  # Avanço das roldanas conforme o número de letras cifradas
  a += 1
  # Primeiro avanço da roldana1
  roldana1 = alterar_roldana(roldana1)
  if a == 14:

      # Avanço de roldana1 + roldana2 (como se fosse entalhe)
      roldana2 = alterar_roldana(roldana2)
  elif a == 28:

      # Avanço de todas as roldanas (rotação completa)
      roldana2 = alterar_roldana(roldana2)
      roldana3 = alterar_roldana(roldana3)
      a = 1

print("Mensagem codificada/decodificada:", "".join(mensagemd))


