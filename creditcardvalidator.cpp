#include <iostream>

int sumoddnum(std::string cnum);
int sumevennum(std::string cnum);
int sumsplitdigit(int digits);

int main() {
    std::string cardnumber;
    int result;

    std::cout << "Enter cedit card number: ";
    std::cin >> cardnumber;

    result = sumevennum(cardnumber) + sumoddnum(cardnumber);

    if(result % 10 == 0) {
        std::cout << "Credit card number is valid\n";
    }
    else {
        std::cout << "Credit card number is invalid\n";
    }
}

int sumoddnum(std::string cnum) {
    int sum = 0;

    for(int i = cnum.size()-1; i >= 0; i-=2) {
        sum+=(cnum[i]-'0');
    }

    return sum;
}
int sumevennum(std::string cnum) {
    int sum = 0;

    for(int i = cnum.size()-2; i >= 0; i-=2) {
        sum+=sumsplitdigit((cnum[i]-'0')*2);
    }

    return sum;
}
int sumsplitdigit(int digits) {
    return ((digits%10) + ((digits/10) % 10));
}