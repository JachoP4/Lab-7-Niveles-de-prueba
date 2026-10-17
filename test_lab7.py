import pytest
import book
import user
import library

@pytest.mark.unit
def test_book_borrow():
    librazo1 = book.Book("El Alquimistra", "Paulo Coehlo", 1967, "ISBN0001")
    assert librazo1.title == "El Alquimistra"
    librazo1.borrow()
    assert librazo1.borrowed == True

@pytest.mark.unit
def test_book_borrow_twice():
    librazo1 = book.Book("El Alquimistra", "Paulo Coehlo", 1967, "ISBN0001")
    assert librazo1.title == "El Alquimistra"
    librazo1.borrow()
    assert librazo1.borrowed == True
    with pytest.raises(ValueError, match="The book is already borrowed"):
        librazo1.borrow()

@pytest.mark.unit
def test_book_borrowed_and_returned():
    librazo1 = book.Book("El Alquimistra", "Paulo Coehlo", 1967, "ISBN0001")
    assert librazo1.title == "El Alquimistra"
    librazo1.borrow()
    assert librazo1.borrowed == True
    librazo1.return_book()
    assert librazo1.borrowed == False

@pytest.mark.sys
def test_library_borrow():
    librazo1 = book.Book("El Alquimista", "Paulo Coehlo", 1967, "ISBN0001")
    user1 = user.User("Miguel", "ID0001")
    lib = library.Library()
    lib.add_book(librazo1)
    assert lib.books[0].title == 'El Alquimista'
    lib.add_user(user1)
    # Corroborar que se agrego
    lib.borrow_book('ID0001', 'ISBN0001')
    assert librazo1.borrowed == True

@pytest.fixture
def library_init():
    librazo1 = book.Book("El Alquimista", "Paulo Coehlo", 1967, "ISBN0001")
    user1 = user.User("Miguel", "ID0001")
    lib = library.Library()
    lib.add_book(librazo1)
    lib.add_user(user1)
    return lib

@pytest.mark.wip
def test_library_borrow(library_init):
    lib = library_init
    # Corroborar que se agrego
    lib.borrow_book('ID0001', 'ISBN0001')
    assert lib.books[0].borrowed == True