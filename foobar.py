"""
Foobar module
"""

import os


def cli():
    print(f"hello {os.environ['USER']}")


if __name__ == "__main__":
    cli()
