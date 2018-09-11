import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from config import Config, HostDB

def _request(method, endpoint, data=None):
    try:
        r = requests.request(
            method=method,
            url=f"{Config.FUSION_URL}/{endpoint}",
            headers={
                "Content-Type": "application/json",
            },
            data=data
        )

        return r.json()

    except requests.exceptions.ReadTimeout:
        pass

    return

def get_vms():
    return HostDB.get_hosts()

def restart(vm):
    return _request('POST', f'vms/{vm}/restart')

# Jettisoning VMware Fusion API code as it is terribly slow
#
# def _request(method, endpoint, data=None, timeout=600):
#     try:
#         r = requests.request(
#             method=method,
#             url=f"{Config.FUSION_URL}/api/{endpoint}",
#             headers={
#                 "Accept": "application/vnd.vmware.vmw.rest-v1+json",
#                 "Authorization": f"Basic {Config.FUSION_AUTH}",
#                 "Content-Type": "application/vnd.vmware.vmw.rest-v1+json",
#             },
#             data=data,
#             verify=False,
#             # hack because Fusion API is slow
#             # timeout=3
#             timeout=timeout
#         )
#
#         print(r.json())
#
#     except requests.exceptions.ReadTimeout:
#         pass
#
#     return
#
# def get_vms():
#     return _request('GET', 'vms')
#
# def restart(vm):
#     vm_id = HostDB.INFO.get(vm)['id']
#     _request('PUT', f"vms/{vm_id}/power", 'off')
#     _request('PUT', f"vms/{vm_id}/power", 'on', timeout=1)
#     return { "status": "restart complete" }
