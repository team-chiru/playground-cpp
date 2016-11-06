#include "dao/header/Bookmark.hpp"
#include "dao/header/BookmarkDAO.hpp"
#include <iostream>

using namespace std;

int main() {
  cout << "Hello World!" << endl;

  Bookmark b = Bookmark::Bookmark();
  BookmarkDAO dao = BookmarkDAO::BookmarkDAO();

  dao.init();

  return 0;
}
