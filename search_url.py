import re


def get_url_from_txt():
    urls_text = open('urls.txt').read()
    r = re.compile(r"(http://[^ ]+)")
    urls = r.sub(r'<a href="\1">\1</a>', urls_text).split('\n')
    for url in urls:
        return url
