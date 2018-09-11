import os
import requests

from config import Config, HostDB

def set_pxe_config(host, os):
    hosts = HostDB.get_hosts()
    r = requests.post(
        url=f"http://{Config.PXE_SERVER_URL}/pxeconfig",
        headers={
            "Content-Type": "application/json"
        },
        json={
            "mac": hosts.get(host)['mac'],
            "os": os
        }
    )

    if r.status_code != requests.codes.ok:
        r.raise_for_status()

    return r.json()
