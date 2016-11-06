#ifndef DEF_BOOKMARK_DAO
#define DEF_BOOKMARK_DAO

#include "Bookmark.hpp"
#include <string>

class BookmarkDAO {
public:
  BookmarkDAO();
  void init();
  void insert(Bookmark b);
  void deelete(Bookmark b);
  void read(Bookmark b);
  void update(Bookmark b);
  void list();

private:
  // Bookmark b;
};

#endif
