# import flask_restful_api_app71.py

def test_canAssertTrue():
    assert True
    print (f"\ntest_canAssertTrue:")

def test_next_filter():
    print (f"\ntest_next_filter: => next")
    exceptMode = "try"
    x = ""
    mylist = iter(["apple", "banana", "cherry"])
    try:
        x = next(mylist, None)
        assert x == "apple"
        assert exceptMode == "try"
        x = next(mylist, None)
        assert x == "banana"
        assert exceptMode == "try"
        x = next(mylist, None)
        assert x == "cherry"
        assert exceptMode == "try"
        x = next(mylist, None)
        assert x == None
    except StopIteration:
        # If default is NOT set to none, then last iteration will generate
        # a StopIteration error that needs to be caught with try-except.
        # However, it seems if you specify the default as None it will return None
        # rather than generate an exception error. That is, except is never triggered.
        exceptMode = "except"
        
    assert exceptMode == "try"

    print (f"\ntest_next_filter: => filter {exceptMode}")

    ages = [5, 12, 17, 18, 24, 32]

    assert ages == [5, 12, 17, 18, 24, 32]

    def pickOver18(x):
        if x < 18:
            return False
        else:
            return True

    adults = filter(pickOver18, ages)

    y = next(adults, None)
    assert y == 18
    print (f"\nAdults: {y}")

    for x in adults:
        print(x)
        
    # The following don't work. Can't access the filter object.
    # assert adults[0] == 18
    # assert adults == [18, 24, 32]




