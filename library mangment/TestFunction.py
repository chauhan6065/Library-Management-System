from User import Member, Librarian


lib = Librarian("Ankit Shukla", "Lucknow", 23, "LKO222021", "JKP1997")
print(lib)
lib.addBook("War and Peace", "Leo Tolstoy", "1867")
lib.addBookItem("War and Peace", "10001000101aa", "B1")
lib.addBookItem("War and Peace", "10001000102aa", "B2")
lib.addBook(" In Search of Lost Time", "Marcel Proust", "1931")
lib.addBookItem(" In Search of Lost Time", "10001000101ab", "C1")
lib.addBookItem(" In Search of Lost Time", "10001000102ab", "C2")
lib.addBook("The Great Gatsby", "F. Scott Fizgerald", "1925")
lib.addBookItem("The Great Gatsby", "10001000101ac", "D1")
lib.addBookItem("The Great Gatsby", "10001000102ac", "D2")
lib.addBookItem("The Great Gatsby", "10001000103ac", "D2")
lib.viewBooks()
lib.removeBookItem("10001000101ac")
lib.viewBooks()
lib.removeBook(" In Search of Lost Time")
lib.viewBooks()


member1 = Member("Rahul kumar", "Ahmedabad", 23, "ADK4321", "NESS4321")
member2 = Member("Sanjay Patel", "Dehradun", 22, "SK1234", "MSU8765")
member3 = Member("Vinay Kumar", "Roorkee", 24, "NK9876", "JSPM1715")
print(member1)
print(member2)
print(member3)
member1.viewBooks()
member1.search_by_book_name("The Great Gatsby")
member1.search_by_book_name("The magic of thinking big")
member1.search_by_author_name("F. Scott Fizgerald")
member1.search_by_author_name("JK rowling")
member1.issue_book("The Great Gatsby", 8)
member2.issue_book("War and Peace", 10)
member1.viewBooks()

lib.view_issued_books()

member1.return_book("10001000101ac")
member1.viewBooks()

member2.issue_book("War and Peace")

lib.viewMembers()

lib.removeMember("Vinay")
member1.issue_book("War and Peace")
lib.viewMembers()
lib.view_issued_books()