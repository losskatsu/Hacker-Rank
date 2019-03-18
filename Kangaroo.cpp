// 히든 문제 10개 

#include <bits/stdc++.h>
#include <string>
#include <vector>

using namespace std;

vector<string> split_string(string);

// Complete the kangaroo function below.
string kangaroo(int x1, int v1, int x2, int v2) {
    string s ; 
    if( (x2 > x1 && v2 >= v1) || (x1 > x2 && v1 >= v2) || (x1==x2 && x1 > x2) || (x1==x2 && x1 < x2)){
        s = "NO";
    }else{
        vector <int> tmp_x1 = {0};
        vector <int> tmp_x2 = {0};

        tmp_x1[0] = x1;
        tmp_x2[0] = x2;
        
        if( x1 > x2){
            int i = 0;
            while (tmp_x1[i] > tmp_x2[i]) {
                tmp_x1[i+1] = tmp_x1[i] + v1;
                tmp_x2[i+1] = tmp_x2[i] + v2;               
                if (tmp_x1[i+1] < tmp_x2[i+1]){ s = "NO"; return s;}
                if (tmp_x1[i+1] == tmp_x2[i+1]){ s = "YES"; return s;}
                i = i+1;
            }
        } else if (x1 < x2){
            int i = 0;
            while (tmp_x1[i] < tmp_x2[i]) {               
                tmp_x1[i+1] = tmp_x1[i] + v1;
                tmp_x2[i+1] = tmp_x2[i] + v2;                
                if (tmp_x1[i+1] > tmp_x2[i+1]){ s = "NO"; return s;}
                if (tmp_x1[i+1] == tmp_x2[i+1]){ s = "YES"; return s;}
                i = i+1;
            }
        } 
    }
    return s;
}
