import pytest
from main import scrape_mercado_libre

def test_scrape_mercado_libre():
    url = "https://httpbin.org/html"  # URL de prueba
    resultados = scrape_mercado_libre(url)
    assert "Título no encontrado" in resultados or "Precio no encontrado" in resultados
