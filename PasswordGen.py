# We're creating a random password generator

import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_letters + string.digits
    result_str = '' .join(random.choice(letters) for i in range(length))
    print ("Random Password Length", length, "is", result_str)
    
    
    
get_random_string(8) 
get_random_string(6)
