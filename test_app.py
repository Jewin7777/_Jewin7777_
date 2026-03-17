from app import add, subtract, is_even

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False