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
            try:
                stream.write(msg)
            except UnicodeError:
                stream.write('Message for Urdu course.')
            stream.write(self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)
