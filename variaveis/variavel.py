# Variáveis:

# Variáveis numéricas

numero_inteiro = 10
numero_flutuante = 3.14

# Variáveis de texto (strings)

nome = "João"
sobrenome = "Silva"

# Variáveis booleanas

ativo = True
desativado = False

# Variáveis compostas em Python:

# Listas: coleção ordenada de itens, mutável

lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ["a", "b", "c", "d"]

# Tuplas: coleção ordenada de itens, imutável

tupla_numeros = (1, 2, 3, 4, 5)
tupla_strings = ("a", "b", "c", "d")

# Dicionários: coleção de pares chave-valor

dicionario_pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Conjuntos: coleção não ordenada de itens únicos

conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_letras = {"a", "b", "c", "d"}

# Variáveis mais avançadas em Python:

# Funções: blocos de código reutilizáveis

def somar(a, b):
    return a + b

# Classes: estruturas para criar objetos

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Objetos: instâncias de classes

pessoa1 = Pessoa("Maria", 25)

# Módulos: arquivos contendo definições e declarações Python

import math

# Arquivos: manipulação de arquivos no sistema

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
arquivo.close()
