# Kartvelian Department of Operational Finance game i think

from rich.console import Console
from rich.panel import Panel

from textual.app import App
from textual.widgets import Placeholder, Button, ButtonPressed
from textual.reactive import Reactive
from textual.widget import Widget


console = Console()

class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hover Button", style=("on red" if self.mouse_over else ""))


    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_click(self, event) -> None:
        self.render(Panel("Clicked!", style=("on teal")))

class HoverApp(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(10))
        await self.view.dock(*hovers, edge="top")


#async def load_menu() -> None:

class Doof(App):

    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        await self.view.dock(Hover(), edge="left", size=20)
        await self.view.dock(Placeholder(), Placeholder(), edge="top")

#console.print("[blue underline]Looks like a link")
#HoverApp.run(log="events.log")

Doof.run(log="events.log")
