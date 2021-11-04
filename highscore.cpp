#include <iostream>

using namespace std;

int score(int a, int b, int c) {
    if (a <= b && a <= c) {
        return(a*a + b*b + c*c + 7 * a);
    } else if (b <= c) {
        return(a*a + b*b + c*c + 7 * b);
    }  else {
        return(a*a + b*b + c*c + 7 * b);
    }
}


int highscore(int a, int b, int c, int d) {
    if (d == 0) {
        return score(a, b, c);
    } else {
        int mina, minb, minc, maxa, maxb, maxc;

        maxa = a;
        mina = a;
        maxb = b;
        minb = b;
        maxc = c;
        minc = c;

        if (a >= b && a >= c) {
            maxa++;
        } else if (b >= c) {
            maxb++;
        } else {
            maxc++;
        }

        if (a <= b && a <= c) {
            mina++;
        } else if (b >= c) {
            minb++;
        } else {
            minc++;
        }

        int hi, lo;
        hi = highscore(maxa, maxb, maxc, d-1);
        lo = highscore(mina, minb, minc, d-1);

        if (hi >= lo) {
            return (hi);
        } else {
            return(lo);
        }
    }
}

int main() {
    int n, a, b, c, d;
    cin >> n;

    for (int i; i < n-1; i++) {
        cin >> a >> b >> c >> d;

        int score = highscore(a, b, c, d);
        cout << score << endl;
    }
    return(0);
}