import logging
import pathlib
import sys

from trestle.oscal.catalog import Catalog
from trestle.core.control_context import ControlContext, ContextPurpose
from trestle.core.catalog.catalog_api import CatalogAPI

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

def demo():

    try:
        # Load a catalog.json into a Catalog object.
        catalog_path = pathlib.Path('catalogs/mobile-app-security-standard/catalog.json')
        c = Catalog.oscal_read(catalog_path)
        logger.info(f"Successfully read catalog from {catalog_path}")
    except Exception as e:
        logger.error(f"Error reading catalog from {catalog_path}")
        return
    
    # Create an instance of the ControlContext class.
    root_path = pathlib.Path('/')
    md_path = pathlib.Path('catalogs/docs')
    cc = ControlContext.generate(purpose=ContextPurpose.CATALOG, 
                                 to_markdown=True, 
                                 trestle_root=root_path, 
                                 md_root=md_path)

    # Create an instance of the CatalogAPI class.
    # Use the CatalogAPI instance to write catalog.json as markdown.
    c_api = CatalogAPI(catalog=c, context=cc)
    logger.info("Created CatalogAPI instance.")

    try:
        c_api.write_catalog_as_markdown(label_as_key=False)
        logger.info("Catalog successfully written as markdown.")
    except Exception as e:
        logger.error(f"Error writing catalog as markdown: {e}")
        return
    
    logger.info("Catalog processing complete.")

if __name__ == '__main__':
    demo()