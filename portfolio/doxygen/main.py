"""
\file main.py
\brief Example Python script with Doxygen comments.
"""

def add_numbers(a, b):
    """
    \brief Adds two numbers.
    \param a The first number.
    \param b The second number.
    \return The sum of the two numbers.
    """
    return a + b

if __name__ == "__main__":
    result = add_numbers(5, 7)
    print(f"Result: {result}")
