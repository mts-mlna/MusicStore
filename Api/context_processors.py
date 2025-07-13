# productos/context_processors.py
from .models import *

def low_stock_count(request):
    """
    Devuelve la cantidad de productos con Stock < 5
    para que esté disponible como {{ low_stock_count }}
    en todos los templates.
    """
    return {
        'low_stock_count': Producto.objects.filter(Stock__lt=5).count()
    }
