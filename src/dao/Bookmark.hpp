#ifndef DEF_BOOKMARK
#define DEF_BOOKMARK

#include <string>

class Bookmark {
public:
  void show_name();

private:
  int id;
  std::string name;
  std::string url;
  std::string time_created;
  std::string stamp;
  int rev_no;
};

#endif
