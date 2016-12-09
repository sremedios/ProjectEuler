#include <iostream>

using namespace std;

int FibCalc(int n){
	if (n <= 0) return 0;
	if (n == 1) return 1;
	if (n == 2) return 2;
	else{
		return FibCalc(n-1) + FibCalc(n-2);
	}

}

int main(){

	int count = 0;
	int n;

	cin >> n;

	for (int i = 1; i <= n; i++){
		if (FibCalc(i) <= 4000000 && FibCalc(i)%2 == 0){
			count += FibCalc(i);
		}
		else if (FibCalc(i) >4000000){
			break;
		}

	}

	cout << count << endl;

	return 0;
}
