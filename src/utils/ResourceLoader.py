import json

from entities.User import User


class ResourceLoader:

    def __init__(self) -> None:
        with open('../utils/users.json') as json_file:
            self._users = json.loads(json_file.read())
        with open('../utils/config.json') as json_file:
            self._conf = json.loads(json_file.read())

    def get_user(self, user_id: str):
        return User(**self._users[user_id])

    def conf(self, config_option_name: str):
        return self._conf[config_option_name]
