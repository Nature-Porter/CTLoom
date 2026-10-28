"""Shared CTLoom identity for terminal and browser interfaces."""

from importlib.resources import files
from urllib.parse import quote

from ctloom import __version__

APP_NAME = "CTLoom"
DISPLAY_VERSION = f"v{__version__}"

# A compact woven C/T monogram, matching the geometry of assets/icon.svg.
TERMINAL_MARK = (
    (("╭━━", "#a78bfa"), ("┳━━", "#67e8f9")),
    (("┃  ", "#a78bfa"), ("╋", "#67e8f9"), ("━ ", "#f0b45c")),
    (("╰━━", "#a78bfa"), ("┛  ", "#67e8f9")),
)


def icon_svg() -> str:
    """Read the packaged vector source used by every browser brand mark."""
    return files("ctloom").joinpath("assets", "icon.svg").read_text(encoding="utf-8")


def favicon_uri() -> str:
    """Embed the icon so remote mode doesn't need an extra asset endpoint."""
    return "data:image/svg+xml," + quote(icon_svg(), safe="")
