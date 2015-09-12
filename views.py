from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404

from django.utils.safestring import mark_safe

import markdown


def example(request):
    """ renders the example page, containing both markdown filter and blocktag
    """
    
    # render the markdown template and convert it to html
    template = loader.get_template('mdown/example.md')
    context_md = RequestContext(request, {
        'name': "Stefan"
    })
    rendered_markdown = template.render(context_md)
    
    # render the actual template
    template = loader.get_template('mdown/example.html')
    context = RequestContext(request, {
        'rendered_markdown': rendered_markdown,
    }) 
    return HttpResponse(template.render(context))

def whole_page_is_markdown(request):
    """renders and entire page as markdown
    """
    template = loader.get_template('mdown/whole_page_is_markdown.md')
    context = RequestContext(request, {
        'name': "Stefan", 
    })
    rendered_template = template.render(context)
    html = markdown.markdown(rendered_template)
    return HttpResponse(html)
    
def page_including_markdown(request):
    """renders a page that is including markdown from a second template
    """
    
    # render the markdown template and convert it to html
    template = loader.get_template('mdown/page_including_markdown.md')
    context_md = RequestContext(request, {
    })
    rendered_template = template.render(context_md)
    html = mark_safe(markdown.markdown(rendered_template))
    
    # render the actual template
    template = loader.get_template('mdown/page_including_markdown.html')
    context_html = RequestContext(request, {
        'body': html,
    }) 
    
    return HttpResponse(template.render(context_html))