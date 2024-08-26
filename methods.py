import hashlib
from cryptography.fernet import Fernet
import faker

class hashTable():

    def __init__(self,):
        return 

    def mask_data(self, data, salt=''):
        """
        Mask the given data using a cryptographic hash function.

        :param data: The sensitive data to be anonymized (string).
        :param salt: An optional salt to add randomness (string).
        """
        return hashlib.sha256((data + salt).encode()).hexdigest()

class cryptography():

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        return 

    def encrypt(self, data):
        return  self.cipher_suite.encrypt(data.encode())

    def decrypt(self, data):
        return self.cipher_suite.decrypt(data).decode()

class anonymization():
    def __init__(self):
        self.fake =  faker.Faker()
        self.masked_data = dict()

    def mask_data(self, data):
        self.masked_data.clear()
        if "name" in data:
            names = []
            for name in data["name"]:
                names.append(self.fake.name())
            self.masked_data["name"] = names
        if "address" in data:
            addresses = []
            for address in data["address"]:
                addresses.append(self.fake.address())
            self.masked_data["addresses"] = addresses
        if "email" in data:
            emails = []
            for email in data["email"]:
                emails.append(self.fake.email())
            self.masked_data["email"] = emails
        if "phone_number" in data:
            phone_numbers = []
            for phone_number in data["phone_number"]:
                phone_numbers.append(self.fake.phone_number())
            self.masked_data["phone_number"] = phone_numbers
        if "dob" in data:
            dobs = []
            for dob in data["dob"]:
                dobs.append(self.fake.date_of_birth())
            self.masked_data["dob"] = dobs
        return self.masked_data




