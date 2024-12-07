import requests
from bs4 import BeautifulSoup
import os
import csv
import json
import time

# Función para realizar el scraping
def scrape_mercado_libre(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept-Language": "es-ES, en;q=0.5",
    }

    try:
        # Pausa para evitar bloqueos del servidor
        time.sleep(8)
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        productos = soup.find_all('h2', class_='poly-box poly-component__title')

        data_list = []
        for producto in productos:
            # Extraer título
            titulo = producto.find('a').text.strip() if producto.find('a') else "Título no encontrado"

            # Extraer precio
            precio = producto.find_next('span', class_='andes-money-amount__fraction').text.strip() if producto.find_next('span', class_='andes-money-amount__fraction') else "Precio no encontrado"

            data_list.append({"Título": titulo, "Precio": precio})

        return data_list

    except Exception as e:
        print(f"Error durante el scraping: {e}")
        return []

# Ejecución principal
if __name__ == "__main__":
    url = "https://listado.mercadolibre.com.co/tenis-nike-hombre"
    productos = scrape_mercado_libre(url)

    if productos:
        # Crear directorio de salida si no existe
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)

        # Guardar datos en archivo CSV
        csv_path = os.path.join(output_dir, 'productos.csv')
        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["Título", "Precio"])
            writer.writeheader()
            writer.writerows(productos)

        # Guardar datos en archivo JSON
        json_path = os.path.join(output_dir, 'productos.json')
        with open(json_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(productos, jsonfile, ensure_ascii=False, indent=4)

        print(f"Datos guardados en:\n- {csv_path}\n- {json_path}")
    else:
        print("No se encontraron productos.")
