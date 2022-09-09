from elastic_status import ElasticsearchConfiguration, StatusApp

config = ElasticsearchConfiguration.from_config('config.json')
StatusApp.run()
