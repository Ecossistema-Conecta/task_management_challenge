from django.db import models, migrations



def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    
    Project = apps.get_model('project', 'Project')
    Task = apps.get_model('project', 'Task')
    Staff = apps.get_model('staff', 'Staff')

    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    content_type_project = ContentType.objects.get_for_model(Project)
    content_type_task = ContentType.objects.get_for_model(Task)
    content_type_staff = ContentType.objects.get_for_model(Staff)

    admin = Group.objects.create(name=u'admin')
    manager = Group.objects.create(name=u'manager')
    staff = Group.objects.create(name=u'staff')

    admin.permissions.add(*Permission.objects.filter(content_type=content_type_project))
    admin.permissions.add(*Permission.objects.filter(content_type=content_type_task))
    admin.permissions.add(*Permission.objects.filter(content_type=content_type_staff))

    manager.permissions.add(*Permission.objects.filter(content_type=content_type_project))
    manager.permissions.add(*Permission.objects.filter(content_type=content_type_task))

    staff.permissions.add(*Permission.objects.filter(content_type=content_type_project, codename__in=['view_project']))
    staff.permissions.add(*Permission.objects.filter(content_type=content_type_task, codename__in=['view_task']))


def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['admin', 'manager', 'staff']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]
