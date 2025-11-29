from django import template
from blog.utils import get_tech_logos
import markdown

register = template.Library()

@register.filter
def logo(keyword):
    keyword = keyword.lower().strip()
    md = get_tech_logos().get(keyword,f"![](https://img.icons8.com/color/96/{keyword}.png)")
    return markdown.markdown(md,extensions=['fenced_code', 'codehilite', 'toc', 'tables'])
