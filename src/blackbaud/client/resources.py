class BlackbaudResource(object):
    ...

class BlackbaudObject(BlackbaudResource):
    """
    Base class for any Blackbaud object, such as a constituent, a grade level, etc.
    """
    ...

class BlackbaudPage(BlackbaudResource):
    """
    A page of results from any Blackbaud API endpoint.
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
    Will have a .results attribute which will be a generator that yields BlackbaudListItems.
    """
    ...