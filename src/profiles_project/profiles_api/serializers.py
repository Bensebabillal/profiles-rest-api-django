from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length = 10)



class UserProfileSerializer(serializers.ModelSerializer):
    """a serializer for our user profile object"""

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={'password': {'write_only':True}}
    
    def create(self,validates_data):
        """create and return a new user."""

        user = models.UserProfile(
            email=validates_data['email'],
            name=validates_data['name']
        )

        user.set_password(validates_data['password'])
        user.save()

        return user




        