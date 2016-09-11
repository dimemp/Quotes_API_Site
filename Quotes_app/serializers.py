from rest_framework import serializers
from .models import * 

class Daily_QuoteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Daily_Quote
		fields = '__all__'
		
			
	
		