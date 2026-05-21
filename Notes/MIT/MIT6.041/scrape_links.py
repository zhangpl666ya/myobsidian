import urllib.request
import re

base = 'https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/resources/mit6_041f10_l01/'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(base, headers=headers)
try:
    response = urllib.request.urlopen(req, timeout=30)
    html = response.read().decode('utf-8')
    print('HTML length:', len(html))
    # Find PDF links
    pdf_links = re.findall(r'href="([^"]*\.pdf)"', html)
    print('PDF links:', pdf_links)
    # Find any links to files
    file_links = re.findall(r'href="([^"]*)"', html)
    for link in file_links:
        if any(x in link.lower() for x in ['pdf', 'slide', 'lec']):
            print('  File link:', link)
except Exception as e:
    print('Error:', type(e).__name__, e)