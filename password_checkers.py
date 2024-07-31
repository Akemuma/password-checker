import re
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
