#include <bits/stdc++.h>
#include <iostream>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


/*
 * Complete the 'getOneBits' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER n as parameter.
 */

vector<int> getOneBits(int n) {
    vector<int> result;
    result.push_back(0);
    
    int offset = 0;
    unsigned int mask = 1 << 31;
    // 0b100000000000000000000;
    // 5 = 0b0000 0000 0000 0101
    // offset = 13
    
    while ((mask & (n << (offset))) == 0) {
        offset++;
    }
    
    // 0101
    // i = 1
    // 0101 << 1 = 1010
    // 1010 & 1000 = 1000 != 0
    // offset = 1
    // 
    
    for (int i = offset; i < 32; i++) {
        if ((mask & (n << i)) != 0) {
            // i = 1
            // offset = 1
            // 1 - 1 + 1
            /// i = 3, offset = 1, push_back(3-1+1)

            result.push_back(i - offset + 1);
        }    
    }
    
    // [0, 1, 5, 10] 
    // [3, 1, 5, 10]
    result[0] = result.size() - 1;
    return result;
}

#if 0
int main() {
    vector<int> result = getOneBits(161);

    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i];

        if (i != result.size() - 1) {
            std::cout << "\n";
        }
    }
}
#endif

#if 1
int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<int> result = getOneBits(n);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
#endif

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
