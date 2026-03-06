def main():
    print("Hello from tester!")
    x = input("What is your name? ")
    print(greet(x))

def greet(n):
    if type(n) != "str":
        str(n)
    print(f"Hello, {n.capitalize()}. It is nice to see you.")
    for i in range(20):
        print(f"This has run {i+1} times, {n.capitalize()}.")
    return "...And we're done."

if __name__ == "__main__":
    main()
