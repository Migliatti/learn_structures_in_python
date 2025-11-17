def calculate_tip(total, tip_percentage):
    return total * (tip_percentage / 100)

try:
    total = float(input("Enter the total amount: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    result = calculate_tip(total, tip_percentage)
    print(f"The tip is U$ {result:.2f}")
    print(f"The total is U$ {total:.2f}")
    print(f"The total with tip is U$ {total + result:.2f}")
except ValueError:
    print("Error: The values must be numbers.")
except Exception as e:
    print(f"Unexpected error: {e}")