from jinja2 import Template
import pdfkit


def save_pdf(html, output_path):
    pdfkit.from_string(html, output_path)


def get_html(template_name, variables):
    template_path = template_name
    with open(template_path, 'r') as template_file:
        template = Template(template_file.read())
    html = template.render(variables)
    return html


def save_pdf_from_tamplate(template_name, variables, output_path):
    html = get_html(template_name, variables)
    save_pdf(html, output_path)
