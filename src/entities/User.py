class User:
    _name: str
    _password: str
    _login: str

    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._password = kwargs['password']
        self._login = kwargs['login']

    def login(self):
        return self._login

    def password(self):
        return self._password

    def name(self):
        return self._name

    def __repr__(self):
        return f"{self.name()}"
