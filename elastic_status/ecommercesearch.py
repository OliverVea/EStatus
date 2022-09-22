from elastic_status.models.elasticsearch_configuration import Configuration

import elastic_status.request as r

r.disable_insecure_request_warning()

def ecommercesearch(endpoint: str, parameters: dict = {}):
    token = r.get_token("searchapi/")

    request = r.Request(
        host="https://localhost",
        port="5124",
        endpoint=endpoint,
        token=token,
        parameters = parameters,
        headers={'content-type': 'application/json'}
    )

    return request

def publish(config: Configuration) -> None:
    ecommercesearch(f'/api/search/segments/{config.segment}/publication/_publish').post('{"comment": "EStatus publication"}')