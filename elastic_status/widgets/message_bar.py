from rich.align import Align
from textual.widget import Widget

class MessageBar(Widget):
    def _set_message(self, message: str):
        self.message = message
        self.refresh()

    def _timer(self):
        self._set_message('')

    def set_message(self, message):
        self._set_message(message)
        self.set_timer(self.timer_time, self._timer, name='clear_message')

    def on_mount(self):
        self.timer_time = 5
        self._set_message('')

    def render(self):
        return Align.left(self.message, vertical='bottom')