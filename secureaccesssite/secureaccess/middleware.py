from django.utils.functional import SimpleLazyObject

from secureaccess.models import UserProfile


class UserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user_agent = SimpleLazyObject(
                lambda: UserProfile.get_last_user_agent_and_update_if_changed_cached(request)
            )
        return self.get_response(request)
