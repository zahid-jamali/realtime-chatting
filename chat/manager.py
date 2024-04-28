from django.contrib.auth.base_user import BaseUserManager
# from .models import CustomUser



class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None):
        if name is None:
            raise ValueError("Name not inserted")

        if email is None:
            raise ValueError("Email Not Found!")

        if phone is None:
            raise ValueError("Phone number not inserted!")

        user=self.model(
            name=name,
            email=self.normalize_email(email),
            phone=phone,
        )

        user.password=set_password(password)
        user.save(self._db)
        return user 

    def create_superuser(self, name, email, phone, password=None):
        user=self.model(
            name=name,
            email=email, 
            phone=phone,
        )
        user.set_password(password)
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user