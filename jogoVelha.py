import random
class JogoVelha:
  matriz = [["-",'-',"-"],["-",'-',"-"],["-", "-","-"]]
  def __init__(self):
    print("Jogo iniciado!!")

  def printar_velha(self):
    for l in range(len(JogoVelha.matriz)):
      for c in range(len(JogoVelha.matriz[l])):
        print(JogoVelha.matriz[l][c], end=" ")
      print()    
  
  def fazer_jogada(self,linha,coluna,figura):
     JogoVelha.matriz[linha][coluna] = figura
     return self.verifica_vencedor()

  def jogada_ia(self):
    linha = random.randint(0,2)
    coluna = random.randint(0,2)
    if(JogoVelha.matriz[linha][coluna] == '-'):
      JogoVelha.matriz[linha][coluna] = "o"
    else:
      self.jogada_ia()  
  
  def verifica_vencedor(self):
    continuar = "sim"
    aux = "n"
    if(JogoVelha.matriz[0][0] != '-' and JogoVelha.matriz[0][0] == JogoVelha.matriz[0][1] and JogoVelha.matriz[0][0] == JogoVelha.matriz[0][2]):
      print("Venceu!!")
      continuar = "nao"
    if(JogoVelha.matriz[0][0] != '-' and JogoVelha.matriz[0][0] == JogoVelha.matriz[1][0] and JogoVelha.matriz[0][0] == JogoVelha.matriz[2][0]):
      print("Venceu!!")
      continuar = "nao"
    if(JogoVelha.matriz[2][0] != '-' and JogoVelha.matriz[2][0] == JogoVelha.matriz[2][1] and JogoVelha.matriz[2][0] == JogoVelha.matriz[2][2]):
      print("Venceu!!")
      continuar = "nao"
    if(JogoVelha.matriz[2][2] != '-' and JogoVelha.matriz[2][2] == JogoVelha.matriz[1][2] and JogoVelha.matriz[2][2] == JogoVelha.matriz[0][2]):
      print("Venceu!!")
      continuar = "nao"
    if(JogoVelha.matriz[2][2] != '-' and JogoVelha.matriz[2][2] == JogoVelha.matriz[1][1] and JogoVelha.matriz[2][2] == JogoVelha.matriz[0][0]):
      print("Venceu!!")
      continuar = "nao"
    
    if(JogoVelha.matriz[2][0] != '-' and JogoVelha.matriz[2][0] == JogoVelha.matriz[1][1] and JogoVelha.matriz[2][0] == JogoVelha.matriz[0][2]):
      print("Venceu!!")
      continuar = "nao"

    if(JogoVelha.matriz[1][0] != '-' and JogoVelha.matriz[1][0] == JogoVelha.matriz[1][1] and JogoVelha.matriz[1][0] == JogoVelha.matriz[1][2]):
      print("Venceu!!")
      continuar = "nao"

    for l in range(len(JogoVelha.matriz)):
      for c in range(len(JogoVelha.matriz[l])):
        if(JogoVelha.matriz[l][c] == "-"):
          aux = "s"
      if(aux == "s"):
        pass
      else:
        continuar == "nao"
     

    return continuar

jogo_da_velha = JogoVelha()

jogo_da_velha.printar_velha()
continuar = "sim"
jogo_da_velha.jogada_ia()
while continuar == "sim":
  jogada = input("Informe a linha e a coluna que você quer jogar: ")
  fig = input("Qual figura o ou x? ")
  j = jogada.split(" ")
  jogo_da_velha.fazer_jogada(int(j[0]),int(j[1]),fig)
  jogo_da_velha.printar_velha()
  continuar = jogo_da_velha.verifica_vencedor()