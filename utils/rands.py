import string
from random import SystemRandom
from django.utils.text import slugify

def slugify_new(group, size):
    group +='-'+''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k = size
        ))
    return slugify(group)