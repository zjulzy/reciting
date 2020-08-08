#include <iostream>
using namespace std;

class Test {
public:
    static int counter;
    int i;
    Test() {
        i = counter;
        counter++;
        cout << "test " << i << " created" << endl;
    }
    ~Test() {
        cout << "test " << i << " destroyed" << endl;
    }
};

int Test::counter = 0;

Test copy1() {
    return Test();
}

Test copy2() {
    Test temp;
    return temp;
}

int main() {
    Test mytest1 = copy1();
    cout << "--------" << endl;
    Test mytest2;
    mytest2 = copy1();

    cout << "========" << endl;
    Test mytest3 = copy2();
    cout << "--------" << endl;
    Test mytest4;
    mytest4 = copy2();

    cout << "========" << endl;
    return 0;
}
