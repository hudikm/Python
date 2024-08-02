def calculate(expression):
    try:
        # Remove any whitespace from the expression
        expression = expression.replace(" ", "")
        
        if '+' in expression:
            a, b = map(float, expression.split('+'))
            return a + b
        elif '-' in expression:
            a, b = map(float, expression.split('-'))
            return a - b
        elif '*' in expression:
            a, b = map(float, expression.split('*'))
            return a * b
        elif '/' in expression:
            a, b = map(float, expression.split('/'))
            return a / b
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    expr = input("Enter an arithmetic expression (e.g., 1+1): ")
    result = calculate(expr)
    print(f"Result: {result}")