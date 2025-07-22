#!/usr/bin/env python3
"""
Exemplos básicos de Python - Conceitos fundamentais
"""

# ========================================
# 1. VARIÁVEIS E TIPOS DE DADOS
# ========================================

print("🔤 Trabalhando com Variáveis:")
print("-" * 30)

# Tipos básicos
nome = "João Silva"
idade = 25
altura = 1.75
estudante = True

print(f"Nome: {nome} (tipo: {type(nome).__name__})")
print(f"Idade: {idade} (tipo: {type(idade).__name__})")
print(f"Altura: {altura}m (tipo: {type(altura).__name__})")
print(f"É estudante: {estudante} (tipo: {type(estudante).__name__})")

# ========================================
# 2. ESTRUTURAS DE DADOS
# ========================================

print(f"\n📊 Estruturas de Dados:")
print("-" * 30)

# Lista
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Lista de frutas: {frutas}")

# Tupla (imutável)
coordenadas = (10, 20)
print(f"Coordenadas: {coordenadas}")

# Dicionário
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "São Paulo"
}
print(f"Dados da pessoa: {pessoa}")

# Set (conjunto)
numeros_unicos = {1, 2, 3, 4, 5, 3, 2, 1}  # Remove duplicatas
print(f"Números únicos: {numeros_unicos}")

# ========================================
# 3. ESTRUTURAS DE CONTROLE
# ========================================

print(f"\n🔄 Estruturas de Controle:")
print("-" * 30)

# Condicional if/elif/else
nota = 8.5
if nota >= 9:
    conceito = "Excelente"
elif nota >= 7:
    conceito = "Bom"
elif nota >= 5:
    conceito = "Regular"
else:
    conceito = "Insuficiente"

print(f"Nota {nota} = Conceito: {conceito}")

# Loop for
print("\nContagem de 1 a 5:")
for i in range(1, 6):
    print(f"  {i}")

# Loop for com lista
print("\nIterando sobre frutas:")
for fruta in frutas:
    print(f"  🍎 {fruta}")

# Loop while
print("\nContagem regressiva:")
contador = 5
while contador > 0:
    print(f"  {contador}")
    contador -= 1
print("  🚀 Decolagem!")

# ========================================
# 4. FUNÇÕES
# ========================================

print(f"\n⚙️ Trabalhando com Funções:")
print("-" * 30)

def saudacao(nome, hora_do_dia="dia"):
    """Função que retorna uma saudação personalizada"""
    saudacoes = {
        "manhã": "Bom dia",
        "tarde": "Boa tarde", 
        "noite": "Boa noite",
        "dia": "Olá"
    }
    return f"{saudacoes.get(hora_do_dia, 'Olá')}, {nome}! 👋"

# Testando a função
print(saudacao("Ana"))
print(saudacao("Carlos", "manhã"))
print(saudacao("Beatriz", "noite"))

def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    return largura * altura

def calcular_area_circulo(raio):
    """Calcula a área de um círculo"""
    import math
    return math.pi * raio ** 2

# Testando funções matemáticas
print(f"\nÁrea do retângulo (5x3): {calcular_area_retangulo(5, 3)}")
print(f"Área do círculo (raio=2): {calcular_area_circulo(2):.2f}")

# ========================================
# 5. TRABALHO COM LISTAS
# ========================================

print(f"\n📝 Manipulação de Listas:")
print("-" * 30)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista original: {numeros}")

# List comprehension - números pares
pares = [n for n in numeros if n % 2 == 0]
print(f"Números pares: {pares}")

# List comprehension - quadrados
quadrados = [n**2 for n in numeros[:5]]
print(f"Quadrados dos 5 primeiros: {quadrados}")

# Métodos úteis de lista
numeros_exemplo = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nLista exemplo: {numeros_exemplo}")
print(f"Soma: {sum(numeros_exemplo)}")
print(f"Máximo: {max(numeros_exemplo)}")
print(f"Mínimo: {min(numeros_exemplo)}")
print(f"Média: {sum(numeros_exemplo) / len(numeros_exemplo):.2f}")

# ========================================
# 6. TRABALHO COM STRINGS
# ========================================

print(f"\n🔤 Manipulação de Strings:")
print("-" * 30)

texto = "  Python é uma linguagem incrível!  "
print(f"Original: '{texto}'")
print(f"Sem espaços: '{texto.strip()}'")
print(f"Maiúsculas: '{texto.upper()}'")
print(f"Minúsculas: '{texto.lower()}'")
print(f"Primeira letra maiúscula: '{texto.strip().capitalize()}'")

# Divisão de string
frase = "Python,Java,JavaScript,C++,Go"
linguagens = frase.split(",")
print(f"\nLinguagens: {linguagens}")

# Junção de strings
nova_frase = " | ".join(linguagens)
print(f"Reunidas: {nova_frase}")

# ========================================
# 7. TRATAMENTO DE EXCEÇÕES
# ========================================

print(f"\n⚠️ Tratamento de Exceções:")
print("-" * 30)

def dividir_numeros(a, b):
    """Função que demonstra tratamento de exceções"""
    try:
        resultado = a / b
        return f"Resultado: {a} ÷ {b} = {resultado}"
    except ZeroDivisionError:
        return "❌ Erro: Divisão por zero não é permitida!"
    except TypeError:
        return "❌ Erro: Os valores devem ser números!"
    except Exception as e:
        return f"❌ Erro inesperado: {e}"

# Testando tratamento de exceções
print(dividir_numeros(10, 2))
print(dividir_numeros(10, 0))
print(dividir_numeros("10", 2))

# ========================================
# 8. EXEMPLO PRÁTICO: ANÁLISE DE DADOS
# ========================================

print(f"\n📈 Exemplo Prático - Análise de Vendas:")
print("-" * 40)

vendas_mensais = {
    "Janeiro": 15000,
    "Fevereiro": 18000,
    "Março": 22000,
    "Abril": 19000,
    "Maio": 25000,
    "Junho": 21000
}

print("Vendas por mês:")
total_vendas = 0
melhor_mes = ""
maior_venda = 0

for mes, valor in vendas_mensais.items():
    print(f"  {mes}: R$ {valor:,.2f}")
    total_vendas += valor
    
    if valor > maior_venda:
        maior_venda = valor
        melhor_mes = mes

print(f"\n📊 Resumo:")
print(f"  Total de vendas: R$ {total_vendas:,.2f}")
print(f"  Média mensal: R$ {total_vendas / len(vendas_mensais):,.2f}")
print(f"  Melhor mês: {melhor_mes} (R$ {maior_venda:,.2f})")

# Crescimento mensal
meses = list(vendas_mensais.keys())
valores = list(vendas_mensais.values())

print(f"\n📈 Crescimento mensal:")
for i in range(1, len(valores)):
    crescimento = ((valores[i] - valores[i-1]) / valores[i-1]) * 100
    sinal = "📈" if crescimento > 0 else "📉" if crescimento < 0 else "➡️"
    print(f"  {meses[i-1]} → {meses[i]}: {sinal} {crescimento:+.1f}%")

print(f"\n✅ Exemplos básicos de Python concluídos!")