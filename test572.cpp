#include <iostream>

using namespace std;

bool mult(int a,int b,int c,int d,int e,int f,int g,int h,int i){
    int a1 = (a*a + b*d+c*g);
    int e1 = (e*e + b*d + f*h);
    int i1 = (i*i + c*g + f*h);
    int b1 = (a*b + b*e + c*h);
    int c1 = (a*c + c*i + b*f);
    int f1 = (e*f + f*i + d*c);
    int d1 = (a*d + d*e + f*g);
    int g1 = (a*g + g*i + h*d);
    int h1 = (i*h + h*e + g*b);
    if(a1 == a && b1 == b && c1 == c && d1 == d && e1 == e && f1 == f && g1 == g && h1 == h && i1 == i){
        return 1;
    }
    else{
        return 0;
    }
}

main(){
    int X = 0;
    int n;
    int a,b,c,d,e,f,g,h,i;
    cin >> n;
    for(int a = -n; a <= n; a++){
        for(int b = -n; b <= n; b++){
            for(int c = -n; c <= n; c++){
                for(int d = -n; d <= n; d++){
                    for(int e = -n; e <= n; e++){
                        for(int f = -n; f <= n; f++){
                            for(int g = -n; g <= n; g++){
                                for(int h = -n; h <= n; h++){
                                    for(int i = -n; i <= n; i++){
                                        X += mult(a,b,c,d,e,f,g,h,i);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << X << endl;
}
