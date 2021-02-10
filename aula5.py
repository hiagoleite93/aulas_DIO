calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']

print(soma(10, 5))
