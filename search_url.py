import re


def get_url_from_txt(text):
    r = re.compile(r"(http://[^ ]+)")
    urls = r.sub(r'<a href="\1">\1</a>', text).split('\n')
    for url in urls:
        return url
