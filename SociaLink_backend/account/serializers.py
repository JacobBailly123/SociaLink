from rest_framework import serializers
from .models import User, FriendshipRequest


class UserSerializer(serializers.ModelSerializer):
    friends_count = serializers.SerializerMethodField()

    def get_friends_count(self, obj):
        return obj.friends.count()

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'friends_count', 'posts_count', 'get_avatar',)


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)
```

Save both files then push everything together:
```
git add .
git commit -m "Fix nav highlighting, DM ordering and friend count"
git push origin main