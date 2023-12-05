from rest_framework import serializers
from django.db import transaction

from interntest.models import Product, Comment
from interntest import models

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text')

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment text cannot be empty.")
        return value


class ProductSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, required=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'comment')

    def validate(self, data):
        comments_data = data.get('comment', [])
        if not comments_data:
            raise serializers.ValidationError("At least one comment is required.")
        return data

    def create(self, validated_data):
        comment_validated = validated_data.pop('comment')

        with transaction.atomic():
            product = models.Product.objects.create(**validated_data)

            comment_models = [
                models.Comment(product=product, **comment_data)
                for comment_data in comment_validated
            ]

            if not comment_models:
                raise serializers.ValidationError("At least one comment is required.")

            models.Comment.objects.bulk_create(comment_models)

        return product
