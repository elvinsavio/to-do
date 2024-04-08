# pylint: disable=missing-module-docstring,too-few-public-methods
import tomllib
import sys

class Constants:
    """
        Class containing application constants
    """
    def __init__(self) -> None:
        self._env = self._load_toml_file()
        self.APPLICATION = self._env["application"]
        self.LOGS = self._env["logs"]

    @staticmethod
    def _load_toml_file():
        """
        Loads local env file into memory
        Application exits if not found
        """
        try:
            with open("env.toml", "rb") as f:
                data = tomllib.load(f)
                return data
        except FileNotFoundError:
            sys.exit("Environment file not found")
