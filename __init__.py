"""a Django app defining markdown processing filters and tags for templates


USAGE
------------

Include this app into your installed apps. Then you can use 
code like the one below in your templates

    {% load markdown_tags %}

    AN EXAMPLE FOR THE USE OF THE MARKDOWNF FILTER<br/>

    {{ a_safe_variable_containing_markdown | safe | markdownf }}

    <hr/>

    AN EXAMPLE FOR THE USE OF THE MARKDOWN BLOCKTAG<br/>
    {% markdown %}

    <markdown text here>

    {% endmarkdown %}


See `views.py` and the templates included in the package for more examples.

Note: this package contains some more example code for how to deal with
markdown (and other textprocessors for this matter):

- `views.whole_page_as_markdown` is an example where an entire template 
is rendered as markdown (this is probably not that useful in practice,
as usually there whould be some wrapper around it)

- `page_including_markdown` is an example for a double tempate page, where
the _master_ page is a regular template which pulls html that is has 
converted from markdown generated by a second template (arguably one might
simply use the `markdownf` filter for that



REQUIREMENTS
------------

This packages uses the `markdown` processor for markdown. It can be installed using

    pip install markdown

"""

__version__ = "1.0b1"

__version_dt__ = "2015-09-12"
__copyright__="Copyright (c) oditorium 2015. All rights reserved."
__license__="MIT License"

    
    