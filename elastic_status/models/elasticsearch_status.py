from elastic_status.models.elasticsearch_configuration import ElasticsearchConfiguration
from elastic_status.models.alias_status import AliasStatus

from rich.table import Table

class ElasticsearchStatus:
    def __init__(self, config: ElasticsearchConfiguration):
        self.config = config
        self.aliases: dict[str, AliasStatus] = {}

    def add_alias(self, name: str, alias_status: AliasStatus):
        if name in self.aliases: return
        self.aliases[name] = alias_status

    def to_table(self) -> Table:
        table = Table(title='Elasticsearch Tracked Aliases')
        
        table.add_column('Name', justify='left')
        table.add_column('Alias', justify='left')
        table.add_column('Status', justify='center')
        table.add_column('Created', justify='right')
        table.add_column('Docs', justify='right')

        for name, alias in zip(self.aliases, self.aliases.values()):
            if not alias: 
                table.add_row(name, 
                        '', 
                        '-', 
                        '', 
                        '')
            else:
                table.add_row(name, 
                        alias.alias, 
                        alias.get_status(), 
                        alias.get_age(), 
                        alias.get_document_count())

        return table
        
    """
    def print(self):
        # print status
        print(f'Elasticsearch Instance: {self.config.get_url()}')

        # alias table
        table = PrettyTable(['name', 'alias', 'status', 'created', 'docs'])
        for name, alias in zip(self.aliases, self.aliases.values()):
            if not alias:
                table.add_row([name, '', '-', '', ''])
            else:
                table.add_row([name, alias.alias, alias.get_status(
                ), alias.get_age(), alias.get_document_count()])
        print(table)
    """
