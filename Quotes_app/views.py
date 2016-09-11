from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


from django.http import HttpResponse

def landing(request):
    return render(request, "Quotes_app/landing-page.html", {})

#List Daily Quote or update it
# dailyquote/
class DailyQuoteList(APIView):
	
	def get(self, request):
		dailyquote = Daily_Quote.objects.all()
		serializer = Daily_QuoteSerializer(dailyquote, many=True)
		return Response(serializer.data)

		
		