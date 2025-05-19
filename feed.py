import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('podcast', {'version':'2.0'})

channel_element = xml_tree.SubElement(rss_element, 'channel')

link_prefix = yaml_data['link']

xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'link').text = yaml_data['link']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'lastBuildDate').text = yaml_data['lastBuildDate']
xml_tree.SubElement(channel_element, 'managingEditor').text = yaml_data['managingEditor']

for item in yaml_data['items']:
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item['title']
    xml_tree.SubElement(item_element, 'link').text = item['link']
    xml_tree.SubElement(item_element, 'description').text = item['description']
    xml_tree.SubElement(item_element, 'pubDate').text = item['pubDate']
    xml_tree.SubElement(item_element, 'author').text = item['author']

    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['guid'],
        'type': 'audio/mpeg',
        'length': item['author']
    })

output_tree = xml_tree.ElementTree(rss_element)
print("✅ Writing to podcast.xml")
output_tree.write("podcast.xml", encoding="utf-8", xml_declaration=True)
print("✅ Done writing")
