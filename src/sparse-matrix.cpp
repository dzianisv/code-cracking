
#include <iostream>
#include <unordered_map>
#include <exception>
#include <cassert>

using namespace std;


template <typename T = int>
class sparse_t {
public:
  sparse_t(size_t width, size_t height, const T& def): width_(width), height_(height), def_(def)
  {}
  
  const T& get(size_t row, size_t column) const
  {
    if (row >= height_ || column >= width_) {
      throw invalid_argument("out of bound");
    }
   
    size_t i = row * width_ + column;
    auto v = data_.find(i);
    if (v != data_.end()) {
      return v->second;
    }
    
    return def_;
  }
  
  void set(size_t row, size_t column, const T& value) 
  {
    if (row >= height_ || column >= width_) {
      throw invalid_argument("out of bound");
    }
    
    size_t i = row * width_ + column;
    
    auto v = data_.find(i);
    if (v != data_.end()) {
      if (value == def_) {
        data_.erase(v);
      } else {
        v->second = value;
      }
    } else {
      data_.emplace(i, value);
    }
  }
  
private:
  unordered_map<size_t, T> data_;
  size_t width_;
  size_t height_;
  T def_;
};


int main() {
  sparse_t<int> data(8, 8, 0);
  
  for (size_t i: {-1, 8}) {
    try {
      data.get(i, i);
    } catch(const invalid_argument& e) {
      cerr << e.what() << endl;
    }
  }
  
  data.set(0, 0, 10);
  assert(data.get(0, 0) == 10);
  assert(data.get(1, 1) == 0);
  data.set(0, 0, 0);
  assert(data.get(0,0) == 0);

}
