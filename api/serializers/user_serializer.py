from rest_framework import fields, serializers
from event.models import User
from rest_framework.authtoken.models import Token



class UserListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password',"is_staff","is_superuser","is_active","groups", "user_permissions"]


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Profile serializer
    """
    email = serializers.EmailField()
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    # confirm_password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name','token', 'password']
    
        extra_kwargs = {"password":
                                {"write_only": True}
                            }

    def create(self, validated_data):
        """
        custom 'create' so that password gets hashed!
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

        
    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"


class UserLoginSerializer(serializers.ModelSerializer):
    """
    User Profile serializer
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id','username','password','token']

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"