import fizzBuzz

def test_canAssertTrue():
    assert True

def test_callfizzBuzz():
    fizzBuzz.fizzBuzz(1)

def test_callWith1():
    assert fizzBuzz.fizzBuzz(1) == "1"

def test_callWith2():
    assert fizzBuzz.fizzBuzz(2) == "2"
    
def test_callWith3():
    assert fizzBuzz.fizzBuzz(3) == "Fizz"

def test_callWith4():
    assert fizzBuzz.fizzBuzz(4) == "4"

def test_callWith5():
    assert fizzBuzz.fizzBuzz(5) == "Buzz"
    
def test_callWith6():
    assert fizzBuzz.fizzBuzz(6) == "Fizz"

def test_callWith15():
    assert fizzBuzz.fizzBuzz(15) == "Fizz Buzz"

def test_callWith7():
    assert fizzBuzz.fizzBuzz(7) == "7"

def test_callWith7():
    assert fizzBuzz.fizzBuzz(9) == "Fizz"

def test_callWith7():
    assert fizzBuzz.fizzBuzz(99) == "Fizz"

def test_callWith10():
    assert fizzBuzz.fizzBuzz(10) == "Buzz"

def test_callWith10():
    assert fizzBuzz.fizzBuzz(100) == "Buzz"
