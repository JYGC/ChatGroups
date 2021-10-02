import logging as error_log

from app.core.config import settings


error_log.basicConfig(
    filename=settings.LOG_FILE,
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s"
)
