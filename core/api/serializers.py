from rest_framework import serializers

class QueryGeneratorSerializer(serializers.Serializer):
    schema = serializers.CharField()
    language = serializers.CharField()
    prompt = serializers.CharField()
    code = serializers.CharField(required=False)
    
    
class CodeGeneratorSerializer(serializers.Serializer):
    language = serializers.CharField()
    prompt = serializers.CharField()
    code = serializers.CharField(required=False)
    
