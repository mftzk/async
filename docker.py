import docker

def run_container():
    client = docker.from_env()
    container = client.containers.run('ubuntu:latest', 'ls -ltr /tmp', volumes={os.getcwd(): {'bind': '/tmp/', 'mode': 'rw'}}, detach=True)
    print(container.logs())