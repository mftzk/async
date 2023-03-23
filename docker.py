import docker
import os

def run_container():
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    container = client.containers.run('ubuntu:latest', 'ls -ltr /tmp', volumes={os.getcwd(): {'bind': '/tmp', 'mode': 'rw'}}, detach=True)
    print(container.logs())

run_container()