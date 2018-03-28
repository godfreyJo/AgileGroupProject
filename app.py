import cmd
import docopt
from datetime import datetime

user_list = []
current_user = []


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
        current_user.append(self)
        return self.login

    def logout(self):
        if self.is_logged_in:
            self.last_logged_in_at = datetime.now()
            self.is_logged_in = False

    def add_comment(self, comment):
        pass

    def delete_comment(self):
        pass


class Moderator(User):
    def __init__(self):
        User.__init__(self)


class Admin(User):
    def __init__(self):
        User.__init__(self)


def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt.docopt(fn.__doc__, arg)
        except docopt.DocoptExit as e:
            print(e)
            return
        except SystemExit:
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Commands(cmd.Cmd):
    prompt = 'comment>>'

    @docopt_cmd
    def do_comment(self, arg):
        """Usage: echo <comment>..."""

        comment = ' '.join(arg['<comment>'])
        # save comment
        print(comment)


    @docopt_cmd
    def do_reply(self, arg):
        """Usage: reply <commment_id> <comment>..."""

        pass

    @docopt_cmd
    def do_edit(self, arg):
        """Usage: edit <comment_id> <comment>..."""

        pass

    @docopt_cmd
    def do_delete(self, arg):
        """Usage: delete <comment_id> <comment>..."""

        pass

    @docopt_cmd
    def do_login(self, arg):
        """Usage: login <username> <password>"""

        login = None
        for user in user_list:
            if user.username == arg['<username>'] and user.password == arg['<password>']:
                login = user.login()
                break

        if login:
            print('success')
        else:
            print('wrong username or password')



    @docopt_cmd
    def do_logout(self, arg):
        """Usage: logout"""

        pass


user1 = User()
user1.username = 'user'
user1.password = 'password'
user_list.append(user1)


def main():
    try:
        Commands().cmdloop()
    except KeyboardInterrupt:
        print('exiting')

if __name__ == '__main__':
    main()