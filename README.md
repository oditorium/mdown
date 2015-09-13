# Markdown Tags

_A Django app to render Markdown within templates_


## Description

Django did have a contributed module for Markdown support a long
time ago, but that got dropped along the line for reasons that are 
not entirely clear to me (my understanding is that there were security
concerns). For me personally Markdown is crucial when writing any
kind of text that is having more than one paragraph because handcoding
html tags for paragraphs, links or emphasis is just painful.

Fortunately markdown support in Django can be easily created using 
template tags. This app provides two of those: a _block tag_ that treats 
the text between them as markdown, and a _filter_ that converts markdown 
from a variable to html. 

It is a very light-weight solution - ultimately all that really matters 
in the implementation at the 20-odd lines in the `markdown_tags.py` file 
that actually implement markdown support.


## Installation

Make sure you have markdown installed, otherwise install it with

    pip  install markdown
    pip3 install markdown

Then just copy this app into your Django project, and register it
in the installed apps in `settings.py`.

	INSTALLED_APPS += ('mdown')


## Usage

Initialising the module in the template file:

	{% load markdown_tags %}

Using the `markdownf` filter:

	{{ a_variable_containing_markdown | safe | markdownf }}


Using the `markdown` block tag:

	{% markdown %}

	<markdown text here>

	{% endmarkdown %}

You can also find a working installation in the app's `views.py` 
and associated template files.

## ChangeLog

- **v1.0** defines the `markdownf` filter, and the `markdown` block tag

## Copyright

Copyright (c) 2015 Stefan Loesch / oditorium. See LICENSE for details.
