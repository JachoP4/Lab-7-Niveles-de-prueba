import pytest
import book 
import user
import library

# Espacio para fixtures
@pytest.fixture # Los fixture son objetos previamente declarados para utilizarlos en las pruebas pertinentes.
def library_init():
    librazo1 = book.Book("El Alquimista", "Paulo Coehlo", 1967, "ISBN0001")
    user1 = user.User("Miguel", "ID0001")
    lib1 = library.Library()
    lib1.add_book(librazo1)
    lib1.add_user(user1)
    return lib1

# Pruebas de unidad
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
    with pytest.raises(ValueError, match="The book has alerady been borrowed"):
        librazo1.borrow()

@pytest.mark.unit
def test_book_borrowed_and_returned():
    librazo1 = book.Book("El Alquimistra", "Paulo Coehlo", 1967, "ISBN0001")
    assert librazo1.title == "El Alquimistra"
    librazo1.borrow()
    assert librazo1.borrowed == True
    librazo1.return_book()
    assert librazo1.borrowed == False

# Hecha por JP
@pytest.mark.unit # En esta función probamos que se le registre un prestamo y un retorno y que se refleje en el historial,
def test_user_history():
    librazo1 = book.Book("El Alquimista", "Paulo Coehlo", 1967, "ISBN0001")
    user1 = user.User("Miguel", "ID0001")
    user1.register_borrow(librazo1)
    user1.register_return(librazo1)
    user1.get_history()
    assert user1.get_history() == ['Borrwed: El Alquimista', 'Reurned: El Alquimista']

# Pruebas de integracion

@pytest.mark.sys # Es de sistema ya que abarca mas modulos, deberia repetirla con utilizando directamente la clase library ya que improta las otras clases.
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

@pytest.mark.sys # Aqui aplicamos el fixture
def test_library_borrow_fixturized(library_init):
    lib = library_init
    # Corroborar que se agrego
    lib.borrow_book('ID0001', 'ISBN0001')
    assert lib.books[0].borrowed == True

# Pruebas de levantamiento de erroes
@pytest.mark.sys
def test_library_find_book_ValueError(library_init): # Aplicamos fixture
    lib = library_init
    with pytest.raises(ValueError):
        lib._find_book(67)
        
@pytest.mark.sys
def test_library_find_user_ValueError(library_init): # Aplicamos fixture
    lib = library_init
    with pytest.raises(ValueError):
        lib._find_user(67) #sixseven

# Pruebas de verificacion de mensajes de error
@pytest.mark.sys
def test_library_find_user_ValueError_message(library_init, capsys):
    lib = library_init
    with pytest.raises(ValueError):
        lib._find_book(67)
        captured = capsys._captured_err()
        assert captured.out == "USer not found"

@pytest.mark.sys
def test_library_find_book_ValueError_message(library_init, capsys):
    lib = library_init
    with pytest.raises(ValueError):
        lib._find_book(67)
        captured = capsys._captured_err()
        assert captured.err == "Book not found"