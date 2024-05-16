from django.urls import path
from .views import ListRecipesView, RecipeDetailView, UploadRecipeView, SendMessageView, ListMessagesView

urlpatterns = [
    path('recipes/', ListRecipesView.as_view(), name='list-recipes'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/upload/', UploadRecipeView.as_view(), name='upload-recipe'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
    path('messages/', ListMessagesView.as_view(), name='list-messages'),
]
