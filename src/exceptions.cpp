#include <iostream>
#include <exception>
#include <chrono>
#include <cstring>


using namespace std;

constexpr size_t ITERATIONS = 1000000UL;

invalid_argument errcode_funciton() {
    return invalid_argument("error");
}

void throwning_function() {
    throw invalid_argument("error");
}

size_t test_exception() {
    size_t errors = 0;

    for (size_t i = 0; i < ITERATIONS; i++) {
        try {
            throwning_function();
        } catch(const invalid_argument& e) {
            errors += 1;
        }
    }

    return errors;
}

size_t test_errcode() {
    size_t errors = 0;

    for (size_t i = 0; i < ITERATIONS; i++) {
        invalid_argument err = errcode_funciton();
        if (strlen(err.what()) > 0) {
            errors += 1;
        }
    }

    return errors;
}

int main(int argc, char* argv[]) {
    {
        auto start = chrono::system_clock::now();
        test_exception();
        cout << "exceptions: " << chrono::duration_cast<chrono::microseconds>(chrono::system_clock::now() - start).count()  << endl;
    }

    {
        auto start = chrono::system_clock::now();
        test_errcode();
        cout << "errcode: " << chrono::duration_cast<chrono::microseconds>(chrono::system_clock::now() - start).count()  << endl;
    }
}