import random
import string
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["name", "phone", "email", "password", ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):

        name_parts = validated_data['name'].split()
        first_name = name_parts[0] if name_parts else ''

        # Generating username from first_name with a random 6-digit number
        random_number = ''.join(random.choices(string.digits, k=6))
        username = f"{first_name.lower()}{random_number}"

        user = User.objects.create_user(
            username=username,
            name=validated_data["name"],
            phone=validated_data["phone"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
