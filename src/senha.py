import os, re, time
from hashlib import sha256
from lib import dicionario, salvar_arquivo
from cores import *
from env_variables import CONTRA_SENHA


def criar_senha():
    while True:
        print(f"{azul}Crie uma senha (A senha precisa ter entre 4 e 16 caracteres e pelo menos uma letra e um número){reset}") # Digite nova senha
        if "Senha" in dicionario:
            print(f"{ciano}Ou digite 'q' para voltar{reset}")
        
        input_senha = input("> ")
        
        if "Senha" in dicionario and input_senha in 'qQ': # Opção de sair apenas se tiver alterando a senha, não criando
            break
        
        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d).{4,16}$', input_senha):
            continue
        
        print(f"\nSenha escolhida: {azul}{input_senha}{reset}\n") # Senha escolhida
        print("Deseja que essa seja a nova senha? (s/n)")  # Confirmar senha
        confirmar_senha = input("> ").lower() 
        
        if confirmar_senha == "s":
            senha_hash = sha256((f'{input_senha}' + f'{CONTRA_SENHA}').encode()).hexdigest()
            os.system('cls||clear')
            print(f"\n{verde}Senha criada/alterada!{reset}\n") 
            time.sleep(1)
            return senha_hash        
        else:
            print(f"\n{azul}Operação cancelada.{reset}\n") 


def campo_senha():
    while True:  # Campo de senha
        if "Senha" not in dicionario:
            senha_hash = criar_senha()
            dicionario.update({"Senha": senha_hash})
            salvar_arquivo('acertos.bin', dicionario)
            #enviar_json()
        
        os.system('cls||clear')
        digitar_senha = input("Digite a senha: ")
        hash_senha = sha256((f'{digitar_senha}' + f'{CONTRA_SENHA}').encode()).hexdigest()
        
        if hash_senha != dicionario["Senha"]:
            print(f"\n{red}Senha incorreta{reset}\n")
            time.sleep(.6)
            continue
        
        else: 
            os.system('cls||clear')
            break