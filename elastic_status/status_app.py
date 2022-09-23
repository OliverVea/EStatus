from textual.events import Load
from textual.app import App
from textual.widgets import Footer

from elastic_status.models.elasticsearch_configuration import Configuration
from elastic_status.services.elasticsearch import  clear_indices
from elastic_status.services.ecommercesearch import publish
from elastic_status.widgets import MessageBar, StatusTable

class StatusApp(App):
    async def on_load(self, event: Load) -> None:
        await self.bind('q', 'quit', 'Quit')
        await self.bind('c', 'clear_indices', 'Clear indices')
        await self.bind('p', 'publish', 'Publish')

    async def action_clear_indices(self) -> None:
        try:
            clear_indices(Configuration.config)
        except Exception as e:
            self.message_bar.set_message(str(e))

    async def action_publish(self) -> None:
        try:
            publish(Configuration.config)
        except Exception as e:
            self.message_bar.set_message(str(e))

    async def on_mount(self):
        grid = await self.view.dock_grid(edge='bottom')
        self.message_bar = MessageBar()
        grid.add_column('')
        grid.add_row('content')
        grid.add_row('message', size=4)
        grid.add_row('footer', size=1)

        grid.place(StatusTable(), self.message_bar, Footer())
