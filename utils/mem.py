from pymem import *

def pattern_scan_all(handle, pattern, *, return_multiple=False):
    next_region = 0

    found = []
    user_space_limit = 0x7FFFFFFF0000 if sys.maxsize > 2**32 else 0x7fff0000
    while next_region < user_space_limit:
        next_region, page_found = pymem.pattern.scan_pattern_page(
            handle,
            next_region,
            pattern,
            return_multiple=return_multiple
        )

        if not return_multiple and page_found:
            return page_found

        if page_found:
            found += page_found

    if not return_multiple:
        return None

    return found