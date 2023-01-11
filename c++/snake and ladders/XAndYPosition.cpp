#include <iostream>
#include <cmath>
#include "XAndYPosition.h"
using namespace std;

XAndYPosition::XAndYPosition()
{
    number = 0;
    XAndY[0] = 0;
    XAndY[1] = 0;
}

void XAndYPosition::getNumber(int n)
{
  number = n;
  getX();
  getY();
  XAndY[0] = getX();
  XAndY[1] = getY();
  cout<<"x : "<<XAndY[0]<<" y : "<<XAndY[1]<<endl;
}

int XAndYPosition::getX()
{

   //cout<<(number/10)<<"\n";
   int numDevideTen = number/10;
   bool checkEven = numDevideTen%2 == 0;
    if(isInteger((double) number/10))
    {
        if(checkEven)
        {
          return 1;
        }
        else
        {
           return 10;
        }
    }

    double num =(double) number/10;
    int decimalPart = (num - floor(num))*10;
   if(checkEven)
   {
     //get decimal part
     return decimalPart;
   }
   else
   {
     return 11 - decimalPart;
   }
}

int XAndYPosition::getY()
{
    if(number < 11)
    {
        return 10;
    }
    //check number is tenths or not
    if(isInteger((double) number/10))
    {
        return (number/10 - 1 )*10 + 10;
    }

    return (number/10)*10 + 10;
}

bool XAndYPosition::isInteger(double d)
{    //using FMOD because module is for integers
    if ( fmod(d,1.0) == 0.0 )
    {
        return true;
    }
    else
    {
      return false;
    }
}


