#include <iostream>

using namespace std;

int main(){
	int n, total = 0;

	cin >> n;

	for (int i = 0; i < n; i++){
		if (i%3 == 0 || i%5 == 0)
			total += i;
	}

	cout << total << endl;
}
