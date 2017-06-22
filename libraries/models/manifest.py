from __future__ import unicode_literals, print_function
from libraries.models.model import Model


class TxManifest(Model):
    db_keys = [
        'repo_name',
        'user_name',
    ]

    db_fields = [
        'repo_name',
        'user_name',
        'lang_code',
        'resource_id',
        'resource_type',
        'title',
        'views',
        'last_updated',
        'manifest',
    ]

    default_values = {
        'views': 0,
        'manifest': {},
    }

    def __init__(self, data=None, **kwargs):
        # Init attributes
        self.repo_name = None
        self.user_name = None
        self.lang_code = None
        self.resource_id = None
        self.resource_type = None
        self.title = None
        self.views = 0
        self.last_updated = None
        self.manifest = {}

        super(TxManifest, self).__init__(**kwargs)

        if isinstance(data, dict):
            self.populate(data)
            if self.db_handler and len(data) == 2 and 'repo_name' in data and 'user_name' in data:
                self.load()
