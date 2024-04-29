from cryptography.fernet import Fernet
import json, os
from calculos_simulados import calculo
from criptografia import descriptografar
from cores import *
from env_variables import CHAVE_FERNET

chave = CHAVE_FERNET
fernet = Fernet(chave.encode())


def salvar_arquivo(nome_arquivo: str, conteudo_descriptografado: dict) -> None:
    dicionario_json = json.dumps(conteudo_descriptografado) # Converte para Json
    dicionario_bytes = dicionario_json.encode() # Converte para bytes   
    criptografado = fernet.encrypt(dicionario_bytes) 
    
    with open(nome_arquivo, 'wb') as f:
        f.write(criptografado)


def abrir_arquivo(nome_arquivo) -> dict:  
    try:
        with open(nome_arquivo, 'rb') as f:
            conteudo_arquivo = f.read()
        
        if os.path.getsize(nome_arquivo) == 0:
            dicionario = {}
        else:
            conteudo_descript = fernet.decrypt(conteudo_arquivo)
            conteudo_string = conteudo_descript.decode()
            dicionario = json.loads(conteudo_string)

    except FileNotFoundError:
        with open(nome_arquivo, 'wb') as f:
            dicionario = {}
        
    return dicionario


dicionario = abrir_arquivo('acertos.bin')
        

def printar_acertos():
    for item in dicionario:
        if item == "Senha":
            continue
        
        print(f"{azul}// Simulado {item} //{reset}")
        for materia, acertos in dicionario[item].items():        
            print(f"{materia}: {descriptografar(acertos)}")
        
        print()
        

def printar_um_simulado(simulado):
    print(f"{azul}// Simulado {simulado} //{reset}")
    for materia, acerto in dicionario[simulado].items():
        print(f"{materia}: {descriptografar(acerto)}")
    print()


def printar_notas():
    for item in dicionario:
        if item != "Senha":
            materia = dicionario[item]
            linguagens, humanas = descriptografar(materia["Linguagens"]), descriptografar(materia["Humanas"]),
            naturezas = descriptografar(materia["Naturezas"])
            matematica, redacao = descriptografar(materia["Matematica"]), descriptografar(materia["Redação"])
            
            print(f"{azul}// Simulado {item} //{reset}")
            print(f"Linguagens: {linguagens} {ciano}({calculo.calc_linguagens(linguagens):.1f}){reset}")
            print(f"Humanas: {humanas} {ciano}({calculo.calc_humanas(humanas):.1f}){reset}")
            print(f"Naturezas: {naturezas} {ciano}({calculo.calc_natureza(naturezas):.1f}){reset}")
            print(f"Matemática: {matematica} {ciano}({calculo.calc_matematica(matematica):.1f}){reset}")
            print(f"Redação: {redacao}")
            
            media = (calculo.calc_linguagens(linguagens) + 
                    calculo.calc_humanas(humanas) + calculo.calc_natureza(naturezas) + 
                    calculo.calc_matematica(matematica) + redacao) / 5
            
            print(f"{azul}Média aproximada: {media:.1f}{reset}")
            print(f"{ciano}Média com bônus regional (10%): {media * 1.1:.1f}{reset}\n")