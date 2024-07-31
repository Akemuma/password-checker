import string
import math

# Function to calculate the entropy (a measure of unpredictability) of the password
def calculate_entropy(password):
    # Initialize pool_size to 0; this will store the total number of possible characters in the password
    pool_size = 0
    
    # Check if the password contains any lowercase letters and add 26 to the pool size if true
    if any(c.islower() for c in password):
        pool_size += 26
    
    # Check if the password contains any uppercase letters and add 26 to the pool size if true
    if any(c.isupper() for c in password):
        pool_size += 26
    
    # Check if the password contains any digits and add 10 to the pool size if true
    if any(c.isdigit() for c in password):
        pool_size += 10
    
    # Check if the password contains any special characters and add the length of the punctuation set to the pool size
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    # Calculate entropy as length of the password multiplied by log2(pool_size); return 0 if pool_size is 0
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

# Function to evaluate the strength of a given password based on multiple criteria
def check_password_strength(password):
    # Check if the password meets the length criteria (at least 8 characters)
    length_criteria = len(password) >= 8
    
    # Check if the password contains at least one uppercase letter
    upper_criteria = any(c.isupper() for c in password)
    
    # Check if the password contains at least one lowercase letter
    lower_criteria = any(c.islower() for c in password)
    
    # Check if the password contains at least one digit
    digit_criteria = any(c.isdigit() for c in password)
    
    # Check if the password contains at least one special character
    special_criteria = any(c in string.punctuation for c in password)

    # Count how many of the above criteria are met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    # Calculate the entropy of the password
    entropy = calculate_entropy(password)
    
    # Determine the strength of the password based on criteria met and entropy value
    if criteria_met == 5 and entropy >= 60:
        strength = "Very Strong"
    elif criteria_met >= 4 and entropy >= 50:
        strength = "Strong"
    elif criteria_met >= 3 and entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Return the strength and the individual criteria checks for further feedback
    return strength, length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria, entropy

# Function to provide feedback to the user based on the password strength evaluation
def provide_feedback(password):
    # Call the check_password_strength function to get the evaluation results
    strength, length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria, entropy = check_password_strength(password)
    
    # Start building the feedback string with the determined password strength
    feedback = f"Password Strength: {strength}\n"
    
    # Add suggestions for improvement based on which criteria were not met
    if not length_criteria:
        feedback += " - Increase the length to at least 8 characters.\n"
    if not upper_criteria:
        feedback += " - Include at least one uppercase letter.\n"
    if not lower_criteria:
        feedback += " - Include at least one lowercase letter.\n"
    if not digit_criteria:
        feedback += " - Include at least one digit.\n"
    if not special_criteria:
        feedback += " - Include at least one special character.\n"
    
    # Add the entropy value to the feedback for informational purposes
    feedback += f"Entropy: {entropy:.2f} bits\n"
    
    # Return the full feedback string
    return feedback

# Example usage
password = "P@ssw0rd!"
# Print the feedback based on the provided password
print(provide_feedback(password))
