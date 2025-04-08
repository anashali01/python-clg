# Write a program that masks all but the last four digits of a credit card number.

def mask_credit_card(card_number):

    # Remove any spaces or dashes from the card number
    card_number = card_number.replace(" ", "").replace("-", "")
    
    # Check if the input is valid
    if not card_number.isdigit():
        return "Invalid input - please enter numbers only"
    if len(card_number) < 4:
        return "Invalid card number length"
        
    # Keep last 4 digits, mask the rest with *
    masked = "*" * (len(card_number) - 4) + card_number[-4:]
    return masked

# Get input from user
card_input = input("Enter your credit card number: ")

# Display masked number
result = mask_credit_card(card_input)
print(f"Masked card number: {result}")
