/**
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, for every step it was noted if it was an uphill, , or a downhill, step. Hikes always start and end at sea level, and each step up or down represents a

unit change in altitude. We define the following terms:

    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

Example

The hiker first enters a valley units deep. Then they climb out and up onto a mountain

units high. Finally, the hiker returns to sea level and ends the hike.

Function Description

Complete the countingValleys function in the editor below.

countingValleys has the following parameter(s):

    int steps: the number of steps on the hike
    string path: a string describing the path

Returns

    int: the number of valleys traversed

Input Format

The first line contains an integer
, the number of steps in the hike.
The second line contains a single string , of

characters that describe the path.

Constraints

Sample Input

8
UDDDUDUU

Sample Output

1

Explanation

If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

_/\      _
   \    /
    \/\/

The hiker enters and leaves one valley.
*/

#include <bits/stdc++.h>
#include <exception>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int countingValleys(int steps, string path) {
    size_t valleys = 0;
    int altitude = 0;
    
    for (const char step: path) {
        switch(step) {
            case 'U':
                altitude += 1;
                break;
            case 'D':
                if (altitude == 0) {
                    valleys += 1;
                }
                altitude -= 1;
                break;
            default:
                throw invalid_argument("invalid step");
        }
    }
    
    return valleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string steps_temp;
    getline(cin, steps_temp);

    int steps = stoi(ltrim(rtrim(steps_temp)));

    string path;
    getline(cin, path);

    int result = countingValleys(steps, path);

    fout << result << "\n";

    fout.close();

    return 0;
}

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

