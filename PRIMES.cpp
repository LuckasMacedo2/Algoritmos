#include <iostream>
using namespace std;


int main(){
    int x, y;

    cin>>x>>y;

    if (y < x){
        int temp = y;
        y = x;
        x = temp;
    }
    
    int ok = 1;
    for (int i = 2; i <= x; i++){
            if (x % i == 0 && y % i == 0) {
                
                ok = 0;
                break;
            }
    }

    if (ok){
        printf("%i e %i sao primos entre si\n", x, y);
    }
    else{
        printf("%i e %i nao sao primos entre si\n", x, y);
    }


}