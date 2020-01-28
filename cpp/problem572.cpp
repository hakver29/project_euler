
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct Str{
    int x;
    int y;
};

vector<Str> factors(int X, int n){
    vector<Str> A;
    if(X == 0){
        for(int i = -n; i <= n; i++){
            if(i == 0){
                A.push_back({0,0});
            }
            else{
                A.push_back({i,0});
                A.push_back({0,i});
            }
        }
    }
    else{
        for(int i = -n; i <= n; i++){
            if(i != 0 and X % abs(i) == 0 and (X/i == i or (X/i <= n and X/i >= -n))){
                A.push_back({i,X/i});
            }
        }
    }
    return A;
}

bool checkSolution(int a,int b,int c,int d,int e,int f,int g,int h,int i,int n){
    if(a*b + b*e + c*h != b or a*c + c*i + b*f != c or e*f + f*i + d*c != f or a*d + d*e + f*g != d or a*g + g*i + h*d != g or i*h + h*e + g*b != h)
        return false;
    else
        return true;
}

int cnt_func(int rnk,int n){
    int cntr = 0;
    for(int a = -n; a <= n; a++){
        for(int e = -n; e <= n; e++){
            int i;
            if(-n <= rnk-a-e && rnk-a-e <= n){
                i = rnk-a-e;
                vector<Str> X1,Y1,Z1;
                X1 = factors((a - a*a + e - e*e - i + i*i)/2,n);
                Y1 = factors((a - a*a - e + e*e + i - i*i)/2,n);
                Z1 = factors((-a + a*a + e - e*e + i - i*i)/2,n);
                int b,d,c,g,f,h;
                for(int x1 = 0; x1 < X1.size(); x1++){
                    for(int y1 = 0; y1 < Y1.size(); y1++){
                        for(int z1 = 0; z1 < Z1.size(); z1++){
                            b = X1[x1].x;
                            d = X1[x1].y;
                            c = Y1[y1].x;
                            g = Y1[y1].y;
                            f = Z1[z1].x;
                            h = Z1[z1].y;
                            cntr += checkSolution(a,b,c,d,e,f,g,h,i,n);
                        }
                    }
                }
            }
        }
    }
    return cntr;
}

int main(){
    int n;
    cin >> n;
    int cntr = 0;
    for(int rnk = 0; rnk <= 2; rnk++){
        cntr += cnt_func(rnk,n);
    }
    cout << cntr+1 << endl;
}
