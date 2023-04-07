from pathlib import Path
from os import listdir
from importlib import import_module


path_parent = Path('./app/routers')
for module in listdir(path_parent):
    if 'route' in module:
        import_module(
            f'app.routers.{module[:-3]}'
        )