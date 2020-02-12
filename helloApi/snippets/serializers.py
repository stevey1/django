from django.contrib.auth.models import User, Group
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())   
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','snippets']


class GroupSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer = ModelSerializer ?
    class Meta:
        model = Group
        fields = ['url', 'name']
#modal and fields        
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   
             
'''
# SnippetSerializer(model object/python object), #.data, is_valid(), .validated_data .save()
# serialize: SnippetSerializer(model)->JSONRenderer().render(serializer.data)
# deserialize: JasonString b string->into stream->JSONParser().parse(stream) 4.SnippetSerializer(data=data), is_valid(), .validated_data .save()
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance       
        '''