"""Custom handlers for logging."""

from logging import StreamHandler


class UTF8StreamHandler(StreamHandler):
    """Handles utf-8 encoded data."""

    def __init__(self, stream):
        """Initialize attributes."""
        StreamHandler.__init__(self, stream)

    def emit(self, record):
        """Print in utf-8 encoding."""
        try:
            msg = self.format(record)
            stream = self.stream
            stream.write(str(bytes(msg + self.terminator, 'utf-8')))
            self.flush()
        except Exception:
            self.handleError(record)
