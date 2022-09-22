from elastic_status import Configuration, StatusApp

Configuration.from_config('config.json')

StatusApp.run()
