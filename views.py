from django.shortcuts import  get_object_or_404, render_to_response
from convertPixelArt.forms import UploadFileForm
from convertPixelArt.models import Threads
from django.core.context_processors import csrf
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import imageConverter.conversionFunctions as iC

def index(request):
    c = {}
    c.update(csrf(request))

    return render_to_response('convertPixelArt/index.html', c)

def changePicture(request):
    data = request.FILES['imageFile'] # or self.files['image'] in your form
    path = default_storage.save('tmp\%s' %data.name, ContentFile(data.read()))
    tmp_file = os.path.join(settings.MEDIA_ROOT, path)
    filename =  data.name
    convertedImage, listOfColors, listOfSymbols, rgbCodes = iC.convertImage(tmp_file)
    combinedList = zip(rgbCodes, listOfSymbols)
    b = {}
    b["myrequest"] = 'uploads/converted/' + convertedImage
    b["myrequestListOfColorsAndSymbols"] = combinedList
    b["Symbols"] = listOfSymbols
    b["names"] = listOfColors
    template_name = '/convertPixelArt/convertImages.html'
    
    return render_to_response('convertPixelArt/convertImages.html', b)