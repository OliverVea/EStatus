from rich.align import Align

from textual.app import App
from textual.widget import Widget
from textual.widgets import Footer

from elastic_status.elasticsearch import get_status
from elastic_status.models.elasticsearch_configuration import ElasticsearchConfiguration


class StatusTable(Widget):
    def on_mount(self):
        self.set_interval(ElasticsearchConfiguration.config.refresh_seconds, self.refresh)

    def render(self):
        try:
            status = get_status(ElasticsearchConfiguration.config)
            table = status.to_table()
            return Align.center(table)  
        except Exception as e:
            return Align.center('Lost connection to elasticsearch.\nMessage:\n' + str(e))


class StatusApp(App):
    async def on_mount(self):
        await self.view.dock(StatusTable())
        await self.view.dock(Footer(), edge='bottom')
