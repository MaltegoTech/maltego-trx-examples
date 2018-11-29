from maltego_trx.entities import Person
from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import UIM_PARTIAL


class NameFromCSV(DiscoverableTransform):
    """
    Lookup the name associated with a phone number.
    """

    @classmethod
    def create_entities(cls, request, response):
        phone = request.Value
        
        try:
            name = cls.get_name(phone)
            if name:
                response.addEntity(Person, name)
            else:
                response.addUIMessage("The phone number given did not match any numbers in the CSV file")
        except IOError:
            response.addUIMessage("An error occurred reading the CSV file.", messageType=UIM_PARTIAL)
    
    
    @staticmethod
    def get_name(search_phone):
        with open("phone_to_names.csv") as f:
            for ln in f.readlines():
                phone, name = ln.split(",", 1)
                if phone.strip() == search_phone.strip():
                    return name.strip()
                    

                    
if __name__ == "__main__":
    print(NameFromCSV.get_name("1-541-754-3010"))