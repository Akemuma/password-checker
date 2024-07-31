import string
import math

def calculate_entropy(password):
     pool_size = 0
         if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

 def check_password_strength(password):  
     length_criteria = len(password) >= 8
     upper_criteria = any(c.isupper() for c in password) 
     lower_criteria = any(c.islower() for c in password)
     digit_criteria = any(c.isdigit() for c in password)
     special_criteria = any(c in string.punctuation for c in password)

     criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

      entropy = calculate_entropy(password)

      if criteria_met == 5 and entropy >= 60:
        strength = "Very Strong"
      elif criteria_met >= 4 and entropy >= 50:
        strength = "Strong"
      elif criteria_met >= 3 and entropy >= 40:
        strength = "Moderate"
      else:
        strength = "Weak"

        return strength, length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria, entropy

def provide_feedback(password):
    strength, length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria, entropy = check_password_strength(password)
    
    feedback = f"Password Strength: {strength}\n"
    if not length_criteria:
        feedback += " - Increase the length to at least 8 characters.\n"
    if not upper_criteria:
        feedback += " - Include at least one uppercase letter.\n"
    if not lower_criteria:
        feedback += " - Include at least one lowercase letter.\n"
    if not digit_criteria:
        feedback += " - Include at least one digit.\n"
    if not special_criteria:


