from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings
import os
from random import randint

class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    @staticmethod
    def fetch_resources(uri, rel):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
        return path

    @staticmethod
    def link_callback(uri, rel):
        """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
        # use short variable names
        sUrl = settings.STATIC_URL      # Typically /static/
        sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL       # Typically /static/media/
        mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

    # def render_to_file(path: str, params: dict):
    #     template = get_template(path)
    #     html = template.render(params)
    #     file_name = "{0}-{1}.pdf".format(params['request'].user.first_name, randint(1, 1000000))
    #     file_path = os.path.join(os.path.abspath(os.path.dirname("__file__")), "store", file_name)
    #     with open(file_path, 'wb') as pdf:
    #         pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), pdf)
    #     return [file_name, file_path]
