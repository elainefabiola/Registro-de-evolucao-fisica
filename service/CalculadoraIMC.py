class CalculadoraIMC:
    
    def calcularIMC(self, peso, altura):
        if peso is None or altura is None:
            return None
        
        if peso <= 0 or altura <= 0:
            return None
        
        imc = peso / (altura ** 2)
        return round(imc, 2)
    
    def classificarIMC(self, imc):
        if imc is None:
            return None
        
        if imc < 17:
            return "Muito abaixo do peso"
        elif imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Acima do peso"
        elif imc < 35:
            return "Obesidade I"
        elif imc < 40:
            return "Obesidade II - Severa"
        else:
            return "Obesidade III - Mórbida"
    
    def calcular_peso_gordura(self, peso, percentual_gordura):
        if peso is None or percentual_gordura is None:
            return None
        
        if peso <= 0 or percentual_gordura < 0:
            return None
        
        peso_gordura = peso * (percentual_gordura / 100)
        return round(peso_gordura, 2)
    
    def calcular_percentual_gordura(self, peso, altura, imc=None):
        if peso is None or altura is None:
            return None
        
        if peso <= 0 or altura <= 0:
            return None
        
        if imc is None:
            imc = self.calcularIMC(peso, altura)
            if imc is None:
                return None
        
        percentual_gordura = (1.20 * imc) - 5.4
        
        if percentual_gordura < 3:
            percentual_gordura = 3.0
        elif percentual_gordura > 70:
            percentual_gordura = 70.0
        
        return round(percentual_gordura, 2)
