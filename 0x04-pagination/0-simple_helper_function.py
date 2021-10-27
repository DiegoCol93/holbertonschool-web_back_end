#!/usr/bin/env python3
""" 0. Simple helper function module. """


def index_range(page: int, page_size: int) -> tuple:
    """ Returns a tuple of size 2 containing a start index and end index. """
    if page <= 0:
        return((0, 0))

    if page == 1:
        return((0, page_size))

    start_index = page * page_size - page_size
    end_index = page * page_size

    return((start_index, end_index))
