# Generated by Django 2.2.19 on 2022-12-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_ingredientrecipe_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_favorited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_in_shopping_cart',
            field=models.BooleanField(default=False),
        ),
    ]
