#include <iostream>
#include "point.h"
#include "vector2.h"
#include "line_segment.h"
#include "triangle.h"

using namespace std;

int main() {
    Point p1(-1, -1);
    Point p2(1, 1);

    //prezentacja klasy punktu
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl;
    cout << "Koordynaty P2: " << p2.getX() << " " << p2.getY() << endl;
    cout << "Dystans pomiedzy P1 i P2: " << p1.distanceTo(p2) << endl;
    cout << "Przesuniecie P1 o Wektor [2,5]" << endl;
    p1.vectorOffset(Vector2(2, 5));
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl;
    cout << "Obrot P1 wokol P2 o 30 stopni" << endl;
    p1.rotate(p2, 30);
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl;
    cout << "Odbicie P1 wzgledem osi OX" << endl;
    p1.xAxisSymetry();
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl;
    cout << "Odbicie P1 wzgledem osi OY" << endl;
    p1.yAxisSymetry();
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl;
    cout << "Odbicie P1 wzgledem punkty P2" << endl;
    p1.pointSymetry(p2);
    cout << "Koordynaty P1: " << p1.getX() << " " << p1.getY() << endl << endl;

    //prezentacja klasy odcinka
    LineSegment l1(Point(4, 5), Point(-4, 15));
    LineSegment l2(Point(2, 1), Point(5, 15));
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Dlugosc L1: " << l1.length() << endl;
    cout << "Przesuniecie L1 o wektor [3,4]" << endl;
    l1.vectorOffset(Vector2(3, 4));
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Obrot L1 wokol P1 o 30 stopni" << endl;
    l1.rotate(p1, 30);
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Odbicie L1 wzgledem osi OX" << endl;
    l1.xAxisSymetry();
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Odbicie L1 wzgledem osi OY" << endl;
    l1.yAxisSymetry();
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Odbicie L1 wzgledem punktu P1" << endl;
    l1.pointSymetry(p1);
    cout << "Koordynaty jednego konca L1: " << l1.getA().getX() << " " << l1.getA().getY() << endl;
    cout << "Koordynaty drugiego konca L2: " << l1.getB().getX() << " " << l1.getB().getY() << endl;
    cout << "Czy L1 jest rownolegly wobec L2? : " << l1.isParallel(l2) << endl;
    cout << "Czy L1 jest prostopadly wobec L2? : " << l1.isPerpendicular(l2) << endl;
    cout << "Czy L1 zawiera P1? : " << l1.containsPoint(p1) << endl << endl;

    //prezentacja klasy trojkata
    Triangle t1(Point(-10, -10), Point(10, -10), Point(0, 10));
    Triangle t2(Point(-9, -9), Point(2, -2), Point(0, 2));
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;
    cout << "Czy T1 zawiera P1? : " << t1.containsPoint(p1) << endl;
    cout << "Czy T1 zawiera T2? : " << t1.containsTriangle(t2) << endl;
    cout << "Czy T1 jest rozlaczny wzgledem T2? : " << t1.isDisjoint(t2) << endl;
    cout << "Pole T1: " << t1.area() << endl;
    cout << "Obwod T1: " << t1.perimeter() << endl;
    cout << "Przesuniecie T1 o wektor [-1,2]" << endl;
    t1.vectorOffset(Vector2(-1, 2));
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;
    cout << "Obrot T1 wokol punktu P1 o 30 stopni" << endl;
    t1.rotate(p1, 30);
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;
    cout << "Odbicie T1 wzgledem osi OX" << endl;
    t1.xAxisSymetry();
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;
    cout << "Odbicie T1 wzgledem osi OY" << endl;
    t1.yAxisSymetry();
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;
    cout << "Odbicie T1 wzgledem punktu P1" << endl;
    t1.pointSymetry(p1);
    cout << "Koordynaty jednego wierzcholka T1: " << t1.getA().getX() << " " << t1.getA().getY() << endl;
    cout << "Koordynaty drugiego wierzcholka T1: " << t1.getB().getX() << " " << t1.getB().getY() << endl;
    cout << "Koordynaty trzeciego wierzcholka T1: " << t1.getC().getX() << " " << t1.getC().getY() << endl;


    return 0;
}