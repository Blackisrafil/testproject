class Contact:

    def __init__(self, name, number, address, email):
        self.name = name
        self.number = number
        self.address = address
        self.email = email

contacts = []

contacts.append(Contact("Jim", 1, "123, Fictional Road", "JimHal@fictional.com"))
contacts.append(Contact("Nazeem", 2, "95, Whiterun, Cloud District", "Constantannoyance@noonecares.com"))
contacts.append(Contact("Balwin", 3, "55, Meerwoods Roads", "Nowhere@amail.com"))

for contact in contacts:
    print(vars(contact))