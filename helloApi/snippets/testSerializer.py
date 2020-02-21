from datetime import datetime

class Comment(object):
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    emailAddress = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    def validate_content(self, value):
        if 'test' in value:
            raise serializers.ValidationError("Content contains Test")
        return value
    def validate(self, data):
        """
        Check that start is before finish.
        """
        if 'test1' in data['content']:
            raise serializers.ValidationError("finish must occur after start")
        return data

serializer = CommentSerializer(data={'emailAddress':'steve@gmail.com', 'content': 'test1','created':'2020-01-01T11:20:20'})        
   
'''
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
'''                

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
# b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
serializer = CommentSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}
