# portfolio/bug_tracking/main.py

def add_numbers(a, b):
    return a - b  # Bug: should be addition, not subtraction

def main():
    result = add_numbers(5, 3)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
