import pytest
from main import scrape_mercado_libre

def test_scrape_mercado_libre():
    # URL de prueba
    url = "https://httpbin.org/html"
    productos = scrape_mercado_libre(url)
    assert isinstance(productos, list), "La salida debe ser una lista"
    assert len(productos) >= 0, "Debe retornar una lista vacía o con datos"
