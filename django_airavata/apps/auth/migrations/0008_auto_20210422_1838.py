# Generated by Django 2.2.17 on 2021-04-22 18:38

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from django_airavata.apps.auth.models import VERIFY_EMAIL_CHANGE_TEMPLATE


def default_templates(apps, schema_editor):
    EmailTemplate = apps.get_model("django_airavata_auth", "EmailTemplate")
    verify_email_template = EmailTemplate(
        template_type=VERIFY_EMAIL_CHANGE_TEMPLATE,
        subject="{{first_name}} {{last_name}} ({{username}}), "
                "Please Verify Your New Email Address in {{portal_title}}",
        body="""
        <p>
        Dear {{first_name}} {{last_name}},
        </p>

        <p>
        Before your email address change can be processed, you need to verify
        your new email address ({{email}}). Click the link below to verify your email
        address:
        </p>

        <p><a href="{{url}}">{{url}}</a></p>
        """.strip())
    verify_email_template.save()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_airavata_auth', '0007_auto_20200917_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='template_type',
            field=models.IntegerField(choices=[(1, 'Verify Email Template'), (2, 'New User Email Template'), (3, 'Password Reset Email Template'), (4, 'User Added to Group Template'), (5, 'Verify Email Change Template')], primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='PendingEmailChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('verification_code', models.CharField(default=uuid.uuid4, max_length=36, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(default_templates, migrations.RunPython.noop),
    ]