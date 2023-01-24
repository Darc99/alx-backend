#!/usr/bin/env python3
"""
 index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing a start index 
    and an end index corresponding to the range of indexes to return in a list f
    or those particular pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.
    Args:
        page (int): page number to return 
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
