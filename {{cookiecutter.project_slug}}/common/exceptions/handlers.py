import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)
def custom_exception_handler(exc, context):
    # Call the default DRF exception handler first
    response = exception_handler(exc, context)
    # Log the exception with context
    logger.error(
        f"Exception: {exc.__class__.__name__} - {str(exc)}",
        extra={"request": context["request"], "view": context["view"]}
    )
    if response is not None:
        # Add more structured data to the response
        response.data = {
            "status_code": response.status_code,
            "error": response.data.get("detail", "An error occurred"),
            "exception": exc.__class__.__name__,
            "view": context["view"].__class__.__name__,
            "method": context["request"].method,
            "path": context["request"].path,
        }
    return response
