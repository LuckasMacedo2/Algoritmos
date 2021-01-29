# Problema do Caixeiro Viajante
# Autor: Lucas Macedo da Silva
# Meta Heuristica: Simulate Annealing

# Versao: 1.0


# Representacao do grafo

# Gerar numeros aleatorios
from random import random, randint, shuffle, uniform

from math import log, exp

# Plota graficos
#import matplotlib.pyplot as plt


class Grafo:
    # O grafo e representado por por um dicionario
    # A chave e uma tupla da forma (origem, destino)
    # O valor e o peso das arestas em origem e destino
    def __init__(self, grafo = {}, vertices = [], label = {}):
        """"
        Inicializa o objeto
        :param grafo: Um dicionario, contendo informacoes das arestas  A chave e uma tupla da forma (origem, destino)
        O valor e o peso das arestas em origem e destino
        :param vertices: Lista de vertices do grafo
        """
        self.grafo = grafo
        self.vertices = vertices
        self.label = label

    def get_peso(self, origem, destino):
        """"Retorna o valor do peso entre duas arestas
        :param origem: A cidade de origem
        :param destino: A cidade de destino
        """
        return self.grafo[(origem, destino)]

    def get_vertices(self):
        return self.vertices

    def imprimir_grafo(self):
        """"
        Retorna uma string contendo um aresta com peso e os vertices que a compoem
        """
        s = 'Origem\t\tDestino\t\tPeso\n'
        for valor in self.grafo:
            s = s + '\t{}\t\t\t{}\t\t {}\n'.format(valor[0], valor[1], self.grafo[valor])
        return s

    def imprimir_percurso1(self, percurso):
        l = len(percurso)
        s = 'Origem\t\tDestino\t\tPeso\n'
        custo = 0
        for i in range(0, l - 1):
            s = s + '\t{}\t\t\t{}\t\t {}\n'.format(percurso[i], percurso[i + 1],
                                                   self.grafo[(percurso[i], percurso[i + 1])])
            custo = custo + self.get_peso(percurso[i], percurso[i + 1])
        s = s + '\t{}\t\t\t{}\t\t {}\n'.format(percurso[-1], percurso[0], self.grafo[(percurso[-1], percurso[0])])
        s = s + f'Custo: [{custo + self.get_peso(percurso[-1], percurso[0])}]'
        return s

    def imprimir_percurso(self, percurso):
        l = len(percurso)
        s = 'Origem{}Destino{}Peso\n'.format(' ' * 29, ' ' * 27)
        m = 35
        custo = 0
        for i in range(0, l - 1):
            index = percurso[i]
            index_i = percurso[i + 1]
            s = s + '{}{}{}{}{}\n'.format(self.label[index], ' ' * (m - len(self.label[index])),self.label[index_i], ' ' * (m - len(self.label[index_i])),self.grafo[(percurso[i], percurso[i+1])])
            custo = custo + self.get_peso(percurso[i], percurso[i + 1])
        index = percurso[-1]
        index_i = percurso[0]
        s = s + '{}{}{}{}{}\n'.format(self.label[index], ' ' * (m - len(self.label[index])) ,self.label[index_i], ' ' * (m - len(self.label[index_i])), self.grafo[(percurso[-1], percurso[0])])
        #s = s + f'\nCusto: [{custo + self.get_peso(percurso[-1], percurso[0])}]'
        s = s + '\nCusto: [{}]'.format(custo + self.get_peso(percurso[-1], percurso[0]))
        return s

    def custo_percurso(self, vertices):
        """
        Retorna o custo do percurso entre os vertices
        :param vertices: Um vetor contendo os vertices que contem o percurso
        :return: Custo do percurso
        """
        l = len(vertices)
        custo = 0
        for i in range(0, l - 1):
            custo = custo + self.get_peso(vertices[i], vertices[i + 1])
        custo = custo + self.get_peso(vertices[-1], vertices[0])
        return custo


