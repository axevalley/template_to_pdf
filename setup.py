#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='template_to_pdf',
    version='1.1',
    description='Converts jinja2 templates to HTML and PDF',
    author='Luke Shiner',
    author_email='luke@lukeshiner.com',
    url='http://www.lukeshiner.com',
    keywords=['template', 'html', 'pdf'],
    install_requires=['jinja2', 'pdfkit'],
    packages=find_packages(),
    )
