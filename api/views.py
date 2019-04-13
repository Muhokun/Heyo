from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from .facedetection_lib.myscript import detect_emotion_func

def get_response(status=200, data=None, error_message=None):
    return {
        'status': status,
        'data': data,
        'error_message': error_message
    }

@csrf_exempt
def emotion_detector(request):

    image = request.FILES.get('image')

    if not image:
        return JsonResponse(get_response(status=404, error_message='You have to send real image'))

    # img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/sad_face.jpg'
    # print(img_path)
    emotion = "sad"

    return JsonResponse(get_response(data=emotion))
