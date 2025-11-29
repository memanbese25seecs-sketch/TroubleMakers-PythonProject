import re

def parse_expression(text):
    text = text.lower().strip()

    # Replacing word operators with symbols
    replacements = {
        "plus": "+", "add": "+",
        "minus": "-", "subtract": "-",
        "times": "*", "multiply": "*", "x": "*",
        "divide": "/", "divided by": "/"
    }

    for word, symbol in replacements.items():
        text = text.replace(word, symbol)

    # Regular expression to extract "num operator num"
    pattern = r"(-?\d+\.?\d*)\s*([\+\-\*/])\s*(-?\d+\.?\d*)"
    match = re.search(pattern, text)

    if not match:
        return None, None, None

    num1 = float(match.group(1))
    op = match.group(2)
    num2 = float(match.group(3))

    return num1, op, num2


def smart_calculator():
    print("🔢 Smart Calculator Started (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter expression: ")

        if user_input.lower() in ["exit", "quit", "close"]:
            print("✔ Calculator Closed")
            break

        num1, op, num2 = parse_expression(user_input)

        if op is None:
            print("❌ Error: Could not understand. Try: 5+2, 12 divided by 4, 7 times 8.\n")
            continue

        # Perform calculation
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("❌ Error: Cannot divide by zero!\n")
                continue
            result = num1 / num2

        print(f"= {result}\n")


# Run program
if __name__ == "__main__":
    smart_calculator()
