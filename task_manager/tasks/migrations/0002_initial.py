# Generated by Django 5.0.7 on 2024-09-01 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("labels", "0001_initial"),
        ("statuses", "0001_initial"),
        ("tasks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_tasks",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="executing_tasks",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Executor",
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tasks",
                to="statuses.taskstatus",
                verbose_name="Status",
            ),
        ),
        migrations.AddField(
            model_name="tasklabelrelation",
            name="label",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="labels.tasklabel",
            ),
        ),
        migrations.AddField(
            model_name="tasklabelrelation",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.task"
            ),
        ),
        migrations.AddField(
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
