def main():
    print("Hello from tester!")
    username = input("What is your name? ")
    greet(username)

def greet(n):
    print(f"Hello, {n.capitalize()}. It is nice to see you.")
    c = input("How many times should I run? ")
    print(run_count(c, n.capitalize()))

def run_count(x, name):
    if not x.isnumeric():
        return error(name)
    for i in range(int(x)):
        print(f"This has run {i+1} times, {name}.")
    return "...And we're done."

def error(name):
    print(f"I'm sorry, {name}. I can't do that.")

if __name__ == "__main__":
    main()
