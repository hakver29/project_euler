#include <iostream>
#include <cmath>

using namespace std;

uint64_t sumDigits(uint64_t a){
    uint64_t S = 0;
    while(a != 0){
        S += (a % 10);
        a = (a - (a % 10))/10;
    }
    return S;
}

uint64_t myPow(uint64_t x, uint64_t p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * myPow(x, p-1);
}

bool checkPower(uint64_t a){
    uint64_t power = 1;
    uint64_t grunntall = sumDigits(a);
    while(myPow(grunntall,power) < a){
        power += 1;
    }
    if(myPow(grunntall,power) == a){
        return 1;
    }
    return 0;
}

bool possibleCandidate(uint64_t a){
    uint64_t x = sumDigits(a);
    if(x % 10 == 1 and a % 10 != 1){
        return false;
    }
    else if(x % 10 == 6 and a % 10 != 6){
        return false;
    }
    else if(x % 10 == 0 and a % 10 != 0){
        return false;
    }
    return true;
}

int main(){
    for(int i = 10; i < 1000000000; i++){
        if(possibleCandidate(i) == 1){
            if(checkPower(i) == 1){
                cout << i << endl;
            }
        }
    }
}
