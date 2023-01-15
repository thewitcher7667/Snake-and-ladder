#ifndef XANDYPOSITION_H
#define XANDYPOSITION_H


class XAndYPosition
{
    public:
        XAndYPosition();
        void getNumber(int n);
        //helper fuctions
        bool isInteger(double d);

    protected:

    private:
        //current player position
        int number;
        //x and y of new position
        int XAndY[2];
        //main functiom
        int getX();
        int getY();
};

#endif // XANDYPOSITION_H
