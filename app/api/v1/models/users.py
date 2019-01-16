users_list = []
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
            "id":len(users_list)+1
        }
        create_payload = users_list.append(payload)
        return users_list
    