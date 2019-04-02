from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    return HttpResponse('<input type = "text" name = "emailOrNumber" class = "emailOrNumber" placeholder = "Моб. телефон или эл. адрес"><br>'
                    '<input type = "text" name = "name" placeholder= "Имя и фамилия">'
                    '<input type = "text" name = "surname" placeholder = "Имя пользователя"><br>'
                    '<input type = "password" name = "newPassword" class = "newPassword" placeholder = "Пароль"><br>'
                    '<button type="submit">Регистрация</button>')

