from elastic_status import ElasticsearchConfiguration, StatusApp

ElasticsearchConfiguration.from_config('config.json')

StatusApp.run()
