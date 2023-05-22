# python-blackbaud

An unofficial Python wrapper for Blackbaud's SKY API.

## Installation

```shell
pip install blackbaud
```

## Usage

### Endpoints

```python
import os
from blackbaud.client import BaseSolutionClient, SKYAPIClient
from blackbaud.school.endpoints import core, users

# Get your credentials from somewhere
BB_API_SUBSCRIPTION_KEY = os.environ.get("BB_API_SUBSCRIPTION_KEY")
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

# Set up a client
client = SKYAPIClient(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    subscription_key=BB_API_SUBSCRIPTION_KEY, 
    redirect_uri=REDIRECT_URI
)

school = BaseSolutionClient(client, "school", "v1")

# Get a token
client.fetch_token(
    code=input(
        "Please visit the following URL: {}\n\nPaste the token here: ".format(
            client.authorization_url
        )
    )
)

# Get going
authorized_user = users.get_self(school)
```

Endpoints are implemented as functions that take a client object (and any required parameter) as an argument, and return a `requests.Response`. So far, only [education management endpoints](https://developer.sky.blackbaud.com/docs/services/school) have been implemented.

They standardize certain parameter names to alleviate inconsistencies and avoid confusion (eg. school level identifiers being called `level_id` in some endpoints and `level_num` in others).

They also standardize formatting where possible, such as for dates and times:

```python
from datetime import datetime, timedelta
from blackbaud.school.endpoints import attendance

# Let's say we want to create an attendance record for a student who
# was absent between 08:00 and 11:00 for a dentist's appointment on
# January 25th, 2023.

# Python lets us represent dates and times as datetime objects:
absent_from = datetime(2023, 1, 25, 8, 0)
absent_to = datetime(2023, 1, 25, 11, 0)

# And we can use these objects to call the API:
attendance_record = create_attendance_record(
    client=school, 
    user_id=SOME_USER_ID,
    start_date=absent_from,
    end_date=absent_to,
    specify_time=True,
    excuse_comment="Dentist's Appointment"
)

# or:
attendance_record = create_attendance_record(
    client=school, 
    user_id=SOME_USER_ID,
    start_date=absent_from,
    end_date=absent_from + timedelta(hours=3),
    specify_time=True,
    excuse_comment="Dentist's Appointment"
)
```

## Rate Limits and Caching

Rate limits and caching are both supported out of the box:

```python
from redis import Redis
from requests_cache.backends.redis import RedisCache

from blackbaud.client.rate_limiters.default import UPGRADED_TIER_1

# Use Redis instead of SQLite for caching
redis_cache = RedisCache(namespace="python_blackbaud")

client = SKYAPIClient(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    subscription_key=BB_API_SUBSCRIPTION_KEY, 
    redirect_uri=REDIRECT_URI,
    # Subscribe to the paid tiers of the SKY API? Indulge yourself:
    rate_limits=UPGRADED_TIER_1,
    # Set Redis as the cache backend:
    cache_backend=redis_cache
)
```

## To Do

- [ ] Write documentation
- [ ] Implement RE NXT endpoints
- [ ] Implement Payments endpoints
- [ ] Write higher-level abstractions
- [ ] Write tests
