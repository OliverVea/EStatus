import requests
from requests.models import Response
from urllib.parse import urljoin

class OidcConfiguration:
    def __init__(self, authority: str, identity: str, scope: str, client_id: str, client_secret: str, **_):
        self.authority = authority
        self.identity = identity
        self.scope = scope
        self.client_id = client_id
        self.client_secret = client_secret

def get_token(config: OidcConfiguration, verify: bool = False):
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'audience': config.scope,
        'client_id': config.client_id,
        'client_secret': config.client_secret
    }

    url = urljoin(config.authority, 'connect/token')

    response = requests.post(url, headers=headers, data=data, verify=verify, timeout=1)
    content = response.json()

    return content['access_token']

def disable_insecure_request_warning():
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from urllib.parse import urljoin

class Request:
    def __init__(self,
        host: str,
        port: str,
        endpoint: str,
        token: str = None,
        headers: dict = {},
        parameters: dict = {}
    ):
        self.host = host
        self.port = port
        self.endpoint = endpoint
        self.token = token.strip()

        self.headers = headers
        self.parameters = parameters
    
    def get_base(self):
        return f'{self.host}:{self.port}'

    def get_url(self):
        base = self.get_base()
        return urljoin(base, self.endpoint)

    def get_headers(self):
        headers = self.headers
        
        if self.token:
            headers.update({'authorization': f'Bearer {self.token}'})
    
        return headers

    def __str__(self):
        contents = {}
        contents['Request URL'] = self.get_url()
        contents['Request Headers'] = self.headers

        return str(contents)

    def get(self, verify: bool = False) -> Response:
        return requests.get(
            url = self.get_url(),
            headers = self.get_headers(),
            params = self.parameters,
            verify = verify,
            timeout=0.5
        )

    def post(self, data: str, verify: bool = False) -> Response:
        return requests.post(
            url = self.get_url(),
            headers = self.get_headers(),
            params = self.parameters,
            data = data,
            verify = verify,
            timeout=0.5
        )

    def put(self, data: str, verify: bool = False) -> Response:
        return requests.put(
            url = self.get_url(),
            headers = self.get_headers(),
            params = self.parameters,
            data = data,
            verify = verify,
            timeout=0.5
        )
    
    def delete(self, verify: bool = False) -> Response:
        return requests.delete(
            url = self.get_url(),
            headers = self.get_headers(),
            params = self.parameters,
            verify = verify,
            timeout=0.5
        )


def ecommercesearch(config: OidcConfiguration, endpoint: str, parameters: dict = {}):
    token = get_token(config)

    request = Request(
        host="https://localhost",
        port="5124",
        endpoint=endpoint,
        token=token,
        parameters = parameters,
        headers={'content-type': 'application/json'}
    )

    return request