from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

User = get_user_model()
        

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'password_confirm')
        write_only_field = ['password']

    def validate(self, attrs: dict):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Пароли не совпадают!')
        return attrs
    
    def create(self, validated_data: dict):
        user = User.objects.create_user(**validated_data)
        return user
    
    
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate_phone_number(self, phone_number):
        if not User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Неверно указан номер')
        return phone_number
    
    def validate(self, attrs):
        request = self.context.get('request')
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        if phone_number and password:
            user = authenticate(phone_number=phone_number,
                                password=password,
                                request=request)
            if not user:
                raise serializers.ValidationError(
                    'Неправильно указан номер или пароль'
                    )
        else:
            raise serializers.ValidationError(
                'Номер и пароль обязательны к заполнению'
                )
        attrs['user'] = user
        return attrs
