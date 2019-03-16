#include <bits/stdc++.h>
#include <string>
#include <vector>

using namespace std;

/*
 * Complete the timeConversion function below.
 */
string timeConversion(string s) {
    /*
    * Write your code here.
    */
    // Get hours
    int h1 = s[0] - '0';
    int h2 = s[1] - '0';
    int hh = h1*10 + h2 ;
    string ans = "00:00:00"; 

    // AM
    if(s[8] == 'A'){
        if(hh==12){
            ans[0] = 0 + '0' ;
            ans[1] = 0 + '0';
            for(int i = 2; i < 8; i++){
                ans[i] = s[i];
            }
        }else{
            ans[0] = h1 + '0';
            ans[1] = h2 + '0';
            for (int i = 2; i < 8; i++){
                ans[i] = s[i];
            }
        }
    }
    // PM
    else{
        if(hh == 12){
            ans[0] = 1 + '0';
            ans[1] = 2 + '0';
            for (int i = 2; i < 8; i++) {
                ans[i] = s[i];
            }
        }else{
            int temp_hh = hh + 12;
            int temp_h1 = temp_hh / 10;
            int temp_h2 = temp_hh % 10;
            ans[0] = temp_h1 + '0';
            ans[1] = temp_h2 + '0';
            for (int i = 2; i < 8; i++) {
                ans[i] = s[i];
            }
        }
    }     
    return ans;
}
