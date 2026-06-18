from loguru import logger

logger.add(
    "logs/execution.log",
    rotation="5 MB",
    level="INFO"
)
