def greet(name):
    """
    This function greets the user with a personalized message.

    :param name: The name of the user.
    :type name: str
    """
    message = f"Hello, {name}! Welcome to our program."
    print(message)


def calculate_sum(a, b):
    """
    This function calculates the sum of two numbers.

    :param a: The first number.
    :type a: int or float
    :param b: The second number.
    :type b: int or float
    :return: The sum of the two numbers.
    :rtype: int or float
    """
    result = a + b
    return result


def main():
    """
    The main function of the program.
    """
    greet("Alice")
    num1 = 10
    num2 = 20
    total = calculate_sum(num1, num2)
    print(f"The sum of {num1} and {num2} is: {total}")


if __name__ == "__main__":
    main()

