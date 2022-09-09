from elastic_status import ElasticsearchConfiguration, get_status
from os import system
import time

config = ElasticsearchConfiguration.from_config('config.json')

while True:
    status = get_status(config)
    status.print()

    time.sleep(config.refresh_seconds)
    system('cls')
