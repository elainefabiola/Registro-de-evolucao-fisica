# Documentação dos Testes Unitários

**Projeto:** Sistema de Registro de Evolução Física  
**Desenvolvido por:** Elaine Faiola Soares - RA: 814550  
**Framework:** unittest (Python)

---

## 1. Visão Geral

Os testes unitários validam os componentes isolados do sistema sem dependência de banco de dados ou serviços externos.

### Componentes Testados

| Componente | Arquivo | Responsabilidade |
|------------|---------|------------------|
| `ValidadorDados` | `service/ValidadorDados.py` | Validação de dados de entrada |
| `CalculadoraIMC` | `service/CalculadoraIMC.py` | Cálculos de IMC e composição corporal |

### Estatísticas

| Métrica | Valor |
|---------|-------|
| Total de Testes | 19 |
| Testes Aprovados | 19 |
| Taxa de Sucesso | 100% |
| Tempo de Execução | ~0.001s |

---

## 2. Estrutura do Arquivo de Testes

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from service.ValidadorDados import ValidadorDados
from service.CalculadoraIMC import CalculadoraIMC
```

---

## 3. Classe TestValidadorDados

Testa a classe `ValidadorDados` responsável pela validação de dados de entrada.

### 3.1 Configuração (setUp)

```python
class TestValidadorDados(unittest.TestCase):

    def setUp(self):
        self.validador = ValidadorDados()
```

### 3.2 Teste: Registrar Todas Circunferências (AC1)

Valida que todas as 15 circunferências corporais são aceitas com valores válidos.

```python
def test_AC1_RegistrarTodasCircunferencias(self):
    circunferencias = {
        'torax': 95.0,
        'braco_direito_contraido': 35.5,
        'braco_esquerdo_contraido': 35.0,
        'braco_direito_relaxado': 32.5,
        'braco_esquerdo_relaxado': 32.0,
        'abdomen': 85.0,
        'cintura': 80.0,
        'quadril': 95.0,
        'antebraco_direito': 28.5,
        'antebraco_esquerdo': 28.0,
        'coxa_direita': 55.0,
        'coxa_esquerda': 54.5,
        'panturrilha_direita': 38.0,
        'panturrilha_esquerda': 37.5,
        'escapular': 20.0
    }
    for campo, valor in circunferencias.items():
        valido, erro = self.validador._validar_circunferencia(valor, campo)
        self.assertTrue(valido)
        self.assertIsNone(erro)
```

**Entrada:** Dicionário com 15 circunferências e valores válidos  
**Saída Esperada:** `(True, None)` para cada circunferência

---

### 3.3 Teste: Valores Numéricos Positivos (AC2)

Valida que valores positivos são aceitos e negativos são rejeitados.

```python
def test_AC2_ValoresNumericosPositivosComDuasCasasDecimais(self):
    valores_validos = [30.00, 35.50, 40.99, 28.5, 33.0]
    for valor in valores_validos:
        valido, erro = self.validador._validar_circunferencia(valor, "torax")
        self.assertTrue(valido)
    
    valor_negativo = -30.0
    valido, erro = self.validador._validar_circunferencia(valor_negativo, "torax")
    self.assertFalse(valido)
    self.assertIn("positivo", erro.lower())
```

**Entrada:** Lista de valores positivos e um valor negativo  
**Saída Esperada:** `True` para positivos, `False` para negativo

---

### 3.4 Teste: Validação de Percentual de Gordura (AC7)

Valida a faixa aceitável de percentual de gordura (3% a 70%).

```python
def test_AC7_ValidacaoPercentualGordura(self):
    valido, erro = self.validador._validar_percentual_gordura(3.0)
    self.assertTrue(valido)
    
    valido, erro = self.validador._validar_percentual_gordura(70.0)
    self.assertTrue(valido)
    
    valido, erro = self.validador._validar_percentual_gordura(2.5)
    self.assertFalse(valido)
    self.assertIn("3%", erro)
    
    valido, erro = self.validador._validar_percentual_gordura(75.0)
    self.assertFalse(valido)
    self.assertIn("70%", erro)
```

**Entrada:** Valores 3.0, 70.0 (válidos), 2.5, 75.0 (inválidos)  
**Saída Esperada:** Aprovação para valores dentro da faixa, rejeição fora

---

### 3.5 Teste: Validação de Peso (AC8)

Valida a faixa aceitável de peso (20kg a 180kg).

```python
def test_AC8_ValidacaoPeso(self):
    valido, erro = self.validador.validarPeso(20.0)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarPeso(180.0)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarPeso(19.0)
    self.assertFalse(valido)
    self.assertIn("20 kg", erro)
    
    valido, erro = self.validador.validarPeso(185.0)
    self.assertFalse(valido)
    self.assertIn("180 kg", erro)
