from rest_framework import serializers
from rest_framework.reverse import reverse

from secureaccess.models import Element


class NewElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('file', 'url', 'shareable_link', 'password')
        read_only_fields = ('shareable_link', 'password')

    def validate(self, data):
        file = data.get('file')
        url = data.get('url')
        if file and url:
            raise serializers.ValidationError('Two parameters given, only one allowed - file or url.')
        if not file and not url:
            raise serializers.ValidationError('Missing parameters - file or url.')
        return data

    def create(self, validated_data):
        self.raw_password = Element.get_random_password()
        validated_data['password'] = Element.make_password(self.raw_password)
        return super().create(validated_data)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['password'] = self.raw_password
        ret['shareable_link'] = reverse('get_element', args=[ret['shareable_link']], request=self.context['request'])
        return ret


class GetElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('file', 'url', 'password')
        extra_kwargs = {'password': {'write_only': True}}
