# Generated by Django 4.0.5 on 2022-06-19 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0016_alter_user_email'),
        ('accounts', '0002_remove_user_role_remove_user_groups_user_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Staff'), (2, 'Trainee'), (3, 'Public')], null=True),
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
    ]