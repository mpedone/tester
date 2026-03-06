def main():
    print("Hello from tester!")
    x = input("What is your name? ")
    print(greet(x))

def greet(n):
    if type(n) != "str":
        str(n)
    return f"Hello, {n.capitalize()}. It is nice to see you."

if __name__ == "__main__":
    main()
