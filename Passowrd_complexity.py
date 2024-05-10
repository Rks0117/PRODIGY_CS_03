def password_complexity_checker(password):
    score = 0
    
    # Check password length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    
    # Check for numbers
    if any(char.isdigit() for char in password):
        score += 1
    
    # Check for special characters
    if any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~`" for char in password):
        score += 1
    
    # Provide feedback based on the score
    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Medium password"
    else:
        return "Weak password"

# Take user input
user_password = input("Enter your password: ")

# Call the function and display the result
result = password_complexity_checker(user_password)
print("Password strength:", result)