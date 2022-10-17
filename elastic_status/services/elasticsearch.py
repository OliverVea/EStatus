import requests
import logging

from elastic_status.models import Alias, Index, Configuration, ElasticsearchStatus, AliasStatus

def cat_aliases(config: Configuration) -> list[Alias]:
    url = 'http://' + config.get_url() + '/_cat/aliases'
    logging.info('Requesting aliases from elasticsearch: {Url}', url)
    params = {'format': 'application/json', 'h': 'alias,index'}
    response = requests.get(url, params=params, timeout=0.5)
    response = response.json()
    aliases = [Alias(**alias) for alias in response]
    logging.info('Got %d aliases: %s', len(aliases), ', '.join(alias.alias for alias in aliases))
    return aliases


def cat_indices(config: Configuration) -> list[Index]:
    url = 'http://' + config.get_url() + '/_cat/indices'

    params = {'format': 'application/json', 'h': 'index,health,docs.count,creation.date'}
    response = requests.get(url, params=params, timeout=0.5)
    response = response.json()
    indices = [Index(**index) for index in response]
    return indices


def get_status(config: Configuration) -> ElasticsearchStatus:
    elasticsearch_status = ElasticsearchStatus(config)

    aliases = cat_aliases(config)
    aliases = {alias.alias: alias for alias in aliases}

    indices = cat_indices(config)
    indices = {index.index: index for index in indices}

    for tracked_alias in config.tracked_aliases:
        if tracked_alias.alias in aliases:
            alias = aliases[tracked_alias.alias]
        else:
            alias = Alias(tracked_alias.alias, '')

        alias_indices = [indices[index_name] for index_name in indices if tracked_alias.index_in_alias(index_name)]

        alias_status = AliasStatus(tracked_alias, alias, alias_indices)

        elasticsearch_status.add_alias(tracked_alias.name, alias_status)

    return elasticsearch_status


def clear_indices(config: Configuration):
    url = 'http://' + config.get_url() + '/*b2c-dk-da*'
    requests.delete(url, timeout=0.5)