from urllib.parse import urlparse, parse_qs
url = input()
parsed_url = urlparse(url)
pq = parse_qs(parsed_url.query)
print(pq[input()])


