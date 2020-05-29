#include <array>
#include <list>
#include <iostream>
#include <algorithm>

using namespace std;

/*
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:
insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.
To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).
Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations.
Example
For queryType = ["insert", "insert", "addToValue", "addToKey", "get"] and query = [[1, 2], [2, 3], [2], [1], [3]], the output should be hashMap(queryType, query) = 5.
 The hashmap looks like this after each query:
1 query: {1: 2}
2 query: {1: 2, 2: 3}
3 query: {1: 4, 2: 5}
4 query: {2: 4, 3: 5}
5 query: answer is 5
The result of the last get query for 3 is 5 in the resulting hashmap.

*/
template <typename T, int Buckets = 16>
class hashmap_t {
public:
    hashmap_t() = default;

    void insert(size_t key, const T& value) {
        size_t k = key % map.size();
        map[k].push_back(std::make_pair(key,value));
    }

    T& get(size_t key) {
        size_t k = key % map.size();
        auto&& bucket = map[k];
        return std::find_if(bucket.begin(), bucket.end(), [key](const std::pair<size_t, T>& item) {
            if (item.first == key) {
                return true;
            }
        })->second;
    }

    void addToValue(const T& value) {
        for (auto&& bucket: map) {
            for (auto&& item: bucket) {
                item.second += value;
            }
        }
    }

    void addToKey(size_t key) {
        auto old_map = std::move(map);
        for (auto&& bucket: old_map) {
            for (auto&& item: bucket) {
                insert(item.first+key, item.second);
            }
        }
    }

    void print() {
        cout << "{";
        size_t items = 0;
        for (auto&& bucket: map) {
            for (auto&& item: bucket) {
                if (items>0) {
                    cout << ", ";
                }
                cout << item.first << ":" << item.second;
                items += 1;
            }
        }
        cout << "}" << endl;
    }
private:
    std::array<std::list<std::pair<size_t, T>>, Buckets> map;
};

int main(int argc, char* argv[]) {
    hashmap_t<int> m;
    m.insert(1,2);
    cout << "1 query: "; m.print();
    m.insert(2,3);
    cout << "2 query: "; m.print();
    m.addToValue(2);
    cout << "3 query: "; m.print();
    m.addToKey(1);
    cout << "4 query: "; m.print();
    cout << "5 query: " << m.get(3) << endl;
}