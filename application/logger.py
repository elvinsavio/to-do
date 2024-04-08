import logging
import traceback


class Logger:
    """
    Create a logging class
    """

    def __init__(self, settings: dict[str]) -> None:
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            format="%(levelname)s:%(message)s",
            filename=settings["path"] + "/application_logs.log",
            encoding="utf-8",
            level=logging.DEBUG,
            filemode="a" if settings["persist"] else "w",
        )
        self.has_output = settings["output"]
        self.has_stdout = settings["stdout"]

        if not self.has_output:
            self.logger.info("Logs write false")

        if not self.has_stdout:
            self.logger.info("Logs stdout false")

    def info(self, *string: str) -> None:
        """
        Info level logging
        """
        if self.has_output:
            self.logger.info(", ".join(map(str, string)))
        if self.has_stdout:
            print("INFO:" + ", ".join(map(str, string)))

    def debug(self, *string: str) -> None:
        """
        Debug level logging
        """
        if self.has_output:
            self.logger.debug(", ".join(map(str, string)))
        if self.has_stdout:
            print("DEBUG:" + ", ".join(map(str, string)))

    def warning(self, *string: str) -> None:
        """
        Warning level logging
        """
        if self.has_output:
            self.logger.warning(", ".join(map(str, string)))
        if self.has_stdout:
            print("WARNING:" + ", ".join(map(str, string)))

    def error(self, *string: str) -> None:
        """
        Error level logging
        """
        if self.has_output:
            self.logger.error(", ".join(map(str, string)), exc_info=True)
        if self.has_stdout:
              # Get the stack trace as a string
            stack_trace = traceback.format_exc()
            # Combine error message(s) with stack trace
            error_message = "\n".join([", ".join(map(str, string)), stack_trace])
            print(f"ERROR: {error_message}")
