import os, time
from inserir_simulado import *
from senha import *
from lib import *
from editar_simulado import *
from excluir_simulados import *
from cores import *
from criptografia import *


def main():
    campo_senha()
    while True: # Loop principal
        print("1. Inserir simulados")
        print("2. Ver simulados")
        print("3. Editar simulados")
        print("4. Excluir simulados")
        print("5. Alterar senha")
        print("6. Fechar programa")
        
        entrada = input("> ")
        
        match entrada:
            case "6":  # Sair do programa
                break
            
            
            case "1": # Inserir acertos
                os.system("cls||clear")
                acertos_lista = inserir_acertos()
                if acertos_lista is not None:
                    dicionario.update(formatar_para_dict(acertos_lista))
                    print(f"\n{verde}Simulado adicionado com sucesso{reset}\n")
                    salvar_arquivo('acertos.bin', dicionario)
                    time.sleep(1)
                os.system("cls||clear")
            
            
            case "2": # Printar notas
                os.system("cls||clear")
                printar_notas()
                input("Aperte 'enter' para voltar ao menu principal")
                os.system("cls||clear")
                    
            
            case "3": # Editar acertos
                os.system("cls||clear")
                editar_simulado()
                salvar_arquivo('acertos.bin', dicionario)
                os.system("cls") 
            
                            
            case "4": # Excluir simulado
                os.system("cls||clear")
                excluir_simulado()
                salvar_arquivo('acertos.bin', dicionario)
                os.system("cls")
            
            
            case "5": # Alterar senha
                os.system("cls||clear")
                nova_senha = criar_senha()
                if nova_senha is not None:
                    dicionario['Senha'] = nova_senha
                    salvar_arquivo('acertos.bin', dicionario)
                os.system("cls||clear")
                     
                     
                            
if __name__ == "__main__":
    main()