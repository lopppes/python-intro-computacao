# Exemplo do uso do type para verificar o tipo de uma variável

x = 10
print(type(x))  # Saída: <class 'int'>

# Operador and - Retorna True se ambas as expressões forem verdadeiras
# e False se pelo menos uma delas for falsa

a = True
b = False
print(a and b)  # Saída: False

# Operador or - Retorna True se pelo menos uma das expressões for verdadeira
# e False se ambas forem falsas

print(a or b)   # Saída: True

# Operador not - Inverte o valor de uma expressão booleana

print(not a)    # Saída: False

# Expressões booleanas podem ser combinadas para criar condições mais complexas
# Exemplo: Verificar se um número está entre 10 e 20

num = 15
print(num > 10 and num < 20)  # Saída: True

# O operador 'is' também pode ser usado para verificar a igualdade de objetos
# Exemplo: Verificar se duas variáveis se referem ao mesmo objeto

lista1 = [1, 2, 3]
lista2 = lista1
print(lista1 is lista2)  # Saída: True
