import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

from sketch_data.catalog_primitive.line import Line


CATALOG = {'Line' : Line}

def create_cad_object(label, **kwargs):
    try:
        return CATALOG[label](**kwargs)
    except KeyError:
        logger.debug(f'Label {label} does not exist.')
        return None