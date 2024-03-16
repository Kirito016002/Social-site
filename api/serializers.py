from rest_framework.serializers import ModelSerializer

from main import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'last_login']
        

class UserRealtionSerializer(ModelSerializer):
    class Meta:
        model = models.UserReletion
        fields = '__all__'


class FollowingSerializer(ModelSerializer):
    class Meta:
        model = models.UserReletion
        fields = ['from_user',]
        depth=1


class FollowerSerializer(ModelSerializer):
    class Meta:
        model = models.UserReletion
        fields = ['to_user',]
        depth=1
        

class ChatSerializer(ModelSerializer):
    class Meta:
        model = models.Chat
        fields = ['id', 'username']
        
        
class MassageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'

class ChatListSerializer(ModelSerializer):
    last_message = MassageSerializer(read_only=True)
    class Meta:
        model = models.Chat
        fields = ['id', 'last_message', 'unread_messages', 'users']
        
        
class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'date']

    def create(self, validated_data):
        user = self.context['request'].user
        return models.Post.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    
    
class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
        

class LikeSerializer(ModelSerializer):
    class Meta:
        model = models.Like
        fields = '__all__'