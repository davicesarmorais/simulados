class Calculos():
    def __init__(self, nl_ling, nl_hum, nl_nat, nl_mat) -> None:
        self.nl_ling: tuple = nl_ling
        self.nl_hum: tuple = nl_hum
        self.nl_nat: tuple = nl_nat
        self.nl_mat: tuple = nl_mat

    def calc_linguagens(self, qtd_acertos):
        nota_minima = self.nl_ling[0]
        nota_maxima = self.nl_ling[1]
        
        if qtd_acertos == 45:
            return nota_maxima
        elif qtd_acertos == 0:
            return nota_minima
        else:
            return ((nota_maxima - nota_minima) * qtd_acertos + (nota_minima * 45)) / 45

    def calc_humanas(self, qtd_acertos):
        nota_minima = self.nl_hum[0]
        nota_maxima = self.nl_hum[1]
        
        if qtd_acertos == 45:
            return nota_maxima
        elif qtd_acertos == 0:
            return nota_minima
        else:
            return ((nota_maxima - nota_minima) * qtd_acertos + (nota_minima * 45)) / 45
        
    def calc_natureza(self, qtd_acertos):
        nota_minima = self.nl_hum[0]
        nota_maxima = self.nl_hum[1]
        
        if qtd_acertos == 45:
            return nota_maxima
        elif qtd_acertos == 0:
            return nota_minima
        else:
            return ((nota_maxima - nota_minima) * qtd_acertos + (nota_minima * 45)) / 45
    
    def calc_matematica(self, qtd_acertos):
        nota_minima = self.nl_mat[0]
        nota_maxima = self.nl_mat[1]
        
        if qtd_acertos == 45:
            return nota_maxima
        elif qtd_acertos == 0:
            return nota_minima
        else:
            return ((nota_maxima - nota_minima) * qtd_acertos + (nota_minima * 45)) / 45
        
        
notas_limite_linguagens = (287, 820.8)
notas_limite_humanas = (289.9, 823)
notas_limite_naturezas = (314.4, 868.4)
notas_limite_matematica = (319.8, 958.6)

calculo = Calculos(notas_limite_linguagens, notas_limite_humanas, 
                   notas_limite_naturezas, notas_limite_matematica)