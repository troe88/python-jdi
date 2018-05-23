import json


class Config:
    def __init__(self) -> None:
        with open('src/utils/config.json') as json_file:
            self._conf = json.loads(json_file.read())

    def conf(self):
        return self._conf
