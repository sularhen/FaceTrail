# FaceTrail

![FaceTrail banner](assets/banner.svg)

FaceTrail es una CLI multiplataforma para extraer rostros, agrupar apariciones similares, generar reportes visuales y exportar copias anonimizadas. Convierte una carpeta de imagenes o videos en un espacio de trabajo realmente util, y nace de la idea original de `PythonFaceTracker` pero rehecha para quedar mas limpia, portable y compartible.

## Que hace

- Escanea imagenes individuales, carpetas completas o videos.
- Detecta rostros con OpenCV sin pedir rutas manuales de cascadas.
- Extrae recortes automaticamente y agrupa apariciones parecidas.
- Calcula la mejor captura de cada grupo segun nitidez.
- Genera un reporte HTML, un `summary.json` y un `detections.csv`.
- Puede exportar copias anonimizadas con desenfoque facial.

## Instalacion

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

## Paquetes de Release

El repositorio ahora incluye un generador de paquetes que deja siempre:

- `dist/facetrail-windows-vX.Y.Z.zip`
- `dist/facetrail-linux-vX.Y.Z.tar.gz`

Se genera con:

```bash
python scripts/build_release.py
```

## Uso rapido

```bash
facetrail scan ./media --output ./output --save-redacted
```

Opciones utiles:

- `--sample-every 10`: procesa uno de cada 10 frames en videos.
- `--min-face-size 96`: ignora rostros muy pequenos.
- `--cluster-threshold 0.95`: crea grupos mas estrictos.

## Salidas

- `output/faces/`: recortes de rostros detectados.
- `output/redacted/`: imagenes o videos con rostros desenfocados.
- `output/report/gallery.html`: galeria visual.
- `output/report/summary.json`: resumen estructurado.
- `output/report/detections.csv`: manifest de detecciones.

## Idea del producto

FaceTrail sirve para:

- Curar material audiovisual antes de compartirlo.
- Revisar bibliotecas de fotos con personas repetidas.
- Preparar datasets pequenos o auditorias visuales.
- Crear una pasada rapida de privacidad sobre videos locales.

## Limitaciones

- El agrupamiento usa descriptores ligeros de apariencia y no pretende ser biometria.
- El detector esta optimizado para practicidad, no para vigilancia ni identificacion.

## Credito

Este repositorio parte de `PythonFaceTracker`, pero fue reconstruido como una utilidad mas utilizable, portable y documentada.
