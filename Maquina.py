
#classe principal da Maquina de Turing Universal
class Maquina():
	#descritor para vizualizar fitas
	def __str__(self):
		out = ""
		out += ("FITA 1 [REGRAS]:\n" + str(self.fitaR) + "\n\nFITA 2 [ESTADO_ATUAL]:\n" + str(self.fitaI) 
			+ "\n\nFITA 3 [PALAVRA]:\n" + str(self.fitaP) + "\n\n")
		return out
		
	def __init__(self, regras, palavra):
		self.fitaR = regras 	  #fitaR contém nossa lista regras/
		self.fitaI = "1"		  #fitaI contém nosso estado inicial
		self.fitaP = palavra      #fitaP contém nossa palavra
		self.lista_transicoes = [Transicao(tran) for tran in regras]# Contém a lista dos objetos em
		self.cabess_maquina = 0   #controla a posicao do cabeçote para leitura e escrita										
		self.D = "1"              #Direcoes da maquina apenas para facilitar implementacao
		self.E = "11"
		self.REJEITA = "\nPalavra rejeitada\n" #mensagens na saida
		self.ACEITA = "\nPalavra aceita\n"
		self.ultima_transicao = []#Transicao que usa heuristia
