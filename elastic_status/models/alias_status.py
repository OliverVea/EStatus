from elastic_status.models.tracked_alias import TrackedAlias
from elastic_status.models.alias import Alias
from elastic_status.models.index import Index

from rich.table import Table

class AliasStatus:
    def __init__(self, tracked_alias: TrackedAlias, alias: Alias, indices: list[Index]):
        self.name = tracked_alias.name
        self.alias = alias.alias
        self.indices = indices

    def add_rows(self, table: Table):
        raise Exception("Implement me OOOO")
