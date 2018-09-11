import docker

client = docker.from_env()

def update_reservation(vm, ip, mac):
    container = client.containers.get('dhcp')
    output = container.exec_run('cat /etc/dhcp/dhcpd.conf')

    file = output.output.decode('utf-8').splitlines()
    file.insert(14, f'    host {vm} {{ hardware ethernet {mac}; fixed-address {ip}; }}')

    newfile = '\n'.join(file)

    output = container.exec_run(['sh', '-c', f"echo -e '{newfile}' > /etc/dhcp/dhcpd.conf"])
    print(output)
    container.restart()

    return { 'success': True }
