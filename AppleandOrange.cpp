#include <bits/stdc++.h>
#include <vector>
#include <string>

using namespace std;

vector<string> split_string(string);

// Complete the countApplesAndOranges function below.
void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
    int m = apples.size();
    int n = oranges.size();
    int cnt_app = 0;
    int cnt_org = 0;
    for(int i=0; i<m; i++){
        int temp_app;
        temp_app = a + apples[i];
        if(temp_app >= s && temp_app <= t){
            cnt_app += 1;
        }
    }
    for(int i=0; i<n; i++){
        int temp_org;
        temp_org = b + oranges[i];
        if(temp_org >= s && temp_org <= t){
            cnt_org += 1;
        }
    }

    cout << cnt_app << endl;
    cout << cnt_org << endl;
}
