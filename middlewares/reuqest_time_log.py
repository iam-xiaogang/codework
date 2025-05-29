# author xiaogang
import time
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)


class RequestTimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - getattr(request, '_start_time', time.time())
        logger.info(f"{request.method} {request.path} took {duration:.2f}s")
        return response
