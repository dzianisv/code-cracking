#include <iostream>
#include <future>
#include <thread>

using namespace std;

void routine(future<bool>&& f) {
    cout << "starting routine" << endl;
    f.get();
    cout << "finishing routine" << endl;
}

int main(int argc, const char** argv)
{
    std::array<thread, 10> threads;

    for (size_t i = 0; i < threads.size(); i++) {
        promise<bool> p;
        future<bool> f = p.get_future();
        threads[i] = thread(routine, std::move(f));
    }

    for (auto&& t: threads) {
        t.join();
    }

    return 0;
}