# Kartvelian Department of Operational Finance game i think

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from textual.app import App
from textual.widgets import Placeholder, Button, ButtonPressed
from textual.reactive import Reactive
from textual.widget import Widget

georgia_text = "საქართველო"

console = Console()

class Hover(Widget):

    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel(f"{georgia_text}", style=("on red" if self.mouse_over else ""))


    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(10))
        await self.view.dock(*hovers, edge="top")


#async def load_menu() -> None:

class DoofConsole(Widget):

    def render(self) -> Console:
        return Console()

class Doof(App):

    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        await self.view.dock(Hover(), edge="left", size=20)
        await self.view.dock(DoofConsole(), edge="top")

#console.print("[blue underline]Looks like a link")
HoverApp.run(log="events.log")


class TestMenuTable(Widget):
    def render(self) -> Table:
        t = Table(show_header=True, header_style="bold")
        t.add_column("Name")
        t.add_column("Age")

        t.add_row("Jason", "[teal]21[/teal]")
        return t

class TestMenu(App):
    async def on_load(self) -> None:
        await self.bind("q", "quit")
    
    async def on_mount(self):
        await self.view.dock(TestMenuTable(), edge="top")
        await self.view.dock(Placeholder(), edge="left", size=25)

#TestMenu.run(log="events.log")