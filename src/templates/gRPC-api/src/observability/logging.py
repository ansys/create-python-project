from datetime import datetime
import logging
import os


class Logging:

    def __init__(self) -> None:
        log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(threadName)-10s %(message)s")
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)

        filename = '{0}.log'.format(datetime.today().strftime('%Y_%m_%d@%H_%M_%S'))
        filepath = f'/var/log/{filename}' if os.name != 'nt' else os.path.join(os.getenv("LOCALAPPDATA"), filename)
        filehandler = logging.FileHandler(filepath)
        filehandler.setLevel(logging.DEBUG)
        filehandler.setFormatter(log_formatter)
        self._logger.addHandler(filehandler)

        consolehandler = logging.StreamHandler()
        consolehandler.setLevel(logging.INFO)
        consolehandler.setFormatter(log_formatter)
        self._logger.addHandler(consolehandler)

    @property
    def logger(self):
        return self._logger
