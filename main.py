#Guilherme Da Costa Baesse
#Nathan Araújo Silva

from MaquinaUTM import Maquina
import sys

#Na main ocorre verificações no arquivo e na representação que contem no arquivo
if __name__ == '__main__':

	try:
		arquivo = open( sys.argv[1] , 'r' ) 
	except:
		print("Erro ao tentar abrir arquivo")	

	# R(m) é a representacao e w a palavra de entrada
	rMw = arquivo.read() 

	# Verificando se a representação e valida
	if rMw[:3] == "000": 

		rMw = rMw[3:]
		segOcorrencia = rMw.find("000") 
		
		#Se  encontrar a segunda ocorrência é uma representação invalida
		if segOcorrencia == -1:
			print ( "Representacao MTU invalida" )
			exit(0)
		else:
			rM = rMw[:segOcorrencia]
			rM = rM.split("00") 

			if len( rM ) == 1: 
				print( "Representacao MTU invalida" )
				exit(0)

			w = rMw[segOcorrencia+3:] # w esta depois da segunda ocorrencia de três 0s

			terOcorrencia = w.find("000") 

			if terOcorrencia == -1: # Não encontrou os ultimos 3 0s, representacao invalida
				print ( "Representacao MTU invalida" )
				exit(0)
			else:
				# Retira os 3 ultimos 0s
				w = w[:len(w)-4]
				# Lista que contém as substrings da palavra w
				w = w.split('0')
				
				# Adicionando B ao fim da palvra
				w.append('111')

				print ( "Representacao MTU valida" )

				# Executa a maquina com transicoes rM na palavra w 
				Maquina( rM , w ).executarMaquina()
	else:	
		print ("Representacao MTU invalida")
			
			

		




