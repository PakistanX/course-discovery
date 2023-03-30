import logging
from django.contrib.sites.middleware import CurrentSiteMiddleware
from django.urls import reverse

logger = logging.getLogger(__name__)


class SkipSiteMiddleware(CurrentSiteMiddleware):
    """Remove SiteMiddleware if request is for /health."""

    def process_request(self, request):
        if request.path not in reverse('health'):
            logger.info('\n\n\nrequest path: {}\n\n\n'.format(request.path))
            return super().process_request(request)
