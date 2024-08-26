from methods import cryptography

method = cryptography()
sensitive_data = "John Doe"
encrypted_output = method.encrypt(sensitive_data)
decrypted_output = method.decrypt(encrypted_output)

print(f"Original Data: {sensitive_data}")
print(f"Encrypted Data: {encrypted_output}")
print(f"Decrypted Data: {decrypted_output}")