class SimulatedAnnealing:

    def __init__(self, grafo):
        self.T0 = 0
        self.Nk = 0
        self.grafo = grafo

    def inicializa_temp_inicial(self, fi, mi, custo_inicial):
        """"
        Inicializa a temperatura inicial
        :param fi: % de aceitacao em que as solucoes sao
        :param mi: % piores que a solucao inicial"""
        self.T0 = (mi / (-log(fi)))*custo_inicial

    def inicializa_n_tentativas(self, n):
        """"
        Inicializa a quantidade de tentativas
        :param n: Quantidades de tentativas a serem realizadas a cada nivel de temperatura"""
        self.Nk = n

    def gerar_solucao_inicial(self, vertices):
        """"
        Gera a solucao inicial, aleatoriamente
        :param vertices: A lista de vertices a serem escolhidos aleatoriamente"""
        shuffle(vertices)
        return vertices

    def gerar_nova_solucao(self, vertices):
        """"
        Gera a solucao vizinha
        :param vertices: Os verties que compoem a solucao atual
        :return a soluca vizinha"""
        x = 0
        y = 0
        while x == y:
            x = randint(1, len(vertices) - 1)
            y = randint(1, len(vertices) - 1)
        a = vertices[y]
        vertices[y] = vertices[x]
        vertices[x] = a
        return vertices

    def imprimir(self, s_atual, Tk):
        print('\n-----------------------------------------------------------')
        print(f'Temperatura: {Tk}\nCusto: {self.grafo.custo_percurso(s_atual)}\nPercurso:\n{self.grafo.imprimir_percurso(s_atual)}')
        print('-----------------------------------------------------------\n')

    def simulated_annealing(self, fi, mi, vi):
        # vi vertice inicial
        # Gera a solucao inicial
        vertices = self.grafo.get_vertices()[:]
        del(vertices[vi-1])
        s_atual = []
        s_atual.append(vi)
        s_atual[1:] = self.gerar_solucao_inicial(vertices)
        #s_atual[1:] = [i for i in range(2, 101)]
        #self.imprimir(s_atual, 10)
        # Inicializa a temperatura inicial
        self.inicializa_temp_inicial(fi, mi, self.grafo.custo_percurso(s_atual))

        # Iniciliza numero de tentativas
        self.inicializa_n_tentativas(len(s_atual))

        # Taxa de decrescimento da temperatura
        B = uniform(0.5, 0.9) # Constante que define o criterio de parada
        Tk = B * self.T0

        # Criterio de parada
        c_p = len(s_atual)

        # Extra
        vetor_custos = []
        vetor_temperaturas = []

        k = 0
        fi = 0
        while k < c_p:
            for L in range(0, self.Nk):
                s_nova = self.gerar_nova_solucao(s_atual[:])
                fi = self.grafo.custo_percurso(s_atual) # Custo do percurso atual
                fj = self.grafo.custo_percurso(s_nova)  # Custo do novo percurso

                if fj <= fi:
                    s_atual = s_nova[:]
                elif exp((fi - fj)/Tk) > random():
                    s_atual = s_nova[:]
                #self.imprimir(s_atual, Tk)

            # Extra
            vetor_custos.append(self.grafo.custo_percurso(s_atual))
            vetor_temperaturas.append(Tk)

            Tk = Tk * B
            k = k + 1

        x = [i for i in range(0, len(vetor_custos))]
        y = vetor_custos

        #figure = plt.figure()
        #ax = figure.add_subplot(111)
        #plt.plot(x, y, 'b*--')


        #plt.xlabel('Numero da tentativa')
        #plt.ylabel('Custo')
        #plt.title('Custo x Numero da tentativa')
        #plt.show()

        return s_atual


# Menor caminho 16 para qualquer grafo

VERTICE_INICIAL = 1


def grafo_estatico():

    # (origem, destino) : peso

    g = {
        # Vertice 1
        (1, 2): 500,
        (1, 3): 300,
        (1, 4): 700,
        (1, 5): 100,
        (1, 6): 100,
        # Vertice 2
        (2, 1): 500,
        (2, 3): 900,
        (2, 4): 400,
        (2, 5): 500,
        (2, 6): 700,
        # Vertice 3
        (3, 1): 100,
        (3, 2): 900,
        (3, 4): 300,
        (3, 5): 200,
        (3, 6): 900,
        # Vertice 4
        (4, 1): 700,
        (4, 2): 400,
        (4, 3): 300,
        (4, 5): 300,
        (4, 6): 800,
        # Vertice 5
        (5, 1): 100,
        (5, 2): 500,
        (5, 3): 200,
        (5, 4): 300,
        (5, 6): 200,
        # Vertice 6
        (6, 1): 100,
        (6, 2): 700,
        (6, 3): 900,
        (6, 4): 800,
        (6, 5): 200,
    }
    label = {1:'Central', 2:'Dep. de T.I.', 3:'Dep. de Segurança', 4:'Dep. de Desenvolvimento', 5:'Dep. de Administração', 6:'Dep. de Infraestrutura'}
    return g, [i for i in range(1, 7)], label


    return g


def teste():
    g, vertices, label = grafo_estatico()
    grafo = Grafo(g, vertices, label)

    sa = SimulatedAnnealing(grafo)

    solucao = sa.simulated_annealing(0.13, 0.01, VERTICE_INICIAL)
    print(grafo.imprimir_percurso(solucao))
    #print()
    #print(grafo.imprimir_percurso1(solucao))

    return grafo.custo_percurso(solucao)

def teste2():
    g, vertices, label = grafo_estatico()
    grafo = Grafo(g, vertices, label)

    sa = SimulatedAnnealing(grafo)

    for i in range(1, 7):
        v = []
        VERTICE_INICIAL = i
        print(i)
        for j in range (1, 10):
            solucao = sa.simulated_annealing(0.13, 0.01, VERTICE_INICIAL)
            #print(grafo.imprimir_percurso(solucao))
            v.append(grafo.custo_percurso(solucao))
        v.sort()
        print(v)


teste()

