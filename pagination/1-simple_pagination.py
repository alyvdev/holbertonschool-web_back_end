#!/usr/bin/env python3
"""Simple Pagination"""

import csv
from typing import List, Tuple

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page with the given page number and page size."""
        # Validate inputs
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

        # Fetch the dataset
        data = self.dataset()

        # Calculate start and end indices
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page or an empty list if out of range
        return data[start_index:end_index] if start_index < len(data) else []

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index."""
    return (page - 1) * page_size, page * page_size
