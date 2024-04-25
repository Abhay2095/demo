import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="E:\\nopcommerce\\Logs\\auto.log",
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p",
                            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
























