from html.parser import HTMLParser
from html import unescape
from io import StringIO

class HTMLFormatter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.indent_level = 0
        self.output = StringIO()

    def handle_starttag(self, tag, attrs):
        self.output.write(' ' * self.indent_level)
        self.output.write('<' + tag + '>\n')
        self.indent_level += 2

    def handle_endtag(self, tag):
        self.indent_level -= 2
        self.output.write(' ' * self.indent_level)
        self.output.write('</' + tag + '>\n')

    def handle_data(self, data):
        self.output.write(' ' * self.indent_level)
        self.output.write(unescape(data) + '\n')

def pretty_print_html(html_bytes):
    parser = HTMLFormatter()
    parser.feed(html_bytes.decode('utf-8'))
    return parser.output.getvalue()
