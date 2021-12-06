#Guilherme Da Costa Baesse
#Nathan Araújo Silva

#classe principal para representar a MTU
class Maquina():
	#descritor para visualizacao das fitas de regra, inical e palavras
	def __str__(self):
		out = ""
		out += ("FITA 1 [REGRAS]:\n" + str(self.fitaR) + "\n\nFITA 2 [ESTADO_ATUAL]:\n" + str(self.fitaI) 
			+ "\n\nFITA 3 [PALAVRA]:\n" + str(self.fitaP) + "\n\n")
		return out
		
	def __init__(self, regras, palavra):
		self.fitaR = regras 	  
		self.fitaI = "1"		 
		self.fitaP = palavra      
		self.lista_transicoes = [Transicao(tran) for tran in regras]
		self.cabeca_maquina = 0  										
		self.D = "1"             
		self.E = "11"
		self.ultima_transicao = []       

	def buscarTransicao(self):

		current_state = self.fitaI

		transicoes = [transicao for transicao in self.lista_transicoes if transicao.estado_inicial == current_state]
		
		if transicoes == []:
			return False, self.ultima_transicao
		
		#para todas possiveis transicoes partindo do estado atual, executar a que convem
		for transicao in transicoes:
			if transicao.simbolo_entrada == self.fitaP[self.cabeca_maquina]:
				try:
					self.ultima_transicao = transicao
					self.executarTransicao(transicao)
					return True, self.ultima_transicao
				except ErroMaquina:
					print("Palavra foi rejeitada")
					exit(0)
		
		print("Palavra foi rejeitada")
		exit(0)

	#realiza alteracoes nas fitas
	def executarTransicao(self, transicao):

		self.fitaI = transicao.estado_destino
		self.fitaP[self.cabeca_maquina] = transicao.simbolo_escrita
		if transicao.direcao == self.D:
			self.cabeca_maquina += 1
		else:
			self.cabeca_maquina -= 1
			if self.cabeca_maquina < 0:
				raise ErroMaquina 

	#busca transicoes e implementa heuristicas
	def executarMaquina(self):

		var = self.buscarTransicao()
		#dicionario usado na heuristica
		conta_transicao = dict()
		
		contador = 1
		
		while var[0] :
			#HEURISTICAS
			# Calculado pelo tamanho da palavra(fitaP) elevado a quantidade de transicoes(fitaR)
			if contador > (len( self.fitaP ) ** len( self.fitaR ) ):
				print("Loop infinito")
				print("Palavra foi rejeitada")
				exit(0)

			try:
				conta_transicao[var[1]] +=1
			except KeyError:
				conta_transicao[var[1]] = 0

			maior_ocorrencia = max( conta_transicao , key = conta_transicao.get )
			# Calculado pelo tamanho da palavra elevado a quantidade de transicoes
			if conta_transicao[maior_ocorrencia] == var[1] and maior_ocorrencia > ( len( self.fitaP ) ** len( self.fitaR) ):
				print("Palavra foi rejeitada")
				print("Loop infinito")
				exit(0)

			print("Execucao " + str(contador))
			print(self)	
			contador+=1

			var = self.buscarTransicao() #buscando proxima transicao
			
			pass
		

		print("Palavra foi aceita")

# Tradução das transicoes para manipulações
class Transicao():

	def __init__(self, transicao_string):
		self.transicao_string = transicao_string.split('0')
		self.estado_inicial = self.transicao_string[0]
		self.simbolo_entrada = self.transicao_string[1]
		self.estado_destino = self.transicao_string[2]
		self.simbolo_escrita = self.transicao_string[3]
		self.direcao = self.transicao_string[4]		

	def __str__(self):	#descreve a transição para facilitar visualizacao
		traducao_estado = lambda s: "q"+str(len(s)-1)
		dire = {
			"1" : "R",
			"11" : "L"
		}
		out = ""
		out += "[" + traducao_estado(self.estado_inicial) + ", " + self.simbolo_entrada + "] ->  "
		out += "[" + traducao_estado(self.estado_destino) + ", " + self.simbolo_escrita + ", " + dire[self.direcao] + "]\n"
		return out

class ErroMaquina(Exception):
	pass
