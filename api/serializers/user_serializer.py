from rest_framework import fields, serializers
from event.models import User
from rest_framework.authtoken.models import Token



# class UserListingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User Profile serializer
    """
    email = serializers.EmailField()
    token = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(read_only=True, required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name','token', 'password', 'confirm_password']
    
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
    password = serializers.CharField(write_only=True, required=False)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id','username','password','token']

    def get_token(self, obj):
        return f"Token {Token.objects.get_or_create(user=obj)[0]}"