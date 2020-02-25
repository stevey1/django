from unittest import TestCase
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User, Group

class test_snippetSerializer(TestCase):
    def setUp(self):
        pass
    def test_it_should_serialize(self):
        user = User(username="test_serializer")
        snippet = Snippet(title='title123',owner = user)
        serializer = SnippetSerializer(snippet, context={
            'request': None,
        })
        self.assertTrue(serializer.data["title"]=='title123') 
        
    def test_it_should_deSerialize(self):
        serializer = SnippetSerializer(data={'title': 'test-de','code': 'test-decode'})
        self.assertTrue(serializer.is_valid()) 
        print(serializer.validated_data)
        self.assertTrue(serializer.validated_data['title']=='test-de') 

    def test_deserialize_should_not_be_deserialized(self):
        serializer = SnippetSerializer(data={'title': 'django restapi test-de'})
        self.assertFalse(serializer.is_valid()) 
        self.assertIsNotNone(serializer.errors['code']) 
        #print(serializer.errors)
        #for error in serializer.errors.items():
            #print(error)

