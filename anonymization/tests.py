from methods import anonymization

method = anonymization()
sensitive_record = {
    'name': ['John Doe'],
    'address': ['123 Main St'],
    'email': ['johndoe@example.com'],
    'phone_number': ['555-1234'],
    'dob': ['1990-01-01']
}
new_data = method.mask_data(sensitive_record)
print(f"Original Record: {sensitive_record}")
print(f"Anonymized Record: {new_data}")

