#from methdos import Pseudonymize
#from . import methods
from methods import hashTable

method = hashTable()
# Example usage
sensitive_data = "John Doe"
salt = "random_salt"  # You can use a different salt for each dataset
output = method.mask_data(sensitive_data, salt)
print(f"Original Data: {sensitive_data}")
print(f"Pseudonymized Data: {output}")
