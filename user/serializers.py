from rest_framework import serializers
from user.models import Assignment, User




class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['is_active'] = True
        password = validated_data.pop('password')
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()

        return validated_data

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}, 
        }

class Assignmentserializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = "__all__"

