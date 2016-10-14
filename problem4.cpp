#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isPalindrome(vector<int> P){
    vector<int> P_1;
    for(int i = P.size()-1; i >= 0; i--){
        P_1.push_back(P[i]);
    }
    for(int i = 0; i < P.size(); i++){
        if(P_1[i] != P[i]){
            return 0;
        }
    }
    return 1;
}

int main(){
    int max_palindrome = 0, X;
    for(int i = 100; i < 1000; i++){
        for(int j = 100; j < 1000; j++){
            vector<int> P;
            X = i*j;
            while(X != 0){
                P.push_back(X % 10);
                X = (X - (X % 10))/10;
            }
            if(isPalindrome(P) == 1 and i*j > max_palindrome){
                max_palindrome = i*j;
            }
        }
    }
    cout << max_palindrome << endl;
}
