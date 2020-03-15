#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
  int tamArr, numOp;

  cin >> tamArr;
  cin >> numOp;

  int arr[tamArr];
  int add = 0;
  for(int i = 0; i < tamArr; i++) {
    cin >> arr[i];
  }

  int op;
  int acc = 0;
  for(int i = 0; i < numOp; i++) {
    cin >> op;

    if(op == 1) {
      int index;
      cin >> index;
      index -= 1;
      int number;
      cin >> number;

      arr[index] = number - acc;
    }
    else if(op == 2){
      int add;
      cin >> add;
      acc += add;
    }
    else{
      int index;
      cin >> index;

      cout << arr[index - 1] + acc << endl;
    }
  }

}