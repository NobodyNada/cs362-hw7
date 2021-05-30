from fizzbuzz import fizzbuzz

def test_numbers():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"
    assert fizzbuzz(4) == "4"
    assert fizzbuzz(101) == "101"

def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(99) == "Fizz"
