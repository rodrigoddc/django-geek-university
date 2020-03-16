import uuid
from django.db import models
from stdimage import StdImageField
from django.utils.translation import gettext_lazy as _


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Modified'), auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', _('Engine')),
        ('lni-stats-up', _('Chart')),
        ('lni-users', _('User')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Rocket')),
    )
    service = models.CharField(_('Service'), max_length=100)
    description = models.TextField(_('Description'), max_length=200)
    icon = models.CharField(_('Icon'), max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.service


class Feature(Base):
    ICON_CHOICES = (
        ('lni-cog', _('Engine')),
        ('lni-stats-up', _('Chart')),
        ('lni-users', _('User')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Rocket')),
    )
    name = models.CharField(_('Name'), max_length=30)
    description = models.TextField(_('Description'), max_length=65)
    icon = models.CharField(_('Icon'), max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.name


class Role(Base):
    role = models.CharField(_('Role'), max_length=100)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return self.role


class Employee(Base):
    name = models.CharField(_('Employee'), max_length=100)
    role = models.ForeignKey('core.Role', verbose_name=_('Role'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=65)
    image = StdImageField(_('Image'), upload_to=get_file_path,
                          variations={
                              'thumbs':
                                  {'width': 480, 'height': 480, 'crop': True}
                          })
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.name

