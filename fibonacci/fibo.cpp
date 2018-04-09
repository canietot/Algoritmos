#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main()
{

    string a ="Para una variable de tipo ";
    string b =" se produce overflow con el Fibonacci numero: \t";
    string c="\t y el maximo fibonacci que puede ser almacenado es: ";
    string d="\t  y equivale al numero:  ";
    string e="  y equivale al numero:  ";

    short sa = 0;
    short sb = 1;
    short stempA = 0;
    int count = 1;;
    while (sb>0) {
        stempA = sa;
        sa = sb;
        sb = (short) (sb+stempA);
        count ++;
    }
    cout << a << "short" << b << count << c << count-1 << d << sa << endl;


    int ia = 0;
    int ib = 1;
    int itempA = 0;
    count = 1;
    while (ib>0) {
        itempA = ia;
        ia = ib;
        ib = ib+itempA;
        count ++;
    }
    cout << a << "entero" << b << count << c << count-1 << d << ia << endl;

    long la = 0;
    long lb = 1;
    long ltempA = 0;
    count = 1;
    while (lb>0) {
        ltempA = la;
        la = lb;
        lb = lb+ltempA;
        count ++;
    }
    cout << a << "long" << b << count << c << count-1 << d << la << endl;
    long long lla = 0;
    long long llb = 1;
    long long lltempA = 0;
    count = 1;
    while (llb>0) {
        lltempA = lla;
        lla = llb;
        llb = llb+lltempA;
        count ++;
    }
    cout << a << "long long" << b << count << c << count-1 << d << lla << endl;

    float fa = 0;
    float fb = 1;
    float ftempA = 0;
    count = 1;
    while (fb < std::numeric_limits<float>::infinity()) {
        ftempA = fa;
        fa = fb;
        fb = fb+ftempA;
        count ++;
    }
    cout << a << "float" << b << count << c << count-1 << d << fa << endl;

    double da = 0.0;
    double db = 1.0;
    double dtempA = 0.0;
    count = 1;
    while (db < std::numeric_limits<double>::infinity()) {
        dtempA = da;
        da = db;
        db = db+dtempA;
        count ++;
    }
    cout << a << "double" << b << count << c << count-1 << e << da << endl;

    return 0;
}
