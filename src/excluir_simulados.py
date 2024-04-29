from lib import printar_acertos, dicionario
import os, time
from cores import *

def excluir_simulado():
    printar_acertos()
    while True:
        print(f"Digite o número do simulado que quer {red}excluir{reset} ou {ciano}'q' para voltar{reset}")
        escolha = input("> ")
        
        if escolha in "qQ":
            os.system("cls||clear")
            break
        
        if escolha not in dicionario:
            print(f"{red}Simulado não encontrado{reset}")
            continue
        
        print(f"Tem certeza que quer {red}excluir{reset} o {ciano}simulado {escolha}{reset}? (s/n)")
        confirmacao = input("> ").lower()
        
        if confirmacao == "s":
            del dicionario[escolha]
            print(f"{verde}Simulado excluído com sucesso!{reset}")
            time.sleep(1)
            break
        else:
            continue
