from loguru import logger

logger.add("log.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
