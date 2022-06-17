# Generated by Django 4.0.5 on 2022-06-17 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetManager', '0006_asset_is_bidded'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='bidders',
            field=models.ManyToManyField(to='assetManager.nft'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='nft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nftHolder', to='assetManager.nft'),
        ),
    ]