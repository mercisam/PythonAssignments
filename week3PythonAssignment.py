def calculate_discount(price, discount_percent):
    """Calculate final price after applying the discount.
    Apply the discount only if it is 20% or higher."""
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of an item: "))
discount_percent = float(input("Enter the discount percentage of the item: "))

# Calculate final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Print result with message
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
