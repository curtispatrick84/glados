import docker

client = docker.from_env()

def clean_puppet_cert(vm):
    container = client.containers.get('puppet')
    output = container.exec_run(f'puppet cert clean {vm}.aperture.com')

    if 'Revoked certificate' in output.output:
        return { 'status': 'success' }

    return { 'status': 'fail' }
