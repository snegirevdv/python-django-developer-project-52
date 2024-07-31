# Generated by Django 5.0.7 on 2024-07-31 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0003_alter_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True,
                related_name="tasks",
                through="tasks.TaskLabelRelation",
                to="labels.tasklabel",
                verbose_name="Labels",
            ),
        ),
    ]