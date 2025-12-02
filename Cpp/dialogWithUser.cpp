#include <iostream>
#include <string>
using namespace std;
int main (){
    string name;
    cout << "what is your name?";
    cin >> name;
    cout << "Hello, " << name << "!";

}

int main (){
    int num1, num2, sum;
    cout << "Give me two numbers: ";
    cin >> num1 >> num2;
    sum = num1 + num2;
    cout << num1 << "+" << num2 << "=" << sum;
}