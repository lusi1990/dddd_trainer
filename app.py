#! /usr/bin/env python
import fire

from loguru import logger
from utils import project_manager
from utils import cache_data
from utils import train


class App:

    def create(self, project_name: str, single: bool = False):
        logger.info("\nCreate Project ----> {}", project_name)
        pm = project_manager.ProjectManager()
        pm.create_project(project_name, single)

    def cache(self, project_name: str, base_path: str, search_type: str = "name"):
        logger.info("\nCaching Data ----> {}\nPath ----> {}", project_name, base_path)
        cache = cache_data.CacheData(project_name)
        cache.cache(base_path, search_type)

    def train(self, project_name: str):
        logger.info("Start Train ----> {}", project_name)
        trainer = train.Train(project_name)
        trainer.start()


if __name__ == '__main__':
    fire.Fire(App)
