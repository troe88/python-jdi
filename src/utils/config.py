__author__ = "Dmitry_Lebedev1"
__date__ = "25-May-18"

import json


class Config:
    def __init__(self) -> None:
        with open('config.json') as json_file:
            self._conf = json.loads(json_file.read())

    def conf(self):
        return self._conf
