#include <iostream>
#include <algorithm>

using namespace std;

uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t mod)
{
    uint64_t x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1){
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}

uint64_t mod_exp(uint64_t grunntall, uint64_t exponent, uint64_t modulo){
    uint64_t grunntall_temp;
    if(modulo == 1){
        return 0;
    }
    else if(exponent == 0){
        return 1;
    }
    else if(exponent == 1){
        return grunntall % modulo;
    }
    else if(exponent % 2 == 0){
        grunntall = (grunntall*grunntall) % modulo;
        exponent /= 2;
        return mod_exp(grunntall,exponent,modulo) % modulo;
    }
    else if(exponent % 2 == 1){
        grunntall_temp = grunntall;
        grunntall = (grunntall*grunntall % modulo);
        exponent = (exponent-1)/2;
        return (grunntall_temp*mod_exp(grunntall,exponent,modulo)) % modulo;
    }
}

bool miller_rabin(uint64_t p,int iteration){
    if (p < 2){
        return false;
    }
    if (p != 2 && p % 2==0){
        return false;
    }
    uint64_t s = p - 1;
    while (s % 2 == 0){
        s /= 2;
    }
    for (int i = 0; i < iteration; i++){
        uint64_t a = rand() % (p - 1) + 1, temp = s;
        uint64_t mod = mod_exp(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1){
            mod = mod_mul(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0){
            return false;
        }
    }
    return true;
}

int main(){
    uint64_t N = 600851475143, X = N, it = 2, max = 0;;

    if (miller_rabin(N,10) == 1){
        cout << N << endl;;
    }
    else{
        while(X != 1){
            while(X % it == 0){
                max = it;
                X /= it;
            }
            it += 1;
        }
        cout << max << endl;
    }
}
