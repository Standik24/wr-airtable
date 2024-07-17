from keboola import docker
import os


class Configuration:
    def __init__(self):
        self.config = docker.Config(os.getenv('KBC_DATADIR'))
        self.app_id = self.config.get_parameters()["app_id"]
        self.table_id = self.config.get_parameters()["table_id"]
        self.column_name = self.config.get_parameters()["column_name"]
        self.token = self.config.get_parameters()["token"]
