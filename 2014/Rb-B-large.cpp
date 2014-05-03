#include <iostream>
#include <fstream>
#include "string.h"
using namespace std;

int main() {

    std::ifstream input("input.in");
    std::ofstream output("output.out");

    //Forget this, the O(n^2) algorithm.....
    //need refactor
    int cases;
    input >> cases;
    cout << cases;
    int k;
    for (k=0;k<cases;k++){
        cout << "I'm alive";
        int firstNum, secondNum, goal = 0;
        input >> firstNum,secondNum, goal;
        int i,j,counter = 0;
        for (i=0;i<firstNum;i++) {
            for (j=0;j<secondNum;j++){
                int sum = firstNum & secondNum;
                cout << sum;
                if (sum< goal)
                    counter ++;
            }
        }
        output << "Case " << (k+1) << ": " << counter<<endl;
    }
    return 0;
}
