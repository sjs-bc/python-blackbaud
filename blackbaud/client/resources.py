from typing import Iterator


class BlackbaudResource(object):
    ...


class BlackbaudObject(BlackbaudResource):
    """
    Base class for any Blackbaud object, such as a constituent, a grade level, etc.

    BlackbaudCollection > BlackbaudPage > BlackbaudObject
    """

    ...


class BlackbaudPage(BlackbaudResource):
    """
    A page of results from any Blackbaud API endpoint.

    BlackbaudCollection > BlackbaudPage > BlackbaudObject
    """
    def __init__(self, url, text) -> None:
        ...

    def __iter__(self) -> Iterator[BlackbaudObject]:
        ...

    def __next__(self) -> BlackbaudObject:
        ...
    
    def __getitem__(self, index) -> BlackbaudObject:
        ...


class BlackbaudCollection(BlackbaudResource):
    """
    A collection of Blackbaud objects, split into pages.

    BlackbaudCollection > BlackbaudPage > BlackbaudObject
    """

    ...


class BlackbaudList(BlackbaudResource):
    """
    A basic or advanced list in Blackbaud.
    {
      "id": 2,
      "name": "List Two",
      "type": "Advanced",
      "description": "This list is more advanced",
      "category": "Admissions",
      "created_by": "John Smith",
      "created": "2021-08-08T00:00:00Z",
      "last_modified": "2021-08-08T00:00:00Z"
    }
    If any part of the list is ever fetched, its columns attribute will be populated.
    Will have a .columns attribute which will list the columns.
    Will have a .results attribute which will be a generator that yields
    BlackbaudListItems.
    """

    ...
