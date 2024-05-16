# backend/views.py
from rest_framework import generics, serializers
from .models import Recipe, Message
from .serializers import RecipeSerializer, MessageSerializer

class ListRecipesView(generics.ListAPIView):
    queryset = Recipe.objects.filter(status='approved')
    serializer_class = RecipeSerializer

class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.filter(status='approved')
    serializer_class = RecipeSerializer

class UploadRecipeView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        # Check if the chef_username is unique
        username = serializer.validated_data['chef_username']
        if Recipe.objects.filter(chef_username=username).exists():
            raise serializers.ValidationError({'chef_username': 'This username is already taken.'})
        serializer.save()

class SendMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ListMessagesView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        sender = self.request.query_params.get('sender')
        receiver = self.request.query_params.get('receiver')
        return Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
