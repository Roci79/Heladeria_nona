# Generated by Django 5.0.3 on 2024-04-08 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helados', '0003_pedido_numero_bolas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='detallepedido',
            name='sabor',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
        migrations.DeleteModel(
            name='DetallePedido',
        ),
    ]
