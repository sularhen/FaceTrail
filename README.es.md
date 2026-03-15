# FaceTrail

![FaceTrail banner](assets/banner.svg)

FaceTrail convierte una carpeta de imagenes o videos en un espacio de trabajo util para revisar rostros detectados, agrupar capturas similares y generar copias anonimizadas listas para compartir. Nacio a partir del proyecto original de seguimiento facial, pero ahora funciona como una herramienta CLI pensada para uso real en Windows y Linux.

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
