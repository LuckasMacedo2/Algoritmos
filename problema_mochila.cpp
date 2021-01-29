/* --- Problema da mochila 0 ou 1 ---
* Autor: Lucas Macedo
* Versao: 1.0
*/

// - Elementos: Cada um possui um valor (v) e peso (w)
// Objetivo: Colocar elementos na mochila de forma a maximizar o valor dos elementos colocados na mochila
// A mochila possui uma capacidade máxima (W)
// Um elemento é representado por: (peso, valor)

// Conjunto de n elementos S
// Cada elemento possui um peso wi e um valor/beneficio bi


// --- Programação Dinâmica ---
// Equação dinâmica que relacione o problema com os subproblemas
// os subproblemas compõem o problema maior, a solução ótima é computada
// a partir das soluções ótimas dos outros subproblemas.

// O subproblema será calcular V[k, w] para encontrar a solução ótima para Sk
//  Sk = {elementos: 1, 2, ..., k}

// Onde V[i, j]
// i = 0, ..., k - 1
// j = 0, ..., w

// w: peso do elemento
// W: capacidade máxima da mochila
// b: beneficio do elemento
// k: 


// Logo V[k, w] =
//                  v[k - 1, w] se wk > W
//                  max {V[k - 1, w], V[k - 1, w - wk] + bk}, caso contrário

// O melhor subconjunto Sk que tem peso total W:
// é:
// 1) O melhor subconjunto S(k-1) que possui um peso total <= W
// 2) O melhor subconjunto S(k-1) que possui um peso total <= W - wk + elemento k

// O melhor subconjunto Sk que tem pesso total <= W contém o elemento o elemento k ou não.

// wk > W então o elemento k não pode ser parte da solução, pois senão o peso total
// seria maior que a capacidade máxima da mochila.

// wk <= W então o elemento k pode fazer parte da solução e escolhemos o caso com maior valor.

#include <iostream>
using std::cout;
using std::cin;
using std::string;
using std::endl;

// Matriz de ordem (n+1)(W+1)

int knapsack(int W, int wt[], int b[], int n){
    // Tabela 
    int V[n + 1][W + 1];

    //  Inicializando a primeira linha e coluna
    for (int w = 0; w <= W; w++)
    {
        V[0][w] = 0;
    }

    for (int i = 0; i <= n; i++)
    {
        V[i][0] = 0;
    }

    // Algoritmo
    for (int i = 1; i <= n; i++)
    {
        for (int w = 1; w <= W; w++)
        {
            // Elemento pode fazer parte da solução
            if (wt[i - 1] <= w) // Max
            {
                int valor = b[i - 1] + V[i - 1][w - wt[i - 1]];
                if (valor > V[i - 1][w])
                {
                    V[i][w] = valor;
                }else{
                    V[i][w] = V[i - 1][w];
                }
            }
            else{
                V[i][w] = V[i - 1][w];
            }
        }
        
    }
    
    // Retorna o valor máximo
    return V[n][W];
    
}

int main(){
    // Capacidade maxima da mochila
    int W = 20;

    // Número de elementos
    int n = 5;

    // Vetor com os valores (beneficios) de cada elemento
    int b[] = {3, 5, 8, 4, 10};

    // Vetor com os pesos de cada elemento
    int wt[] = {2, 4, 5, 3, 9};

    // Obter o máximo valor que pode ser colocado na mochila
    int max_valor = knapsack(W, wt, b, n);

    cout<<"Valor Maximo: "<<max_valor<<endl;

}

