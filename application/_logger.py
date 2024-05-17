import logging
import traceback
from pathlib import Path
from typing import Union

from application._constants import Constants

class Logger:
    """
    Create a logging class
    """

    def __init__(self, settings: Constants) -> None:
        self.path: str = settings.LOGS["path"]
        self.has_output: bool = settings.LOGS["output"]
        self.has_stdout: bool = settings.LOGS["stdout"]

        # creates the logs folder
        self._create_log_folder()

        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            format="%(levelname)s:%(module)s:%(message)s",
            filename=settings.LOGS["path"] + "/application_logs.log",
            encoding="utf-8",
            level=logging.DEBUG,
            filemode="a" if settings.LOGS["persist"] else "w",
        )

        if not self.has_output:
            self.logger.info("Logs write false")

        if not self.has_stdout:
            self.logger.info("Logs stdout false")

    def _create_log_folder(self):
        """
        Creates the log output folder
        """
        Path(self.path).mkdir(parents=True, exist_ok=True)

    def info(self, *string: str) -> None:
        """
        Info level logging
        """
        if self.has_output:
            self.logger.info(", ".join(map(str, string)))
        if self.has_stdout:
            print(f"INFO:{', '.join(map(str, string))}")

    def debug(self, *string: str) -> None:
        """
        Debug level logging
        """
        if self.has_output:
            self.logger.debug(", ".join(map(str, string)))
        if self.has_stdout:
            print(f"DEBUG:{', '.join(map(str, string))}")

    def warning(self, *string: str) -> None:
        """
        Warning level logging
        """
        if self.has_output:
            self.logger.warning(", ".join(map(str, string)))
        if self.has_stdout:
            print(f"WARNING:{', '.join(map(str, string))}")

    def error(self, *string: str) -> None:
        """
        Error level logging
        Logs stack strace regardless of has_output or not
        """
        self.logger.error(", ".join(map(str, string)), exc_info=True)
        if self.has_stdout:
            stack_trace = traceback.format_exc()
            error_message = "\n".join([", ".join(map(str, string)), stack_trace])
            print(f"ERROR:{__name__}: {error_message}")
