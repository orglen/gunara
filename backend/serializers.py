# 在 serializers.py 文件中

from rest_framework import serializers
from .models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        # fields = '__all__'  # 或者你可以明确列出你想要的字段
        exclude = ['id','messages']  # 排除 'messages' 字段

class ConversationTitle(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['title', 'create_time', 'update_time', 'id']

    def get_id(self, obj):
        return obj.conversation_id
    

class Conversations(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    class Meta:
        model = Conversation
        fields = ['title', 'create_time', 'update_time', 'id']
        
    def get_id(self, obj):
        return obj.conversation_id