```

**Entrada:** Pesos nos limites (20kg, 180kg) e fora dos limites (19kg, 185kg)  
**Saída Esperada:** Validação correta dos limites

---

### 3.6 Teste: Validação de Altura (AC9)

Valida a faixa aceitável de altura (1.00m a 2.50m).

```python
def test_AC9_ValidacaoAltura(self):
    valido, erro = self.validador.validarAltura(1.00)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarAltura(2.50)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarAltura(0.95)
    self.assertFalse(valido)
    self.assertIn("1.00 m", erro)
    
    valido, erro = self.validador.validarAltura(2.60)
    self.assertFalse(valido)
    self.assertIn("2.50 m", erro)
```

**Entrada:** Alturas nos limites e fora dos limites  
**Saída Esperada:** Validação correta dos limites

---

### 3.7 Teste: Campo Observações com Limite (AC10/AC11)

Valida o limite de 1000 caracteres para observações.

```python
def test_AC10_AC11_CampoObservacoesComLimite(self):
    observacao_valida = "A" * 1000
    valido, erro = self.validador._validar_observacoes(observacao_valida)
    self.assertTrue(valido)
    
    observacao_invalida = "A" * 1001
    valido, erro = self.validador._validar_observacoes(observacao_invalida)
    self.assertFalse(valido)
    self.assertIn("1000 caracteres", erro)
```

**Entrada:** String com 1000 caracteres (válida) e 1001 caracteres (inválida)  
**Saída Esperada:** Aprovação até 1000, rejeição acima

---

### 3.8 Teste: Validar Medidas Completas

Valida um conjunto completo de medidas corporais.

```python
def test_ValidarMedidasCompletas(self):
    medidas = {
        'peso': 75.0,
        'altura': 1.80,
        'percentual_gordura': 15.0,
        'torax': 95.0,
        'cintura': 80.0,
        'quadril': 95.0,
        'observacoes': 'Teste de medidas'
    }
    valido, erro = self.validador.validarMedidas(medidas)
    self.assertTrue(valido)
    self.assertIsNone(erro)
```

**Entrada:** Dicionário com medidas válidas  
**Saída Esperada:** `(True, None)`

---

### 3.9 Teste: Validar Medidas Inválidas

Valida a rejeição de medidas fora dos limites.

```python
def test_ValidarMedidasInvalidas(self):
    medidas = {'peso': 250.0, 'altura': 1.80}
    valido, erro = self.validador.validarMedidas(medidas)
    self.assertFalse(valido)
    self.assertIn("180 kg", erro)
```

**Entrada:** Peso de 250kg (acima do limite)  
**Saída Esperada:** `(False, "Peso deve ser no máximo 180 kg")`

---

### 3.10 Teste: Validar Formato Numérico

Valida se o valor é um número válido.

```python
def test_ValidarFormatoNumerico(self):
    valido, erro = self.validador.validarFormatoNumerico(75.5)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarFormatoNumerico("abc")
    self.assertFalse(valido)
    
    valido, erro = self.validador.validarFormatoNumerico(None)
    self.assertFalse(valido)
```

**Entrada:** Número válido, string inválida, valor nulo  
**Saída Esperada:** Validação correta de cada caso

---

### 3.11 Teste: Validar Faixa de Valores

Valida se um valor está dentro de uma faixa especificada.

```python
def test_ValidarFaixaValores(self):
    valido, erro = self.validador.validarFaixaValores(50, 0, 100)
    self.assertTrue(valido)
    
    valido, erro = self.validador.validarFaixaValores(-10, 0, 100)
    self.assertFalse(valido)
    
    valido, erro = self.validador.validarFaixaValores(150, 0, 100)
    self.assertFalse(valido)
