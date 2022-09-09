from elastic_status.models.elasticsearch_configuration import ElasticsearchConfiguration
from elastic_status.models.alias_status import AliasStatus

class ElasticsearchStatus:
    def __init__(self, config: ElasticsearchConfiguration):
        self.config = config
        self.aliases: dict[str, AliasStatus] = {}

    def add_alias(self, name: str, alias_status: AliasStatus):
        if alias_status.name in self.aliases:
            return
        self.aliases[name] = alias_status

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
