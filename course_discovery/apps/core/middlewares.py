from django.contrib.sites.middleware import CurrentSiteMiddleware
from django.urls import reverse


class SkipSiteMiddleware(CurrentSiteMiddleware):
    """Remove SiteMiddleware if request is for /health."""

    def process_request(self, request):
        if request.path not in reverse('health'):
            return super().process_request(request)
