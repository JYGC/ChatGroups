import logging as error_log

from app.core.config import settings


unknown_error_http_code = 404
unknown_error_detail = "Unknown request"


error_log.basicConfig(
    filename=settings.LOG_FILE,
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s"
)


def unknown_error_response(exception_callback: callable, exc: Exception):
    error_log.exception(exc, exc_info=True)
    raise exception_callback(
        status_code=unknown_error_http_code,
        detail=unknown_error_detail
    )
