from django.utils.deprecation import MiddlewareMixin
from datetime import datetime


class LastActivityMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.user.last_activity = datetime.now()
            request.user.save()
        return None