"""New and Init Subclass"""

# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class A:
    """Baseclass"""

    def __new__(cls, *args, **kwargs):
        print(f"I am (new) of A, with {cls=}")
        return super().__new__(cls, *args, **kwargs)

    def __init__(self) -> None:
        print("I am (init) of A")









if __name__ == "__main__":

    var = A()
    print("------------------------------------")
    print(f"Type of instance (var): {type(var)}")
