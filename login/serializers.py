from rest_framework import serializers
from .models import Sign_Up_Data

class Sign_Up_DataSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sign_Up_Data
		# fields = ('ticker', 'volume')
		fields = '__all__'