from elastic_status import Alias, Index, ElasticsearchConfiguration, ElasticsearchStatus, AliasStatus
import requests

def cat_aliases(config: ElasticsearchConfiguration) -> list[Alias]:
    url = 'http://' + config.get_url() + '/_cat/aliases'
    response = requests.get(
        url, params={'format': 'application/json', 'h': 'alias,index'})
    response = response.json()
    aliases = [Alias(**alias) for alias in response]
    return aliases


def cat_indices(config: ElasticsearchConfiguration) -> list[Index]:
    url = 'http://' + config.get_url() + '/_cat/indices'
    response = requests.get(url, params={
                            'format': 'application/json', 'h': 'index,health,docs.count,creation.date'})
    response = response.json()
    indices = [Index(**index) for index in response]
    return indices


def get_status(config: ElasticsearchConfiguration) -> ElasticsearchStatus:
    elasticsearch_status = ElasticsearchStatus(config)

    aliases = cat_aliases(config)
    aliases = {alias.alias: alias for alias in aliases}

    indices = cat_indices(config)
    indices = {index.index: index for index in indices}

    for tracked_alias in config.tracked_aliases:
        if not tracked_alias.alias in aliases:
            elasticsearch_status.add_alias(tracked_alias.name, None)
            continue

        alias = aliases[tracked_alias.alias]

        if not alias.index in indices:
            elasticsearch_status.add_alias(tracked_alias.name, None)
            continue

        index = indices[alias.index]

        alias_status = AliasStatus(tracked_alias, alias, index)

        elasticsearch_status.add_alias(tracked_alias.name, alias_status)

    return elasticsearch_status
