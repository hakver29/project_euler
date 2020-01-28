#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int numberOfDivisors(int n){
    int numberOfDivisors = 0;
    for(int i = 1; i <= sqrt(n); i++){
        if(n % i == 0){
            if(n / i == i){
                numberOfDivisors += 1;
            }else{
                numberOfDivisors += 2;
            }
        }
    }
    return numberOfDivisors;
}

int main(){
    int cnt = 0;

    int div;
    vector<int> Divisors;
    for(int n = 2; n < 10000000; n++){
        div = numberOfDivisors(n);
        Divisors.push_back(div);
    }

    for(int i = 0; i < Divisors.size(); i++){
        if(i != Divisors.size() - 1){
            if(Divisors[i] == Divisors[i+1]){
                cnt += 1;
            }
        }
    }

    return cnt;
}
