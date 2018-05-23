import json

from entities.User import User


class ResourceLoader:

    def __init__(self) -> None:
        with open('src/utils/users.json') as json_file:
            self._users = json.loads(json_file.read())

    def get_user(self, user_id: str):
        return User(**self._users[user_id])
