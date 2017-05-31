import sys
import csv
import requests
import xml.etree.ElementTree as ET

# read the WXR input file (just an RSS XML file) from STDIN
wxr = sys.stdin.read()
wxrRoot = ET.fromstring(wxr)
namespaces = {
	'wp': 'http://wordpress.org/export/1.2/'
}

# prep the CSV output
output = csv.writer(sys.stdout)

# parse through each item in the RSS file
channel = wxrRoot.find('channel')
for item in channel.findall('item'):

	# skip anything that's not a media post type
	postTypeTag = item.find('wp:post_type', namespaces)
	if postTypeTag.text != 'attachment':
		continue

	# gather all the necessary data from the XML file
	id = item.find('wp:post_id', namespaces).text
	title = item.find('title').text
	url = item.find('wp:attachment_url', namespaces).text

	# get the file size from the server
	response = requests.head(url)
	filesize = 0
	if response.status_code == requests.codes.ok:
		filesize = response.headers['Content-Length']

	# print the data in CSV format
	output.writerow([id, title, url, filesize])