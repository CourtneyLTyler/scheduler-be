# Generated by Django 2.1.7 on 2019-03-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20190314_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulebyshift',
            name='section_blue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blue', to='scheduler.Employee'),
        ),
        migrations.AlterField(
            model_name='schedulebyshift',
            name='section_green',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='green', to='scheduler.Employee'),
        ),
        migrations.AlterField(
            model_name='schedulebyshift',
            name='section_orange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orange', to='scheduler.Employee'),
        ),
        migrations.AlterField(
            model_name='schedulebyshift',
            name='section_purple',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purple', to='scheduler.Employee'),
        ),
        migrations.AlterField(
            model_name='schedulebyshift',
            name='section_yellow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yellow', to='scheduler.Employee'),
        ),
    ]