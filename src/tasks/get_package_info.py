from main import app, logger
import utils.storage
import utils.steam
import logging
import json


@app.task(name="get_package_info", time_limit=3, autoretry_for=(SoftTimeLimitExceeded,), retry_kwargs={'max_retries': 3, 'countdown': 5})
def get_package_info_task(packages=[]):
    """
    Get package information of input list of packages, generate
    separate json files and upload them to the store.
    """

    logger.info("Getting product info for following packages: " + str(packages))
    packages = utils.steam.get_packages_info(packages)

    for package in packages:
        content = json.dumps(packages[package])
        write = utils.storage.write(content, "package/", str(package) + ".json")
