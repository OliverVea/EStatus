from elastic_status.models.elasticsearch_configuration import ElasticsearchConfiguration

import oliversmoduler.request as r
import oliversmoduler.get_tokens as gt

r.disable_insecure_request_warning()


def ecommercesearch(endpoint: str, parameters: dict = {}):
    token = gt.get_token("searchapi/")

    request = r.Request(
        host="https://localhost",
        port="5124",
        endpoint=endpoint,
        token=token,
        parameters = parameters,
        headers={'content-type': 'application/json'}
    )

    return request

def publish(config: ElasticsearchConfiguration) -> None:
    ecommercesearch(f'/api/search/segments/{config.segment}/publication/_publish').post('{"comment": "EStatus publication"}')