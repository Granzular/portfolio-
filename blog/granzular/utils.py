# The code in this file use of 
# python libaries that are seper# ate from django libaries

from urllib.request import urlopen
from .a import pretty_print_html

def inspect(url):
    res = urlopen(url).read()
    return pretty_print_html(res)

