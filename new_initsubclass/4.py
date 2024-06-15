"""New and Init Subclass"""

# pylint: disable=too-few-public-methods, super-init-not-called, invalid-name
class A:
    """Baseclass"""

    def __init_subclass__(cls) -> None:
        print(f"(init subclass) {cls=}")

    def __new__(cls, *args, **kwargs):
        print(f"I am (new) of A, with {cls=}")
        return super().__new__(B, *args, **kwargs)

    def __init__(self) -> None:
        print("I am (init) of A")


class B(A):
    """Implementation class"""

    def __init__(self) -> None:
        print("I am (init) of B")







if __name__ == "__main__":
    pass
