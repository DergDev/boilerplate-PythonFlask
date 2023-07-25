import app


class LoggingUtility:

    @staticmethod
    def critical(message: str):
        app.app.logger.critical(message)

    @staticmethod
    def error(message: str):
        app.app.logger.error(message)

    @staticmethod
    def warn(message: str):
        app.app.logger.warning(message)

    @staticmethod
    def info(message: str):
        app.app.logger.info(message)

    @staticmethod
    def debug(message: str):
        app.app.logger.debug(message)
