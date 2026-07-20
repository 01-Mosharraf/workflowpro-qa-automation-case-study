from pathlib import Path


def capture(page, name):

    folder = Path("screenshots")

    folder.mkdir(exist_ok=True)

    page.screenshot(
        path=f"screenshots/{name}.png"
    )