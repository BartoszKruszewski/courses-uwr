#include <iostream>
#include <float.h>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
	int x, y;
};

struct Answear {
    Point a, b, c; 
    double p;
};

double dist(Point a, Point b) {
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

double perimeter(Point a, Point b, Point c) {
    return dist(a, b) + dist(b, c) + dist(c, a);
}

Answear brute(Point P[], int n, double p) {
	double min = p;
    int mi = 0, mj = 0, mk = 0;
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n && (P[j].y - P[i].y) < min; j++) {
			double distIJ = dist(P[i], P[j]);
			for (int k = j + 1; k < n && (P[k].y - P[j].y) < min; k++) {
				double distKJ = dist(P[k], P[j]);
				double distKI = dist(P[k], P[i]);
				double actualP = distIJ + distKJ + distKI;
				if (actualP < min) {
					min = actualP;
					mi = i; mj = j; mk = k;
				}
			}
		}
			
	return {P[mi], P[mj], P[mk], min};
}

Answear getMin(Point Px[], Point Py[], int n)
{	
	if (n <= 5) return brute(Py, n, DBL_MAX);
	
	int mid = n / 2;
	Point midPoint = Px[mid];

	Point Pyl[mid], Pyr[n - mid];
	int li = 0, ri = 0;
	for (int i = 0; i < n; i++) {
        if ((Py[i].x < midPoint.x || (Py[i].x == midPoint.x && Py[i].y < midPoint.y)) && li < mid)
			Pyl[li++] = Py[i];
        else 
			Pyr[ri++] = Py[i];
	}

    Answear left = getMin(Px, Pyl, mid);
    Answear right = getMin(Px + mid, Pyr, n - mid);
    Answear m = left.p < right.p ? left : right;

	int j = 0;
	Point strip[n];
	for (int i = 0; i < n; i++)
		if (abs(Py[i].x - midPoint.x) <= m.p)
			strip[j++] = Py[i];
	
	Answear s = brute(strip, j, m.p);

	return s.p < m.p ? s : m;
}

int main()
{
	int n;
	cin >> n;

	Point Px[n], Py[n];

	for (int i = 0; i < n; i++) {
		cin >> Px[i].x >> Px[i].y;
		Py[i] = Px[i];
	}

	sort(Px, Px + n, [](Point a, Point b) {return a.x < b.x || (a.x == b.x && a.y < b.y);});
	sort(Py, Py + n, [](Point a, Point b) {return a.y < b.y;});

    Answear m = getMin(Px, Py, n);

	cout << m.a.x << " " << m.a.y << endl;
	cout << m.b.x << " " << m.b.y << endl;
	cout << m.c.x << " " << m.c.y << endl;
	//cout << m.p << endl;
	return 0;
}