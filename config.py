import os

class Config():
    # FUSION_AUTH = os.environ.get('AUTH')
    FUSION_URL = os.environ.get('FUSION_API_URL')

    PXE_SERVER_URL = os.environ.get('PXE_SERVER', '127.0.0.1:8069')

class HostDB():
    INFO = {
        "node01": {
            "ip": "10.0.0.10",
            "mac": "00:0C:29:12:0F:C5"
        },
        "node02": {
            "ip": "10.0.0.11",
            "mac": "00:50:56:3E:98:9A"
        },
        "node03": {
            "ip": "10.0.0.12",
            "mac": "00:50:56:3E:98:9A"
        }
    }
