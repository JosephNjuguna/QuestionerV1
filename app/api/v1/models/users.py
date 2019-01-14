userslist = []
import datetime
import uuid

class UsersModels():
    def sign_up_user(self, firstname, lastname, email, password, confirmpassword):
        payload =  {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password":password,
            "confirmpassword":confirmpassword,
            "registered": datetime.datetime.utcnow(),
            "public_id": str(uuid.uuid4()),
            "id":len(userslist)+1
        }
        create_payload = userslist.append(payload)
        return userslist
    