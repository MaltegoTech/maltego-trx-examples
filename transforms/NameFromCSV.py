from maltego_trx.entities import Person
from maltego_trx.maltego import UIM_PARTIAL
from maltego_trx.transform import DiscoverableTransform


class NameFromCSV(DiscoverableTransform):
    """
    Lookup the name associated with a phone number.
    """

    @classmethod
    def create_entities(cls, request, response):
        phone = request.Value

        try:
            names = cls.get_names(phone)
            if names:
                for name in names:
                    response.addEntity(Person, name)
            else:
                response.addUIMessage("The phone number given did not match any numbers in the CSV file")
        except IOError:
            response.addUIMessage("An error occurred reading the CSV file.", messageType=UIM_PARTIAL)

    @staticmethod
    def get_names(search_phone):
        matching_names = []
        with open("phone_to_names.csv") as f:
            for ln in f.readlines():
                phone, name = ln.split(",", 1)
                if phone.strip() == search_phone.strip():
                    matching_names.append(name.strip())
        return matching_names


if __name__ == "__main__":
    print(NameFromCSV.get_names("1-541-754-3010"))
