from lib import printar_acertos, printar_um_simulado, dicionario
import os, time
from criptografia import criptografar
from cores import *

def editar_simulado():
    principal_while = True
    primeiro_while = True
    segundo_while = True
    terceiro_while = True
    while principal_while:
        
        while primeiro_while:
            printar_acertos()

            print(f"Digite o número do simulado que quer editar\n{ciano}Ou 'q' para sair{reset}")
            numero_simulado = input("> ")
            
            if numero_simulado in "qQ":
                segundo_while, terceiro_while = False, False
                principal_while = False
                break
            
            if numero_simulado == 'Senha':
                print("🤨")
                time.sleep(0.5)
                os.system("cls||clear")
                continue
            
            if numero_simulado not in dicionario:
                print(f"{red}Simulado não encontrado{reset}")
                time.sleep(1)
                os.system("cls||clear")
                continue
            
            segundo_while = True
            terceiro_while = True
            break
        
        while segundo_while:
            os.system("cls||clear")
            printar_um_simulado(numero_simulado)
            print("Digite a primeira letra da área que quer editar")
            print(f"Digite {ciano}'1'{reset} para escolher outro simulado ou {ciano}'2'{reset} para retornar ao menu principal")
            letra_area = input("> ").upper()
            
            if letra_area == '1':
                os.system("cls||clear")
                terceiro_while = False
                primeiro_while = True
                break
            
            if letra_area == '2':
                terceiro_while = False
                principal_while = False
                break
            
            
            if letra_area not in ["L","H","N","M","R"]:
                print(f"{red}Área não encontrada{reset}")
                time.sleep(1)
                continue
            
            terceiro_while = True
            break
                
        areas = {"L": "Linguagens","H": "Humanas", "N": "Naturezas", "M": "Matematica", "R": "Redação"}
        
        while terceiro_while:
            novo_valor = input(f"Digite a nova nota ou quantidade de acertos de {azul}{areas[letra_area]}{reset} ou {ciano}'c' para cancelar:{reset} ")
            
            if novo_valor in 'cC':
                primeiro_while = False
                os.system("cls||clear")
                break
            
            if not novo_valor.isdecimal():
                print(f"{red}Você deve digitar um número{reset}")
                continue
            
            novo_valor = int(novo_valor)
            if letra_area != "R" and novo_valor > 45 or novo_valor < 0:
                print(f"{red}A quantidade de acertos deve estar entre 0 e 45.{reset}")
                continue
            
            if letra_area == "R" and novo_valor > 1000 or novo_valor < 0:
                print(f"{red}A nota da redação deve estar entra 0 e 1000.{reset}")
                continue
            
            print(f"Você deseja confirmar a alteração de {azul}{areas[letra_area]}{reset} para {verde}{novo_valor}{reset}? (s/n)")
            confirmacao = input("> ").lower()
            
            if confirmacao == 's':
                dicionario[numero_simulado][areas[letra_area]] = criptografar(int(novo_valor))
                print(f"\n{verde}Simulado editado com sucesso!{reset}\n")
                time.sleep(1)
                principal_while = False
                break
            else:
                continue
