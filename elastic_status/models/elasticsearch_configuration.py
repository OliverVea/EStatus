from elastic_status.models.tracked_alias import TrackedAlias
import json

from elastic_status.services.request import OidcConfiguration

class Configuration:
    def __init__(self, hostname: str, port: int, refresh_seconds: float, tracked_aliases: list[dict], segment: str, oidc: dict, **_):
        self.hostname = hostname
        self.port = port
        self.refresh_seconds = refresh_seconds
        self.tracked_aliases = [TrackedAlias(**tracked_alias) for tracked_alias in tracked_aliases]
        self.segment = segment
        self.oidc = OidcConfiguration(**oidc)

    def get_url(self):
        return f'{self.hostname}:{self.port}'

    @staticmethod
    def from_config(path: str):
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        Configuration.config = Configuration(**config)
        return config
