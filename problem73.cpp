#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

struct frac{
    int n;
    int d;
};

bool operator==(const frac& lhs, const frac& rhs){
    if(lhs.d == rhs.d && lhs.n == rhs.n){
        return true;
    }else{
        return false;
        }
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main(){
    vector<frac> S;
    frac X;
    double upper,lower;
    upper = 1/float(2);
    lower = 1/float(3);
    int x,y,m;
    int N = 0;
    for(int d = 1; d <= 12000; d++){
        for(int n = 1; n <= d; n++){
            m = gcd(n,d);
            if(m == 1){
                if(n/float(d) > lower && n/float(d) < upper){
                    N += 1;
                }
            }
        }
    }
    cout << N << endl;
}
