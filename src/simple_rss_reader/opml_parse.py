import xml.etree.ElementTree as ET
from pathlib import Path


def opml_parser(opml_link: str) -> list[str]:
    """
    - parses the opml file and returns a list of all the links
    - does not use package as implementation is quite simple
    """
    opml_list = []
    if Path(opml_link).suffix != ".opml":
        raise ValueError("The file must be .opml file")
    tree = ET.parse(opml_link)
    root = tree.getroot()
    for outline_element in root.findall(".//outline"):
        feed_url = outline_element.attrib.get("xmlUrl")
        if feed_url:
            opml_list.append(feed_url)
    return opml_list
