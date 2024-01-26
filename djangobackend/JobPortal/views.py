from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from JobPortal.serializers import JobsSerializer
from JobPortal.models import jobs

@csrf_exempt
def jobsApi(request,id=0):
    if request.method=='GET':
        job = jobs.objects.all()
        jobs_serializer=JobsSerializer(job,many=True)
        return JsonResponse(jobs_serializer.data,safe=False)
    
    


