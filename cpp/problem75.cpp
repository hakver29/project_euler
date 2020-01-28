#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

bool is_present(vector<int> S, int n){
    if(find(S.begin(), S.end(), n) != S.end()){
        return true;
    }else{
        return false;
    }
}

bool is_sqrd(int n){
    int x;
    x = int(sqrt(n));
    if(x*x == n){
        return true;
    }else{
        return false;
    }
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int not_both_odd(int a, int b){
    if(a % 2 == 1 && b % 2 == 1){
        return false;
    }
    return true;
}

// generate all pythagorean triples
// https://en.wikipedia.org/wiki/Pythagorean_triple
int main(){
    vector<int> S;
    int M;
    int bound = 1500000; // Cannot be larger than 750,000
    int m,n,k,l;
    for(int n = 1; n < bound; n++){
        for(int m = n+1; m < 867; m++){
            if(gcd(m,n) == true && not_both_odd(m,n) == true){
                k = 1;
                l = 2*k*m*m + 2*k*m*n;
                while(l <= bound){
                    S.push_back(l);
                    k += 1;
                    l = 2*k*m*m + 2*k*m*n;
                }
            }
        }
    }
    sort( S.begin(), S.end() );
    //S.erase( unique( S.begin(), S.end() ), S.end() );

    M = 0;
    for(int i = 0; i < S.size(); i++){
        if(i == 0){
            if(S[i] == S[i+1]){
                M += 1;
            }
        }else if(i == S.size()-1){
            if(S[i] == S[i-1]){
                M += 1;
            }
        }else{
            if(S[i] == S[i-1] || S[i] == S[i+1]){
                M += 1;
            }
        }
    }
    cout << S.size() - M << endl;
}
