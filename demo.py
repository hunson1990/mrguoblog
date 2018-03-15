from urllib.parse import urljoin

base_url = "http://www.pythonclub.org"

relative_url = "../python-basic/datetime"

abs_url = urljoin(base_url, relative_url)

#print(abs_url)

a=b"\xE5\x9c\xA8"

c=a.decode('utf-8')

#print(c)

