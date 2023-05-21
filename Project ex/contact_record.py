class ContactRecord:
    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}\nEmail Address: {self.email_address}"
