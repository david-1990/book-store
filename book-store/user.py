class User:
    def __init__(self):
        self.user_type='guest'

    def register(self, name, pwd, emailID):
        self.uname=name
        self.pwd=pwd
        self.emailID=emailID

    def __repr__(self):
        str = 'Name: {0}, Email: {1}, Type: {2}\n'
        str = str.format(self.uname, self.emailID, self.user_type)
        return str