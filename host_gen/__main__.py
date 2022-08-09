import os.path
from glob import iglob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TARGET = os.path.abspath(os.path.join(os.getcwd(), "10-adbhosts.txt"))
CACHE = set()
WL_CACHE = set()
ITERATOR = iglob("./data/blocklist/**.txt")
WL_ITERATOR = iglob("./data/whitelist/**.txt")


def make_host(url):
    """make_host: converts an url to a valid hosts file entry"""
    return "0.0.0.0 {url}".format(url=url)


def make_cache():
    """make_cache: reads all files in ./data/blacklists/ and caches them in CACHE"""
    logger.info("Caching blacklists")
    for entry in ITERATOR:
        with open(entry, "r") as fin:
            for url in fin.readlines():
                if url[0] == "#":
                    continue
                logger.debug("Adding {} to blacklist".format(url))
                CACHE.add(make_host(url))


def make_host_file():
    """make_host_file: writes hosts file to Target"""
    with open(TARGET, "w") as fout:
        logger.info("Writing host file")
        fout.writelines((host.strip() for host in CACHE.difference(WL_CACHE)))


def make_whitelist():
    """make_cache: reads all files in ./data/whitelists/ and caches them in WL_CACHE"""
    logger.info("Caching whitelists")
    for entry in WL_ITERATOR:
        with open(entry, "r") as fin:
            for url in fin.readlines():
                if url[0] == "#":
                    continue
                logger.debug("Adding {} to whitelist".format(url))
                WL_CACHE.add(make_host(url))


def main():
    make_cache()
    make_whitelist()
    make_host_file()


if __name__ == "__main__":
    main()
