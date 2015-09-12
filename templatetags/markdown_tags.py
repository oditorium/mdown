"""defines markdown-related tags to use in Django templates

Using the module
----------------------
{% load markdown_tags %}


The `markdownf` filter
----------------------

{{ a_variable_containing_markdown | markdownf }}



The `markdown` block tag
------------------------

{% markdown %}

<markdown text here>

{% endmarkdown %}
"""

__version__ = "1.0.0"
__version_dt__ = "2015-09-12"


from django import template
register = template.Library()
from django.utils.safestring import mark_safe
# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

import markdown

@register.filter(name="markdownf", is_safe=True)
def markdownf(value, autoescape=True):
    """Converts the string from markdown"""
    return markdown.markdown(value)

@register.tag(name="markdown")
def do_markdown(parser, token):
    nodelist = parser.parse(('endmarkdown',))
    parser.delete_first_token()
    return MarkdownNode(nodelist)

class MarkdownNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
    def render(self, context):
        output = self.nodelist.render(context)
        return (markdown.markdown(output))