import logging

logger_api = logging.getLogger("api_log")
logger_api.setLevel("INFO")

# создаем обработчик для файла
file_handler_api = logging.FileHandler("logs/api.log")
# задаем форматирование для логово
formatter_api = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
# применяем форматированию к обработчику
file_handler_api.setFormatter(formatter_api)
# добавляем обработчик к логеру
logger_api.addHandler(file_handler_api)
