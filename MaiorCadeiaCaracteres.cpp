#include <iostream>

using namespace std;

//|____________________________________________________
//|Aluno: Lucas Macedo da Silva                       |
//|Turma A02 Projeto e Analise de Algoritmos I        |
//|Implementação C++:                                 |
//|Caracterização de uma subsequência comum mais longa|
//|____________________________________________________

int main(int argc, char *argv[])
{
    string X[] = {"1", "0", "0", "1", "0", "1", "0", "1" };
    string Y[] = {"0", "1", "0", "1", "1", "0", "1", "1", "0"};

    int m = 9, n = 10;
    int c[m][n];
    string b[m][n];



    for (int i = 0; i < m; ++i) {
        c[i][0] = 0;
    }
    for (int i = 0; i < n; ++i) {
        c[0][i] = 0;
    }

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; ++j) {
            if(X[i-1] == Y[j-1]){
                c[i][j] = c[i-1][j-1] + 1;
                b[i][j] = "\\";
            }else{
                if(c[i-1][j] >= c[i][j-1]){
                    c[i][j] = c[i-1][j];
                    b[i][j] = "|";
                }
                else
                {
                    c[i][j] = c[i][j-1];
                    b[i][j] = "-";
                }
            }
        }
    }


    cout<<endl;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if(b[i][j] != "\\" && b[i][j] != "|" && b[i][j] != "-")
                cout<<" ";
            else
                cout<<b[i][j];
            cout<<c[i][j]<<"\t";
        }
        cout<<endl;
    }
    cout<<endl;


    return 0;
}
