class Logger:
    def log(self, message):
        with open("game_log.txt", "a", encoding="utf-8") as file:
            file.write(message + '\n')

logger = Logger()