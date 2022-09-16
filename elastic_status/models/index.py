from elastic_status.constants import WEEK, DAY, HOUR, MINUTE
import time

class Index:
    def __init__(self, index: str, health: str, **kwargs):
        self.index = index
        self.health = health
        self.document_count = kwargs['docs.count']
        self.created = kwargs['creation.date']

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
