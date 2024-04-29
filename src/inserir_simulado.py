from lib import dicionario
from criptografia import criptografar
from cores import *

def inserir_acertos():
    i = 0
    acertos_lista = []
    materias = [0,"LINGUAGENS", "HUMANAS", "NATUREZAS", "MATEMATICA"]
    print(f"{ciano}Digite 'q' a qualquer momento para sair.{reset}") 
    while i <= 5:    
        if i == 0:
            qtd_acertos = input("Digite o número do simulado: ")
            if qtd_acertos in dicionario:
                print(f"{red}Já existe um simulado com esse número{reset}")
                continue    
       
       
        elif i == 5:
            qtd_acertos = input("Digite a nota da REDAÇÃO: ") 
        
        else:
            qtd_acertos = input(f"Digite a quantidade de acertos de {materias[i]}: ")

        
        
        if qtd_acertos == 'q':
            break
        
        if not qtd_acertos.isdigit():
            print(f"{red}Você deve digitar um número{reset}")
            continue
        
        if i == 5 and int(qtd_acertos) > 1000 or int(qtd_acertos) < 0:
            print(f"{red}A nota da redação deve estar entra 0 e 1000{reset}")
            continue  
        
        if i != 0 and i != 5 and int(qtd_acertos) > 45 or int(qtd_acertos) < 0:
            print(f"{red}A quantidade de acertos deve estar entre 0 e 45.{reset}")
            continue
        
        if i != 0: qtd_acertos = criptografar(int(qtd_acertos))
        
        acertos_lista.append(qtd_acertos)
        i += 1

    return acertos_lista if len(acertos_lista) == 6 else None

def formatar_para_dict(lista):
    dicionario = {
        str(lista[0]): {
            "Linguagens": lista[1],
            "Humanas": lista[2],
            "Naturezas": lista[3],
            "Matematica": lista[4],
            "Redação": lista[5] 
        }
    }
    return dicionario
