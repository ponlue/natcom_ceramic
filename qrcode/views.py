from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pyqrcode

def index(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get('url')
        qr = pyqrcode.create(url)

        # Create a BytesIO buffer to store the PNG image
        buffer = BytesIO()
        qr.png(buffer, scale=6)
        # module_color=(0, 0, 0, 128), background=(0xff, 0xff, 0xcc)

        # Move the buffer cursor to the beginning
        buffer.seek(0)

        # Create an HTTP response with the PNG image
        response = HttpResponse(content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="ceramic-qrcode.png"'
        response.write(buffer.read())
        
        if HttpResponse.status_code == 200:
            return response
    return render(request, 'qrcode/qrcode.html', context=context)
