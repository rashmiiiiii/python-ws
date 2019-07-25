from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list = []   #class variable
    @classmethod
    def addContact(cls):
        name = input("enter theh name:")
        email = input("enter theh email:")
        mobile = input("enter theh mobile:")
        address = input("enter theh address:")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print(f"contact is added successfully with name :{name}")

    @classmethod
    def deleteContact(cls):
        name = input("enter the name ")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"contact with {name} is successfully deleted")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"contact with {name} is not found")
    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)
    @classmethod
    def search(cls):
        if len(cls.contact_list) > 0:
            name = input("enter the name:")
            s_list = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))
            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print("contact list is empty you cant search")
    @classmethod
    def updateContact(cls):
        name = input("enter the name :")
        contact=cls.get_contact_by_name(name)
        if contact:
            print("1.Name 2.Email 3.Mobile 4.Address")
            ch = int(input("enter the choice:"))
            if ch == 1:
                print(f"old name :{contact.get__name()}")
                name = input("enter the new name:")
                if name:
                    contact.set__name(name)
            elif ch == 2:
                print(f"old Email :{contact.get__email()}")
                email = input("enter the new email:")
                if email:
                    contact.set__email(email)
            elif ch == 3:
                print(f"old Mobile :{contact.get__mobile()}")
                mobile = input("enter the new mobile no:")
                if mobile:
                    contact.set__mobile(mobile)
            elif ch == 4:
                print(f"old address :{contact.get__address()}")
                address = input("enter the new address:")
                if address:
                    contact.set__address(address)
        else:
            print(f"contact with name:{name} does not exist")

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ["Name","Email","Mobile","Address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"contact book is empty")
    
    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contact_list) > 0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_list))
            return contact[0] if contact else None
