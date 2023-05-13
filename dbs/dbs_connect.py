from .queries import create_connection
from .set_config import config


def connect():
    connections = config.dbs_connections.get_secret_value().split(",")
    connections_ref = {}

    for connection in connections:
        name, path = connection.split(":")
        ref = create_connection(path)
        connections_ref[name] = ref

    return connections_ref


connections = connect()
