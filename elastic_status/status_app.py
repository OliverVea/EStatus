from rich.align import Align

from textual.events import Load
from textual.app import App
from textual.widget import Widget
from textual.widgets import Footer, Button, ButtonPressed

from elastic_status.elasticsearch import get_status, delete_indices
from elastic_status.ecommercesearch import publish
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
    async def on_load(self, event: Load) -> None:
        await self.bind('q', 'quit', 'Quit')
        await self.bind('c', 'delete_indices', 'Clear indices')
        await self.bind('p', 'publish', 'Publish')

    async def action_delete_indices(self) -> None:
        delete_indices(ElasticsearchConfiguration.config)

    async def action_publish(self) -> None:
        publish(ElasticsearchConfiguration.config)

    async def on_mount(self):
        await self.view.dock(Footer(), edge='bottom')
        await self.view.dock(StatusTable(), edge='top')
