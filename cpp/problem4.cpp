#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool isPalindrome(vector<int> P){
    vector<int> P_1(P);
    reverse(P_1.begin(),P_1.end());
    if (equal(P.begin(), P.begin() + P.size(), P_1.begin()))
        return 1;
    return 0;
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
