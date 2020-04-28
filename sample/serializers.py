from django.contrib.auth.models import User
from rest_framework import serializers

from sample.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Document
        fields = ('id', 'url', 'owner', 'created_time', 'type', 
        	'source_type', 'source_id', 'input_meta_data',)


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 
        	'email', 'date_joined')
