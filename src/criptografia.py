from env_variables import SEGREDO_CRIPTO

a = SEGREDO_CRIPTO

def criptografar(inteiro: int) -> str:
    numero_inicial = inteiro
    if numero_inicial > 45:
        etapa1 = ''.join(a[int(x)] for x in str(numero_inicial))
        numero_criptografado = '+' + etapa1[len(etapa1) // 2:] + etapa1[0:len(etapa1)//2]
    else:
        numero_inicial = str(numero_inicial).zfill(2)
        soma = str(int(numero_inicial[0]) + int(numero_inicial[1])).zfill(2)
        multiplicacao = str(int(numero_inicial[0]) * int(numero_inicial[1])).zfill(2)
        
        if int(numero_inicial[0]) - int(numero_inicial[1]) > 0:
            subtracao = str(int(numero_inicial[0]) - int(numero_inicial[1])).zfill(2)
        else:
            subtracao = str(abs(int(numero_inicial[0]) - int(numero_inicial[1]))+ 1).zfill(2)

        primeira_etapa = f'{soma}{multiplicacao}{subtracao}'
        segunda_etapa = ''.join(a[int(x)] for x in primeira_etapa)
        numero_criptografado = segunda_etapa[len(segunda_etapa) // 2:] + segunda_etapa[0:len(segunda_etapa)//2]
    
    return numero_criptografado
    
    
def descriptografar(string: str) -> int:
    numero_criptografado = string
    
    if numero_criptografado[0] == '+':
        etapa1 = numero_criptografado[1:]
        tamanho = len(etapa1) + 1 if len(etapa1) % 2 != 0 else len(etapa1)
        etapa2 = etapa1[tamanho // 2:] + etapa1[0:tamanho//2]
        numero_descriptografado = ''.join(str(a.index(x)) for x in etapa2)
    
    else:
        tamanho = len(numero_criptografado) + 1 if len(numero_criptografado) % 2 != 0 else len(numero_criptografado)
        descriptografar_1 = numero_criptografado[tamanho // 2:] + numero_criptografado[0:tamanho//2]

        numeros = ''.join(str(a.index(x)) for x in descriptografar_1)

        for i in range(5):
            for j in range(10):
                if i-j > 0:
                    sub = i-j
                else:
                    sub = abs(i-j) + 1
                if (i + j) == int(numeros[0:2]) and (i * j) == int(numeros[2:4]) and (sub) == int(numeros[4:6]):
                    numero_descriptografado = str(i) + str(j) 
                    break
        
    return int(numero_descriptografado)
