from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOERAN = "kr"
    LANGUAGE_CHOICES = (LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOERAN, "Korean")

    CURRENCY_USD = "usd"
    CURRENCY_USD = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_USD, "KRW"))
    # null=True만 넣어주면 Save할때 필수 입력하라고 나온다.
    # 사용자들이 사진이나 성별을 입력하지 않아도 다음으로 넘어가게 하려면 blank=True를 넣어주어야 한다.
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    langauge = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)