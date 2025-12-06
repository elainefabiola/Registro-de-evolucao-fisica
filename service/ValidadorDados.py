class ValidadorDados:
    
    def validarPeso(self, peso):
        if peso is None:
            return (False, "Peso não informado")
        
        try:
            peso_float = float(peso)
        except (ValueError, TypeError):
            return (False, "Peso deve ser um número")
        
        if peso_float < 20:
            return (False, "Peso deve ser no mínimo 20 kg")
        
        if peso_float > 180:
            return (False, "Peso deve ser no máximo 180 kg")
        
        return (True, None)
    
    def validarAltura(self, altura):
        if altura is None:
            return (False, "Altura não informada")
        
        try:
            altura_float = float(altura)
        except (ValueError, TypeError):
            return (False, "Altura deve ser um número")
        
        if altura_float < 1.00:
            return (False, "Altura deve ser no mínimo 1.00 m")
        
        if altura_float > 2.50:
            return (False, "Altura deve ser no máximo 2.50 m")
        
        return (True, None)
    
    def _validar_percentual_gordura(self, percentual):
        if percentual is None:
            return (True, None)
        
        try:
            percentual_float = float(percentual)
        except (ValueError, TypeError):
            return (False, "Percentual de gordura deve ser um número")
        
        if percentual_float < 3:
            return (False, "Percentual de gordura deve ser no mínimo 3%")
        
        if percentual_float > 70:
            return (False, "Percentual de gordura deve ser no máximo 70%")
        
        return (True, None)
    
    def _validar_circunferencia(self, valor, nome_campo="circunferência"):
        if valor is None or valor == "":
            return (True, None)
        
        try:
            valor_float = float(valor)
        except (ValueError, TypeError):
            return (False, f"{nome_campo} deve ser um número")
        
        if valor_float < 0:
            return (False, f"{nome_campo} deve ser um valor positivo")
        
        partes = str(valor_float).split('.')
        if len(partes) == 2 and len(partes[1]) > 2:
            return (False, f"{nome_campo} deve ter no máximo 2 casas decimais")
        
        return (True, None)
    
    def _validar_observacoes(self, observacoes):
        if observacoes is None or observacoes == "":
            return (True, None)
        
        observacoes_str = str(observacoes)
        
        if len(observacoes_str) > 1000:
            return (False, "Observações devem ter no máximo 1000 caracteres")
        
        return (True, None)
    
    def validarFormatacaoTexto(self, texto):
        """
        Valida se o texto contém apenas formatação básica permitida.
        Permite: letras, números, espaços, pontuação básica, quebras de linha, acentos.
        Não permite: HTML, tags, scripts, caracteres especiais perigosos.
        
        Args:
            texto: Texto a ser validado (string)
        
        Returns:
            Tupla (valido, erro): (True, None) se válido, (False, mensagem_erro) se inválido
        """
        if texto is None or texto == "":
            return (True, None)
        
        texto_str = str(texto)
        
        caracteres_proibidos = ['<', '>', '&', '"', "'", '/', '\\', '`', '|']
        
        for char in caracteres_proibidos:
            if char in texto_str:
                return (False, f"Texto não pode conter o caractere '{char}'. Use apenas texto simples.")
        
        return (True, None)
    
    def validarMedidas(self, medidas):
        if 'peso' in medidas:
            valido, erro = self.validarPeso(medidas['peso'])
            if not valido:
                return (False, erro)
        
        if 'altura' in medidas:
            valido, erro = self.validarAltura(medidas['altura'])
            if not valido:
                return (False, erro)
        
        if 'percentual_gordura' in medidas:
            valido, erro = self._validar_percentual_gordura(medidas['percentual_gordura'])
            if not valido:
                return (False, erro)
        
        circunferencias = [
            'torax', 'braco_direito_contraido', 'braco_esquerdo_contraido',
            'braco_direito_relaxado', 'braco_esquerdo_relaxado', 'abdomen',
            'cintura', 'quadril', 'antebraco_direito', 'antebraco_esquerdo',
            'coxa_direita', 'coxa_esquerda', 'panturrilha_direita',
            'panturrilha_esquerda', 'escapular'
        ]
        
        for circ in circunferencias:
            if circ in medidas:
                valido, erro = self._validar_circunferencia(medidas[circ], circ)
                if not valido:
                    return (False, erro)
        
        if 'observacoes' in medidas:
            valido, erro = self._validar_observacoes(medidas['observacoes'])
            if not valido:
                return (False, erro)
        
        return (True, None)
    
    def validarFormatoNumerico(self, valor):
        if valor is None:
            return (False, "Valor não informado")
        
        try:
            float(valor)
            return (True, None)
        except (ValueError, TypeError):
            return (False, "Valor deve ser um número")
    
    def validarFaixaValores(self, valor, min_valor, max_valor):
        valido, erro = self.validarFormatoNumerico(valor)
        if not valido:
            return (False, erro)
        
        valor_float = float(valor)
        
        if valor_float < min_valor:
            return (False, f"Valor deve ser no mínimo {min_valor}")
        
        if valor_float > max_valor:
            return (False, f"Valor deve ser no máximo {max_valor}")
        
        return (True, None)
