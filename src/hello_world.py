"""Sample program for GitHub issue #1."""


def main() -> None:
    print("Hello World")
    a = 5
    b = 0

    if b == 0:
        result = "undefined (division by zero)"
    else:
        result = a / b

    print(f"a = {a}, b={b}, results = {result}")
    print("Goodbye World")


if __name__ == "__main__":
    main()
