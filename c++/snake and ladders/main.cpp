#include <iostream>
#include "XAndYPosition.h"

using namespace std;

int main()
{
    XAndYPosition x;
    //test cases
    x.getNumber(1);
    x.getNumber(5);
    x.getNumber(9);
    x.getNumber(10);
    cout<<"-----------------------------\n";
    x.getNumber(15);
    x.getNumber(19);
    x.getNumber(20);
    cout<<"-----------------------------\n";
    x.getNumber(25);
    x.getNumber(30);
    cout<<"-----------------------------\n";
    x.getNumber(40);
    x.getNumber(99);
    x.getNumber(100);
    return 0;
}
