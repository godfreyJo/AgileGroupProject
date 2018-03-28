class Comment:
    def __init__(self):
        self.comment_id = None
        self.author = None
        self.comment = None
        self.timestamp = None
        self.parent = None


class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.last_logged_in_at = None
        self.comments = []
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        self.last_logged_in_at = datetime.now()

    def logout(self):
        self.is_logged_in = False

    def add_comment(self, comment):
        pass

    def edit_comment(self):
        comm_id = "3"
        old_comm = "Old Comment"
        comm_data = "This is a  new comment"
        for item in self.comments():
            if comm_id == item.comment_id:
                new_comm = {Comment().comment_id: comm_id,
                            Comment().comment: comm_data,
                            Comment().timestamp = datetime.now()}
                self.comments.append(new_comm)
        
    
        



    def delete_comment(self):
        pass


class Moderator(User):
    def __init__(self):
        User.__init__(self)


class Admin(User):
    def __init__(self):
        User.__init__(self)
