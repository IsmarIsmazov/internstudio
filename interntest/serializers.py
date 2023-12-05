from rest_framework import serializers

from interntest import models
from interntest.models import Comment, Product


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text')


class ProductSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'comment')

    def create(self, validated_data):
        comment_validated = validated_data.pop('comment')
        product = models.Product.objects.create(**validated_data)

        comment_models = [
            models.Comment(product=product, **comment)
            for comment in comment_validated
        ]
        models.Comment.objects.bulk_create(comment_models)

        return product