import json
import re
import threading

# a more lenient number regex (modified from json.scanner.NUMBER_RE)
NUMBER_RE = re.compile(
    r'(-?(?:\d*))(\.\d+)?([eE][-+]?\d+)?',
    (re.VERBOSE | re.MULTILINE | re.DOTALL))


# we are going to be messing with the internals of `json.scanner`. As such we
# want to return it to its initial state when we're done with it, but we need to
# do so in a thread safe way.
_LOCK = threading.Lock()
def thread_safe_py_make_scanner(context, *, number_re=json.scanner.NUMBER_RE):
    with _LOCK:
        original_number_re = json.scanner.NUMBER_RE
        try:
            json.scanner.NUMBER_RE = number_re
            return json.scanner._original_py_make_scanner(context)
        finally:
            json.scanner.NUMBER_RE = original_number_re

json.scanner._original_py_make_scanner = json.scanner.py_make_scanner
json.scanner.py_make_scanner = thread_safe_py_make_scanner


class MyJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # overwrite the stricter scan_once implementation
        self.scan_once = json.scanner.py_make_scanner(self, number_re=NUMBER_RE)