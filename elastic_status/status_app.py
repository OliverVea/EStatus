from textual.app import App

from datetime import datetime

from rich.align import Align

from textual.app import App
from textual.widget import Widget

from elastic_status.elasticsearch import get_status
from elastic_status.models.elasticsearch_configuration import ElasticsearchConfiguration


class StatusTable(Widget):
    def on_mount(self):
        self.set_interval(ElasticsearchConfiguration.config.refresh_seconds, self.refresh)

    def render(self):
        status = get_status(ElasticsearchConfiguration.config)
        return status.to_table()


class StatusApp(App):
    async def on_mount(self):
        await self.view.dock(StatusTable())
