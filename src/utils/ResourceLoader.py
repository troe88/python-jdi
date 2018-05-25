__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import json

from entities.User import User


class ResourceLoader:

    def __init__(self) -> None:
        with open('data/users.json') as json_file:
            self._users = json.loads(json_file.read())

    def get_user(self, user_id: str) -> User:
        return User(**self._users[user_id])
