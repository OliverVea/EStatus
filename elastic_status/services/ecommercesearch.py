import json
from elastic_status.models.elasticsearch_configuration import Configuration

import elastic_status.services.request as r

r.disable_insecure_request_warning()

def publish(config: Configuration) -> None:
    url = f'/api/search/segments/{config.segment}/publication/_publish'
    body = json.dumps({'comment': 'EStatus publication'})
    r.ecommercesearch(config.oidc, url).post(body)