#include <iostream>
#include <array>

using namespace std;

int main()
{
	array <int, 3>obj = {12,23,34};							// array of int type having size 10
    for(int i=0; i<3; i++)
        cout<<obj[i]<<endl;
    return 0;
}
