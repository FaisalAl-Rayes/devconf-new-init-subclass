"""New and Init Subclass"""

# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class A:
    """Baseclass"""

    def __init_subclass__(cls, test_arg) -> None:
        print(f"(init subclass) {cls=}, with {test_arg=}")

    def __new__(cls, *args, **kwargs):
        print(f"I am (new) of A, with {cls=}")
        return super().__new__(C, *args, **kwargs)

    def __init__(self) -> None:
        print("I am (init) of A")


class B(A, test_arg="devconf"):
    """Implementation class"""

    def __init__(self) -> None:
        print("I am (init) of B")


class C(A, test_arg="coffee_house"):
    """Implementation class"""

    def __init__(self) -> None:
        print("I am (init) of C")





if __name__ == "__main__":

    var = A()
    print("------------------------------------")
    print(f"Type of instance (var): {type(var)}")
