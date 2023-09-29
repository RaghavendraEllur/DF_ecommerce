# Generated by Django 4.2.4 on 2023-09-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_composition_product_benefits_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Benefits',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('AL', 'Almonds'), ('PI', 'Pistachios'), ('CA', 'Cashew'), ('AP', 'Apricot'), ('DA', 'Dates'), ('HA', 'Hazelnuts'), ('PN', 'Peanut'), ('BN', 'Betel-Nut'), ('DC', 'Dry-Coconut'), ('WL', 'Walnuts'), ('RA', 'Raisins'), ('SE', 'Seeds'), ('PR', 'Prunes'), ('DF', 'Dry-Figs'), ('FN', 'Fox-Nuts'), ('DB', 'Dry-Berries'), ('PE', 'Pecans'), ('CN', 'Corn-Nuts')], max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='benefits',
            field=models.TextField(default=''),
        ),
    ]