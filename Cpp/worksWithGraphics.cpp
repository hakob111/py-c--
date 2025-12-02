#include "TXLib.h"
/*TX Library is a tiny graphics library for Win32 written in C++.
Brought to you by: ded32. See on https://sourceforge.net/projects/txlib/ */

 int main()
{
     txCreateWindow (800, 600);
     txSetPixel(10, 20, TX_MAGENTA);
     cout << std::hex << txGetPixel(10, 20);
}

 int main() 
{
     txCreateWindow(800, 600);
     txRectangle(50, 50, 100, 130);

}

 int main() {
     txCreateWindow(800, 600);
     POINT a[4] = {{40, 70}, {65, 55},{70, 55}, {70, 70}};
     POINT b[4] = {{75, 55}, {95, 55}, {110, 70}, {75, 70}};
     POINT c[8] = {{20, 95}, {20, 70}, {30, 70}, {60, 50}, {100, 50}, {120, 70}, {160, 80}, {160, 95}};
     txSetFillColor(TX_LIGHTBLUE);
     txPolygon(c, 8);
     txSetFillColor(TX_BLACK);
     txPolygon(a, 4);
     txSetFillColor(TX_GRAY);
     txCircle(50, 115, 13);
    txCircle(120, 95, 13);
 }

/*To fix the problem in the code above, create the correct variables and functions */

 void drawCarBody()
{
     POINT carBody[8] = {{20, 95}, {20, 70}, {30, 70}, {60, 50}, 
                         {100, 50}, {120, 70}, {160, 80}, {160, 95}};
     txSetFillColor(TX_LIGHTBLUE);
     txPolygon(carBody, 8);
}

 void drawCarWindows()
{
     txSetFillColor(TX_BLACK);
     POINT backWindow[4] = {{40, 70}, {65, 55},
                             {70, 55}, {70, 70}};
     txPolygon(backWindow, 4);
     POINT frontWindow[4] = {{75, 55}, {95, 55}, 
                             {110, 70}, {75, 70}};
     txPolygon(frontWindow, 4);
}

 void drawCarWheels(){
     txSetFillColor(TX_GRAY);
     txCircle(50, 95, 13);
     txCircle(120, 95, 13);
}


 int main() {
     txCreateWindow(800, 600);
     drawCarBody();
     drawCarWindows();
     drawCarWheels();

}


/*Argument in function and function declaration */
void drawCarBody(int x, int y, COLORREF color);
void drawCarWindows(int x, int y);
void drawCarWheels(int x, int y);
void drawCar(int, int, COLORREF);

void drawCarBody(int x, int y, COLORREF color){
    txSetFillColor(color);
    POINT carBody[8] = {{x, y}, {x, y-25}, {x+10, y-25}, {x+40, y-45}, 
                   {x+80, y-45}, {x+100, y-25}, {x+140, y-15}, {x+140, y}};
    txPolygon(carBody, 8);
}

void drawCarWindows(int x, int y){
    txSetFillColor(TX_BLACK);
    POINT backWindow[4] = {{x+20, y-25}, {x+45, y-40},
                            {x+50, y-40}, {x+50, y-25}};
    txPolygon(backWindow, 4);
    POINT frontWindow[4] = {{x+55, y-40}, {x+75, y-40}, 
                            {x+90, y-25}, {x+55, y-25}};
    txPolygon(frontWindow, 4);
}

void drawCarWheels(int x, int y){
    txSetFillColor(TX_GRAY);
    txCircle(x+30, y, 13);
    txCircle(x+100, y, 13);
}

void drawCar(int x, int y, COLORREF color){
    drawCarBody(x, y, color);
    drawCarWindows(x, y);
    drawCarWheels(x, y);
}

int main(){
    txCreateWindow(800, 600);
    drawCar(20, 95, TX_LIGHTBLUE);
    drawCar(100, 100, TX_RED);
}