#!/usr/bin/env python3
""" 2. Hypermedia pagination. """
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """ Returns a tuple of size 2 containing a start and end index. """
        if page <= 0:
            return((0, 0))

        if page == 1:
            return((0, page_size))

        start_index = page * page_size - page_size
        end_index = page * page_size
        return((start_index, end_index))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Pagination method to return index of a page and offset.  """
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        self.dataset()
        index = self.index_range(page, page_size)
        if index[0] > len(self.__dataset):
            return []
        results = []
        for row in self.__dataset[index[0]: index[1]]:
            results.append(row)
        return results

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Returns a dictionary containing the data. """
        results = self.get_page(page, page_size)
        index = self.index_range(page, page_size)

        start = index[0]
        end = index[1]
        next = None if (page * page_size) > len(self.__dataset) else page + 1
        prev = None if page * page_size - page_size < 1 else page - 1
        total = len(self.__dataset) // page_size
        data = {
            "page_size": len(results),
            "page": page,
            "data": results,
            "next_page": next,
            "prev_page": prev,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
        return(data)
