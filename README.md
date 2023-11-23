# Paso1: Redirigete a la carpeta del proyecto

## Paso2: Cree el ambiente virtual
python -m venv myenv

## Paso 3: Activar el entorno virtual
myenv\Scripts\activate

## Paso 4: Instalar las librerias del archivo requirements
pip install -r requirements.txt

## Paso  5: Luego descargar el csv más reciente de la siguiente url
https://datosabiertos.mineduc.cl/titulados-en-educacion-superior/

## Paso6: Ejecutar la aplicación
python gel_excel_resumen_es.py
