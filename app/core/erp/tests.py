from app.wsgi import *
from core.erp.models import Type

# listar
# qyery = Type.objects.all()
# print(qyery)

# insercion
# t = Type()
# t.name = 'Algo'
# t.save()

# editar
# t = Type.objects.get(id=1)
# print(t.name)

# eliminar
# t = Type.objects.get(id=1)
# t.delete()

# obj = Type.objects.filter(name__contains='pru')
# obj = Type.objects.filter(name__icontains='pru')
obj = Type.objects.filter(name__endswith='a')
# obj = Type.objects.filter(name__)
print(obj)