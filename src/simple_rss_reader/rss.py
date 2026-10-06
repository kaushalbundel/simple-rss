import feedparser
import nh3
from rich import print
from simple_rss_reader.opml_parse import opml_parser

# d = feedparser.parse("https://travelsofsamwise.substack.com/feed")

# feed related information
# print(d.feed)  # feed object
# print(d.feed.title)  # feed title
# print(d.feed.link)  # feed link
#
# Feed entry related information
# print(d.entries[0].title)
# print(d.entries[0].description)
# print(d.entries[0].link)
# print(d.entries[0].published)
# print(d.entries[0].content)


# print(d.entries[0].content[0].value)  # the printed image is not readable.
# create a function that prints the last 5 feed and related information


def sanitize_html(html_string: str):
    """Sanitizes the HTML content coming from the feed"""
    allowed_tags = {
        "p",
        "span",
        "a",
        "b",
        "i",
        "strong",
        "em",
        "ul",
        "ol",
        "li",
        "blockquote",
        "sup",
        "sub",
    }

    # Allowed attributes
    allowed_attributes = {"a": {"href", "title"}, "img": {"src", "alt"}}

    cleaned_html = nh3.clean(
        html_string, tags=allowed_tags, attributes=allowed_attributes
    )
    return cleaned_html


# TODO: Some entries have entry content on the description block whereas others have on entry content. Try manage.
# TODO When the related fields are not found the entire script is crashing. Like for eg: with content block not available the script is failing. Build a fail safe mechenism
def get_entries_from_url(feed_url: str, num_entries: int = 3):
    """RSS information extraction using single url"""
    feed = feedparser.parse(feed_url)

    feed_title = feed.feed.title
    print("\n" + "*" * 30 + "New feed" + "*" * 30 + "\n")
    print(f"Feed Title: {feed_title}")

    for feed_entries in feed.entries[:num_entries]:
        print("\n" + "=" * 60)

        if not feed_entries:
            print("No entries found")
            continue

        entry_title = feed_entries.title
        entry_desc = feed_entries.description
        entry_link = feed_entries.link
        # entry_content = sanitize_html(feed_entries.content[0].value)

        print(f"Blog Title: {entry_title} \n")
        print(f"Blog Link: {entry_link} \n")
        print(f"Blog Description: {entry_desc} \n")
        # print(f"Blog content: {entry_content} \n")


def get_entries_from_opml(opml_file_path: str):
    """RSS information extraction using opml file"""
    opml_links = opml_parser(opml_file_path)
    for link in opml_links:
        get_entries_from_url(feed_url=link, num_entries=3)
    print("All entries shown successfully")


def main():
    get_entries_from_opml(
        "/Users/kaushalbundel/02-projects/python-projects/simple-rss/Subscriptions-OnMyMac.opml"
    )


if __name__ == "__main__":
    main()
