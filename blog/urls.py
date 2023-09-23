from django.urls import path
from .views import (BookListApi, book_list_view,
                    BookDetailAPIView, BookDeleteAPIView, BookUpdateApiView,
                    BookCreateApiView, BookListCreateAPIView, BookUpdateDetailAPIView)

urlpatterns = [
    path('books_list_create/', BookListCreateAPIView.as_view()),
    path('books_update_detail/<int:pk>', BookUpdateDetailAPIView.as_view()),
    path('books/', BookListApi.as_view()),
    path('books/create', BookCreateApiView.as_view()),
    path('books/<int:pk>', BookDetailAPIView.as_view()),
    path('books/<int:pk>/edit', BookUpdateApiView.as_view()),
    path('books/<int:pk>/delete', BookDeleteAPIView.as_view()),
    path('kitoblar/', book_list_view),

]

# http://127.0.0.1:8000/api/v1/books/
# manashuga get so'rov jo'natadi kitoblar tro'yxat
# http://127.0.0.1:8000/api/v1/books/2/edit {'title', 'subtitle'}

# http://127.0.0.1:8000/api/v1/books/<id> id get jo'natadi
# bitta kitobni olasan