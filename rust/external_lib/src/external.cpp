#include "external.h"
#include <chrono>
#include <thread>
using namespace std;

void do_it() {
    std::this_thread::sleep_for(5000ms);
    throw "not implemented";
}