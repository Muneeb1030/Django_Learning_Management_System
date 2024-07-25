# Django Learning Management System

## Major Features
- Django Backend
    - Jazzmin used for admin panel customization.
    - Custom User Model Is created using AbstractUser from django.contrib.auth.models
        - It gives a implementation of authuser model which we have used to customize according to our requirements
    - ProfileUser Model is created to balance load on User Model
        - It will be automatically created for user when a neew entry in User table is created
            - Here Django Signals are used.
- React Frontend