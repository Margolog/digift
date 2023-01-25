
from voluptuous import Schema, Optional

js = Schema(
    {
        'name': 'Alcatel',
        'sort_field': 'name'
    },
    Optional('search', 'sort_field')
)
