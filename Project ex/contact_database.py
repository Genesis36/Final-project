class ContactDatabase:
    def __init__(self, settings):
        self.records = []
        self.settings = settings

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, record):
        self.records.remove(record)

    def search_record(self, keyword):
        for record in self.records:
            if keyword.lower() in [record.name.lower(), record.address.lower(), record.phone_number.lower(), record.email_address.lower()]:
                return record
        return None

    def modify_record(self, record, new_name, new_address, new_phone_number, new_email_address):
        record.name = new_name
        record.address = new_address
        record.phone_number = new_phone_number
        record.email_address = new_email_address

    def print_all_records(self):
        for record in self.records:
            print(record)
            print("--------------------")
