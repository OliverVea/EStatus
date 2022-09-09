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
        if delta > WEEK:
            return f'{int(delta / WEEK):d}w'
        if delta > DAY:
            return f'{int(delta / DAY):d}d'
        if delta > HOUR:
            return f'{int(delta / HOUR):d}h'
        if delta > MINUTE:
            return f'{int(delta / MINUTE):d}m'
        return f'{delta // 1}s'

    def get_document_count(self) -> str:
        if self.document_count > 1e6:
            return f'{(self.document_count / 1e6):.1f}m'
        if self.document_count > 1e3:
            return f'{(self.document_count / 1e3):.1f}k'
        return f'{self.document_count // 1}'
