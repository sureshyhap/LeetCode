#include <iostream>
#include <string>

bool example1(std::string s);

int main(int argc, char* argv[]) {
  std::cout << std::boolalpha << example1("racecar") << '\n';  
  return 0;
}

bool example1(std::string s) {
  for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
    if (s[i] != s[j]) {
      return false;
    }
  }
  return true;
}
