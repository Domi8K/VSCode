from calculator2 import square


def main():
    test_square()


def test_square():
    """
    if square(2) != 4:
        print("2 squared was not 4")
    """
    try:
        assert square(2) == 4
    except AssertionError:
        print("the square of 2 was not properly carried out")
    try:
        assert square(3) == 9
    except AssertionError:
        print("the square of 3 was not properly carried out")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("the square of -2 was not properly carried out")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("the square of -3 was not properly carried out")
    try:
        assert square(0) == 0
    except AssertionError:
        print("the square of 0 was not properly carried out")


if __name__ == "__main__":
    main()
