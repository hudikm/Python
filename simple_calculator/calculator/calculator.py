def calculate(expression):
    try:

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    expr = input("Enter an arithmetic expression (e.g., 1+1): ")
    result = calculate(expr)
    print(f"Result: {result}")