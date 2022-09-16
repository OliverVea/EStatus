import re


class TrackedAlias:
    def __init__(self, name: str, alias: str, index_pattern: str, **_):
        self.name = name
        self.alias = alias
        self.index_pattern = re.compile(index_pattern)

    def index_in_alias(self, index: str) -> bool:
        return self.index_pattern.match(index) != None