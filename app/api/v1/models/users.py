userslist = []

class UsersModels():
    def sign_up_user(self, firstname, lastname, email,password,confirmpassword, registered, isAdmin):
        payload =  {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password":password,
            "confirmpassword":confirmpassword,
            "registered": registered,
            "isAdmin": isAdmin
        }
        create_payload = userslist.append(payload)
        return True
    