import logging

class Logger:
    __instance = None

    @staticmethod
    def __create_instace():
        # create logger with 'spam_application'
        Logger.__instance = logging.getLogger('etimesheet')
        Logger.__instance.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler('timesheet.log')
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        Logger.__instance.addHandler(fh)
        Logger.__instance.addHandler(ch)

    @staticmethod
    def get_instance():
        if Logger.__instance == None:
            Logger.__create_instace()
        
        return Logger.__instance
