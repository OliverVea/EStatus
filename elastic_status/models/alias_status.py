from elastic_status.models.tracked_alias import TrackedAlias
from elastic_status.models.alias import Alias
from elastic_status.models.index import Index

from rich.table import Table
from textual.widgets import Button

class AliasStatus:
    def __init__(self, tracked_alias: TrackedAlias, alias: Alias, indices: list[Index]):
        self.name = tracked_alias.name
        self.alias = alias
        self.indices = indices

    def add_rows(self, table: Table):
        self._draw_aliased_index(table)
        self._draw_other_indices(table)

    def _draw_aliased_index(self, table: Table) -> None:
        aliased_index = self._get_aliased_index()
        if aliased_index == None: return
        self._draw_index(table, aliased_index, highlighted=True)


    def _get_aliased_index(self):
        aliased_indices = [index for index in self.indices if self.alias.index == index.index]
        return aliased_indices[0] if len(aliased_indices) > 0 else None

    def _draw_other_indices(self, table: Table):
        other_indices = [index for index in self.indices if index.index != self.alias.index]
        other_indices = list(sorted(other_indices, key=lambda i: i.created, reverse=True))

        if len(other_indices) > 5:
            self._draw_summarized_index_list(table, other_indices)
            return

        for index in other_indices:
            if index.index == self.alias.index: continue
            self._draw_index(table, index)

    def _draw_summarized_index_list(self, table: Table, indices: list[Index]):
        self._draw_index(table, indices[0])
        self._draw_index(table, indices[1])
        table.add_row('...')
        self._draw_index(table, indices[-2])
        self._draw_index(table, indices[-1])

    def _draw_index(self, table: Table, index: Index, highlighted: bool = False):
        row = [
            self.alias.alias if highlighted else '',
            index.index,
            index.get_status(),
            index.get_age(),
            index.get_document_count()
        ]

        table.add_row(*row, style='bold' if highlighted else 'dim')
