class User:

    def __init__(self):

        self.username = None

        self.password = None

        self.last_logged_in_at = None

        self.comments = []

        self.is_logged_in = False


currentuser = []
    def login(self, username,password):
             for user in userlist:
            if user.username == username and  user.password == password
               self.is_logged_in = True
               currentuser.append(self)
                return self.login
                
    def logout(self, username,password):  
        if self.is_logged_in = True:     
            self.last_logged_in_at = datetime.now()
            self.is_logged_in = False



    def add_comment(self, comment):

        pass



    def edit_comment(self):

        pass



    def delete_comment(self):

        pass



    try:



class Moderator(User):

    def __init__(self):

        User.__init__(self)





class Admin(User):

    def __init__(self):

        User.__init__(self)