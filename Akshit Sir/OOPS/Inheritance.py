class Phone:
    def __init__(self, phone_name: str, phone_company: str):
        self.phone_name = phone_name

        self.phone_company = phone_company

    def display_all_details(self):
        print(
            f"{self.phone_name},{self.phone_company}".split(','))


phone_one = Phone('Pixel', 'Google')
phone_one.display_all_details()
