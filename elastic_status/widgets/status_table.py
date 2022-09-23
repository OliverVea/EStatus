from rich.align import Align
from textual.widget import Widget

from elastic_status.models.elasticsearch_configuration import Configuration
from elastic_status.services.elasticsearch import get_status

class StatusTable(Widget):
    def on_mount(self):
        self.set_interval(Configuration.config.refresh_seconds, self.refresh)

    def render(self):
        try:
            status = get_status(Configuration.config)
            table = status.to_table()
            return Align.center(table)  
        except Exception as e:
            return Align.center('Lost connection to elasticsearch.\nMessage:\n' + str(e), vertical='bottom')