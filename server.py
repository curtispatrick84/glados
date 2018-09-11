#!/usr/bin/env python
import hug
import falcon
import logging
import json

from fusion import get_vms, restart
from pxe import set_pxe_config

@hug.get('/vms')
def list_vms():
    return get_vms()


@hug.post('/vms/{vm}/restart')
def restart_vm(vm):
    return restart(vm)


@hug.post('/vms/{vm}/pxe_setup')
def set_pxe(vm, body, response=None):
    print(vm, body)
    if body is not None and body.get('os') is not None:
        return set_pxe_config(vm, body.get('os'))

    response.status = falcon.HTTP_422
    return 'OS specification is required'


@hug.not_found()
def not_found_handler(response=None):
    response.status = falcon.HTTP_404
    return "Not Found"


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(asctime)s - %(funcName)s: %(message)s', level=logging.INFO)

    hug.API(__name__).http.serve(port=8080)
