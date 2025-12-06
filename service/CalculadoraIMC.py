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
    
    def classificar_percentual_gordura(self, percentual_gordura, idade, genero):
        """
        Classifica o percentual de gordura segundo faixas por idade e gênero.
        
        Args:
            percentual_gordura: Percentual de gordura (float)
            idade: Idade da pessoa (int)
            genero: Gênero ('M' para masculino, 'F' para feminino)
        
        Returns:
            String com a classificação: Excelente, Bom, Acima da média, Média, Abaixo da média, Ruim, Muito ruim
        """
        if percentual_gordura is None or idade is None or genero is None:
            return None
        
        if percentual_gordura < 3 or percentual_gordura > 70:
            return None
        
        if idade < 18 or idade > 100:
            return None
        
        genero = genero.upper()
        if genero not in ['M', 'F']:
            return None
        
        if genero == 'M':
            if idade >= 18 and idade <= 30:
                if percentual_gordura < 8:
                    return "Excelente"
                elif percentual_gordura < 14:
                    return "Bom"
                elif percentual_gordura < 18:
                    return "Acima da média"
                elif percentual_gordura < 22:
                    return "Média"
                elif percentual_gordura < 25:
                    return "Abaixo da média"
                elif percentual_gordura < 30:
                    return "Ruim"
                else:
                    return "Muito ruim"
            elif idade >= 31 and idade <= 40:
                if percentual_gordura < 11:
                    return "Excelente"
                elif percentual_gordura < 15:
                    return "Bom"
                elif percentual_gordura < 19:
                    return "Acima da média"
                elif percentual_gordura < 23:
                    return "Média"
                elif percentual_gordura < 26:
                    return "Abaixo da média"
                elif percentual_gordura < 31:
                    return "Ruim"
                else:
                    return "Muito ruim"
            elif idade >= 41 and idade <= 50:
                if percentual_gordura < 13:
                    return "Excelente"
                elif percentual_gordura < 17:
                    return "Bom"
                elif percentual_gordura < 21:
                    return "Acima da média"
                elif percentual_gordura < 25:
                    return "Média"
                elif percentual_gordura < 28:
                    return "Abaixo da média"
                elif percentual_gordura < 33:
                    return "Ruim"
                else:
                    return "Muito ruim"
            else:
                if percentual_gordura < 15:
                    return "Excelente"
                elif percentual_gordura < 19:
                    return "Bom"
                elif percentual_gordura < 23:
                    return "Acima da média"
                elif percentual_gordura < 27:
                    return "Média"
                elif percentual_gordura < 30:
                    return "Abaixo da média"
                elif percentual_gordura < 35:
                    return "Ruim"
                else:
                    return "Muito ruim"
        else:
            if idade >= 18 and idade <= 30:
                if percentual_gordura < 16:
                    return "Excelente"
                elif percentual_gordura < 20:
                    return "Bom"
                elif percentual_gordura < 23:
                    return "Acima da média"
                elif percentual_gordura < 26:
                    return "Média"
                elif percentual_gordura < 30:
                    return "Abaixo da média"
                elif percentual_gordura < 35:
                    return "Ruim"
                else:
                    return "Muito ruim"
            elif idade >= 31 and idade <= 40:
                if percentual_gordura < 18:
                    return "Excelente"
                elif percentual_gordura < 22:
                    return "Bom"
                elif percentual_gordura < 25:
                    return "Acima da média"
                elif percentual_gordura < 28:
                    return "Média"
                elif percentual_gordura < 32:
                    return "Abaixo da média"
                elif percentual_gordura < 37:
                    return "Ruim"
                else:
                    return "Muito ruim"
            elif idade >= 41 and idade <= 50:
                if percentual_gordura < 20:
                    return "Excelente"
                elif percentual_gordura < 24:
                    return "Bom"
                elif percentual_gordura < 27:
                    return "Acima da média"
                elif percentual_gordura < 30:
                    return "Média"
                elif percentual_gordura < 34:
                    return "Abaixo da média"
                elif percentual_gordura < 39:
                    return "Ruim"
                else:
                    return "Muito ruim"
            else:
                if percentual_gordura < 22:
                    return "Excelente"
                elif percentual_gordura < 26:
                    return "Bom"
                elif percentual_gordura < 29:
                    return "Acima da média"
                elif percentual_gordura < 32:
                    return "Média"
                elif percentual_gordura < 36:
                    return "Abaixo da média"
                elif percentual_gordura < 41:
                    return "Ruim"
                else:
                    return "Muito ruim"