from main import app, logger
from .get_app_info import get_app_info_task
import utils.storage
import utils.steam
import config
import logging


@app.task(name="check_missing_apps")
def check_missing_apps_task():
    """
    Check for missing stored apps by comparing them with
    all available apps in Steam and start tasks to
    retrieve the info for the missing apps.
    """

    steam_apps = utils.steam.get_app_list()

    stored_apps = utils.storage.list("app/")
    stored_apps_list = []
    for app in stored_apps:
        print(app)
        app_id = app.split(".")[0]
        app_ext = app.split(".")[1]
        if app_ext == "json":
            stored_apps_list.append(int(app_id))

    diff = utils.helper.list_differences(steam_apps, stored_apps_list)

    for i in range(0, len(diff), config.chunk_size):
        chunk = diff[i : i + config.chunk_size]
        get_app_info_task.delay(chunk)
