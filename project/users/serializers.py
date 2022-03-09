from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):

    start_date = serializers.ReadOnlyField()

    class Meta:
        model = Users
        fields = ('email', 'user_name', 'password', 'start_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
