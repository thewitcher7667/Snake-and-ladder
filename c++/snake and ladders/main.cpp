#include <iostream>
#include "XAndYPosition.h"
#include "Player.h"

using namespace std;

void board(int playerPosition)
{
  XAndYPosition y;
  for(int i =1;i<=100;i++)
  {
      if(i == playerPosition)
      {
          cout<<"[X]"<<" ";
          continue;
      }
      int d = i/10;
      bool b = d%2 != 0;
      if(y.isInteger((double) i/10))
      {
        if(b)
        {
           cout<<"["<<i<<"]"<<" ";
        }
        else
        {
           cout<<"["<<((i/10)-1)*10+1<<"]"<<" ";
        }
        cout<<"\n";
      }
      else if(b)
      {
        int newd = 11-(i- d*10) + (d*10);
        cout<<"["<<newd<<"]"<<" ";
      }
      else
      {
        cout<<"["<<i<<"]"<<" ";
      }
  }
}

int dice()
{
   return(rand() % 6)+1;
}

int main()
{
    Player player1;
    board(1);
    board(10);board(16);board(20);board(21);board(100);
    while(player1.currentPosition < 100)
    {
       cout<<"press one to play"<<"\n";
       int play;
       cin>>play;
       if (play != 1)
       {
           return 0;
       }
       int random = dice();
       player1.currentPosition = player1.currentPosition + random;
       board(player1.currentPosition);
       cout<<player1.currentPosition<<endl;
       cout<<dice<<endl;
    }

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
