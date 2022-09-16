from elastic_status.models.tracked_alias import TrackedAlias
from elastic_status.models.alias import Alias
from elastic_status.models.index import Index
from elastic_status.constants import WEEK, DAY, HOUR, MINUTE
import time

class AliasStatus:
    def __init__(self, tracked_alias: TrackedAlias, alias: Alias, index: Index):
        self.name = tracked_alias.name
        self.alias = alias.alias
        self.index = index.index
        self.document_count = int(index.document_count)
        self.health = index.health
        self.created = int(index.created)

    def get_status(self) -> str:
        if self.health == 'green':
            return 'H'
        return '?'

    def get_age(self) -> str:
        delta = time.time() - self.created / 1000

        if delta > WEEK: factor, unit = WEEK, 'w'
        elif delta > DAY: factor, unit = DAY, 'd'
        elif delta > HOUR: factor, unit = HOUR, 'h'
        elif delta > MINUTE: factor, unit = MINUTE, 'm'
        else: factor, unit = 1, 's'

        return f'{int(delta / factor):d}{unit}'

    def get_document_count(self) -> str:
        if self.document_count > 1e6:
            return f'{(self.document_count / 1e6):.1f}m'
        if self.document_count > 1e3:
            return f'{(self.document_count / 1e3):.1f}k'
        return f'{self.document_count // 1}'
