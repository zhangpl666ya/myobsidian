import urllib.request
import re
import os

base_url = 'https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010'

# Resource pages for lectures 1-4
resource_pages = [
    '/resources/mit6_041f10_l01/',
    '/resources/mit6_041f10_l02/',
    '/resources/mit6_041f10_l03/',
    '/resources/mit6_041f10_l04/',
]

headers = {'User-Agent': 'Mozilla/5.0'}
out_dir = r'C:\Users\39173\Desktop\笔记\myobsidan\Notes\MIT\MIT6.041'

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirect())

for i, page in enumerate(resource_pages, 1):
    url = base_url + page
    print(f'Lecture {i}: Fetching {url}')
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req, timeout=30)
        html = response.read().decode('utf-8')
        pdf_links = re.findall(r'href="([^"]*\.pdf)"', html)
        if pdf_links:
            pdf_url = 'https://ocw.mit.edu' + pdf_links[0]
            print(f'  PDF URL: {pdf_url}')
            req2 = urllib.request.Request(pdf_url, headers=headers)
            try:
                resp2 = opener.open(req2, timeout=15)
                ct = resp2.headers.get('Content-Type')
                data = resp2.read()
                out_path = os.path.join(out_dir, f'lecture{i:02d}.pdf')
                with open(out_path, 'wb') as f:
                    f.write(data)
                print(f'  Saved {len(data)} bytes to lecture{i:02d}.pdf')
            except Exception as e:
                print(f'  PDF download error: {e}')
        else:
            print(f'  No PDF links found')
    except Exception as e:
        print(f'  Page fetch error: {e}')

print('Done!')