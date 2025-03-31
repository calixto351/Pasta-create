from pathlib import Path
import os

nome = str(input("Nome"))
idade = int(input("Idade"))
profiss = str(input("Profissão"))
frasedia = str(input("Frase do dia"))

#criar pasta
pasta = Path.cwd()
nomepasta=input("nome da pasta")
pasta1= pasta/nomepasta
pasta1.mkdir()
#criando o arquivo na nova pasta
pasta= Path(nomepasta)
nomearquivo = input("nome do arquivo")
novoarquivo = pasta/f"{nomearquivo}.txt"
frasearquivo= input("escrita do arquivo caso for txt para não ficar em branco")
novoarquivo.write_text(frasearquivo)
#abrir/editar ou ler arquivo

            #ler
            arquivo = pasta1 /nomearquivo
            arquivo2 = arquivo.open("r")
            linhas = arquivo2.read_text()
            for linha in linhas:
                print(linha,end="")
            arquivo2.close()
            #escrever substituindo o antigo
            arquivo = pasta1 /nomearquivo
            arquivo2 = arquivo.open("w")
            arquivo2.write("sua escrita")
            arquivo2.close()