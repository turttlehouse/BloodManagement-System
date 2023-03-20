from django.urls import path,include
from .import views

'''urlpatterns = [
    path('',views.home,name='home'),
    path('A/',views.A),
    path('B/',views.B),
    path('AB/',views.AB),
    path('O/',views.O),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update)
    
]
'''

urlpatterns = [
    path('',views.loginuser,name='login'),
    path('logoutuser/',views.logoutuser),
    path('home/',views.home),
    path('choose/<str:dog>',views.choose),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update),
    path('check/',views.check),
    path('search/',views.search,name="searchbar"),
    path('signupuser/',views.signupuser)
]
