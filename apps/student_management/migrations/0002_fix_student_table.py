# Recreate student_management_student with correct columns (fixes old 0001 that only had id)

from django.db import migrations


def recreate_student_table(apps, schema_editor):
    """Drop old table and recreate with full schema from the model."""
    from django.db import connection

    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS student_management_student")

    # Get the historical Student model (as in 0001) and create the table
    Student = apps.get_model('student_management', 'Student')
    schema_editor.create_model(Student)


def reverse_recreate(apps, schema_editor):
    """Reverse: recreate minimal table (old broken schema)."""
    with schema_editor.connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS student_management_student")
        cursor.execute(
            "CREATE TABLE student_management_student (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT)"
        )


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(recreate_student_table, reverse_recreate),
    ]
