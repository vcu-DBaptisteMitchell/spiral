def spiralize(number):
    # Set n
    n = (number - 1) // 2
    # Return function
    return (16 * n ** 3 + 30 * n ** 2 + 26 * n + 3) // 3
