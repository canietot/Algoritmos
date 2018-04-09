#include <iostream>
#include <ctime>
#include <ratio>
#include <chrono>

using namespace std::chrono;

int main()
{

    short min = 20;
    short max = 51;
    short retry = 10;
    int oper = 0;
    double tMean = 0.0;
    double tt = 0.0;
    double tMeans [max-min];
    double total =0.0;

    for (short T=min; T<max; T++) {

        short matriz1 [T][T];
        short matriz2 [T][T];
        short matriz3 [T][T];
        for(int i=0; i<T; i++) {
            matriz1[i][i] = (short)1;
            matriz2[i][i] = (short)2;
            matriz3[i][i] = (short)0;
        }
        oper = ((T*T*T) + (T*T*(T-1)));

        for (int m=0; m<retry; m++) {
            high_resolution_clock::time_point t1 = high_resolution_clock::now();
            for(int i=0; i<T; i++) {
                for(int j=0; j<T; j++) {
                    for(int k=0; k<T; k++) {
                        matriz3[i][j] += matriz1[i][k] * matriz2[k][j];
                    }
                }
            }
            high_resolution_clock::time_point t2 = high_resolution_clock::now();
            duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
            tt = (double) (time_span.count());
            tMean += (tt/oper);
        }

        tMeans[T-min] = (tMean/retry);
    }

    std::cout << "[";
    int ff = (sizeof(tMeans)/sizeof(tMeans[0]));
    for(int i=0; i<ff; i++) {
        std::cout << tMeans[i] << ", ";
        total += tMeans[i];
    }
    std::cout << "]" << std::endl;
    tMean= total/ff;
    std::cout << "El tiempo promedio por instruccion es: " <<tMean << std::endl;

    return 0;
}