```

**Entrada:** Valores dentro e fora da faixa 0-100  
**Saída Esperada:** Validação correta dos limites

---

## 4. Classe TestCalculadoraIMC

Testa a classe `CalculadoraIMC` responsável pelos cálculos de IMC e composição corporal.

### 4.1 Configuração (setUp)

```python
class TestCalculadoraIMC(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraIMC()
```

### 4.2 Teste: Cálculo Automático de Peso de Gordura (AC5)

Calcula o peso de gordura baseado no percentual.

```python
def test_AC5_CalculoAutomaticoPesoGordura(self):
    peso = 75.5
    percentual_gordura = 15.0
    peso_gordura = self.calculadora.calcular_peso_gordura(peso, percentual_gordura)
    peso_gordura_esperado = 75.5 * 0.15
    self.assertIsNotNone(peso_gordura)
    self.assertAlmostEqual(peso_gordura, peso_gordura_esperado, places=2)
```

**Entrada:** Peso 75.5kg, Percentual de gordura 15%  
**Saída Esperada:** 11.33kg (75.5 × 0.15)

---

### 4.3 Teste: Cálculo Automático de IMC (AC26)

Calcula o IMC usando a fórmula peso/(altura²).

```python
def test_AC26_CalculoAutomaticoIMC(self):
    peso = 75.5
    altura = 1.80
    imc = self.calculadora.calcularIMC(peso, altura)
    imc_esperado = peso / (altura ** 2)
    self.assertIsNotNone(imc)
    self.assertAlmostEqual(imc, imc_esperado, places=2)
```

**Entrada:** Peso 75.5kg, Altura 1.80m  
**Saída Esperada:** IMC ≈ 23.30

---

### 4.4 Teste: IMC com Duas Casas Decimais (AC27)

Verifica se o IMC é retornado com no máximo 2 casas decimais.

```python
def test_AC27_IMCDuasCasasDecimais(self):
    imc = self.calculadora.calcularIMC(75.567, 1.803)
    self.assertIsNotNone(imc)
    imc_str = str(imc)
    if '.' in imc_str:
        casas_decimais = len(imc_str.split('.')[1])
        self.assertLessEqual(casas_decimais, 2)
```

**Entrada:** Peso e altura com várias casas decimais  
**Saída Esperada:** IMC com no máximo 2 casas decimais

---

### 4.5 Teste: Classificação de IMC (AC28)

Verifica todas as 7 faixas de classificação do IMC.

```python
def test_AC28_ClassificacaoIMC(self):
    classificacoes = [
        (16.5, "Muito abaixo do peso"),
        (18.0, "Abaixo do peso"),
        (22.0, "Peso normal"),
        (27.0, "Acima do peso"),
        (32.0, "Obesidade I"),
        (37.0, "Obesidade II"),
        (42.0, "Obesidade III")
    ]
    for imc, classificacao_esperada in classificacoes:
        classificacao = self.calculadora.classificarIMC(imc)
        self.assertIsNotNone(classificacao)
        self.assertIn(classificacao_esperada.lower(), classificacao.lower())
```

**Entrada:** 7 valores de IMC representando cada faixa  
**Saída Esperada:** Classificação correta para cada faixa

| IMC | Classificação |
|-----|---------------|
| < 17 | Muito abaixo do peso |
| 17 - 18.49 | Abaixo do peso |
| 18.5 - 24.99 | Peso normal |
| 25 - 29.99 | Acima do peso |
| 30 - 34.99 | Obesidade I |
| 35 - 39.99 | Obesidade II |
| ≥ 40 | Obesidade III |

---

### 4.6 Teste: Calcular IMC com Valores Inválidos

Verifica o tratamento de valores nulos e inválidos.

```python
def test_CalcularIMCValoresInvalidos(self):
    self.assertIsNone(self.calculadora.calcularIMC(None, 1.80))
    self.assertIsNone(self.calculadora.calcularIMC(75.0, None))
    self.assertIsNone(self.calculadora.calcularIMC(0, 1.80))
    self.assertIsNone(self.calculadora.calcularIMC(75.0, 0))
    self.assertIsNone(self.calculadora.calcularIMC(-75.0, 1.80))
```

**Entrada:** Valores nulos, zero e negativos  
**Saída Esperada:** `None` para todos os casos inválidos

---

### 4.7 Teste: Classificar IMC Nulo

Verifica o tratamento de IMC nulo.

```python
def test_ClassificarIMCNulo(self):
    self.assertIsNone(self.calculadora.classificarIMC(None))
```

**Entrada:** `None`  
**Saída Esperada:** `None`

---

### 4.8 Teste: Calcular Peso de Gordura com Valores Inválidos

Verifica o tratamento de valores inválidos no cálculo de peso de gordura.

```python
def test_CalcularPesoGorduraValoresInvalidos(self):
    self.assertIsNone(self.calculadora.calcular_peso_gordura(None, 15.0))
    self.assertIsNone(self.calculadora.calcular_peso_gordura(75.0, None))
    self.assertIsNone(self.calculadora.calcular_peso_gordura(0, 15.0))
    self.assertIsNone(self.calculadora.calcular_peso_gordura(75.0, -5.0))
```

**Entrada:** Valores nulos, zero e negativos  
**Saída Esperada:** `None` para todos os casos inválidos

---

### 4.9 Teste: Calcular Percentual de Gordura

Verifica o cálculo do percentual de gordura.

```python
def test_CalcularPercentualGordura(self):
    percentual = self.calculadora.calcular_percentual_gordura(75.0, 1.80)
    self.assertIsNotNone(percentual)
    self.assertGreaterEqual(percentual, 3.0)
    self.assertLessEqual(percentual, 70.0)
```

**Entrada:** Peso 75kg, Altura 1.80m  
**Saída Esperada:** Percentual entre 3% e 70%

---

### 4.10 Teste: Calcular Percentual de Gordura com Valores Inválidos

Verifica o tratamento de valores inválidos.

```python
def test_CalcularPercentualGorduraValoresInvalidos(self):
    self.assertIsNone(self.calculadora.calcular_percentual_gordura(None, 1.80))
    self.assertIsNone(self.calculadora.calcular_percentual_gordura(75.0, None))
    self.assertIsNone(self.calculadora.calcular_percentual_gordura(0, 1.80))
```

**Entrada:** Valores nulos e zero  
**Saída Esperada:** `None` para todos os casos inválidos

---

## 5. Execução dos Testes

### Comandos

```bash
# Executar todos os testes
python3 test_sistema.py

# Executar com saída detalhada
python3 test_sistema.py -v

# Executar teste específico
python3 -m unittest test_sistema.TestValidadorDados.test_AC8_ValidacaoPeso

# Executar uma classe de testes
python3 -m unittest test_sistema.TestValidadorDados
```

### Resultado da Execução

```
test_AC26_CalculoAutomaticoIMC ... ok
test_AC27_IMCDuasCasasDecimais ... ok
test_AC28_ClassificacaoIMC ... ok
test_AC5_CalculoAutomaticoPesoGordura ... ok
test_CalcularIMCValoresInvalidos ... ok
test_CalcularPercentualGordura ... ok
test_CalcularPercentualGorduraValoresInvalidos ... ok
test_CalcularPesoGorduraValoresInvalidos ... ok
test_ClassificarIMCNulo ... ok
test_AC10_AC11_CampoObservacoesComLimite ... ok
test_AC1_RegistrarTodasCircunferencias ... ok
test_AC2_ValoresNumericosPositivosComDuasCasasDecimais ... ok
test_AC7_ValidacaoPercentualGordura ... ok
test_AC8_ValidacaoPeso ... ok
test_AC9_ValidacaoAltura ... ok
test_ValidarFaixaValores ... ok
test_ValidarFormatoNumerico ... ok
test_ValidarMedidasCompletas ... ok
test_ValidarMedidasInvalidas ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.001s

OK
```

---

## 6. Mapeamento com Critérios de Aceitação

| ID Teste | Critério de Aceitação | Descrição |
|----------|----------------------|-----------|
| AC1 | US01 - AC1 | Registrar todas as circunferências |
| AC2 | US01 - AC2 | Valores numéricos positivos |
| AC5 | US02 - AC5 | Cálculo automático peso gordura |
| AC7 | US02 - AC7 | Validação percentual gordura |
| AC8 | US02 - AC8 | Validação de peso |
| AC9 | US02 - AC9 | Validação de altura |
| AC10/AC11 | US03 - AC10/AC11 | Campo observações com limite |
| AC26 | US05 - AC26 | Cálculo automático IMC |
| AC27 | US05 - AC27 | IMC duas casas decimais |
| AC28 | US05 - AC28 | Classificação IMC |

---

## 7. Boas Práticas Aplicadas

| Prática | Aplicação |
|---------|-----------|
| Nomenclatura clara | Nomes descritivos nos métodos |
| Isolamento | Cada teste é independente |
| setUp | Inicialização comum no setUp |
| Assertions específicos | assertTrue, assertFalse, assertIn, etc. |
| Cobertura de limites | Testes nos valores limite |
| Casos positivos e negativos | Validação de sucesso e falha |

---

## 8. Resumo Final

| Métrica | Valor |
|---------|-------|
| Classes de Teste | 2 |
| Métodos de Teste | 19 |
| Componentes Testados | 2 |
| Taxa de Aprovação | 100% |
| Tempo de Execução | 0.001s |
| Dependências Externas | Nenhuma |

---

**Data:** Dezembro 2025  
**Versão:** 1.0

