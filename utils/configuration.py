import json


class Config:
    def __init__(self, file_path: str = "config.json"):
        with open(file_path, "r") as f:
            data = json.load(f)

        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<Config {self.__dict__}>"


