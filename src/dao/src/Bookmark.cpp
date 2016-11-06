#include "../header/Bookmark.hpp"

using namespace std;
#include <iostream>;

Bookmark::Bookmark() {
  id = 1;
  name = "Bookmark";
  url = "www.test.com";
  time_created = "01/01/2015";
  stamp = "01/01/2016";
  rev_no = 5;
}

std::string Bookmark::get_name() { return this->name; }
