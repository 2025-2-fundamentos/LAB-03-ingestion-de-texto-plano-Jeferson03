"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = lines[4:]

    pattern = re.compile(r'^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)$')

    data = []
    curCluster = None
    curCount = None
    curPercent = None
    curKeywords = []

    for line in lines:
        if line.strip() == "":
            continue

        match = pattern.match(line)

        if match:
            if curCluster is not None:
                keywords = " ".join(curKeywords)
                keywords = re.sub(r'\s+', ' ', keywords)
                keywords = ", ".join([x.strip() for x in keywords.split(",")])
                keywords = keywords.rstrip(".")
                data.append([curCluster, curCount, curPercent, keywords])

            curCluster = int(match.group(1))
            curCount = int(match.group(2))
            curPercent = float(match.group(3).replace(",", "."))
            tail = match.group(4).strip()

            curKeywords = []
            if tail:
                curKeywords.append(tail)

        else:
            txt = line.strip()
            if txt:
                curKeywords.append(txt)

    if curCluster is not None:
        keywords = " ".join(curKeywords)
        keywords = re.sub(r'\s+', ' ', keywords)
        keywords = ", ".join([x.strip() for x in keywords.split(",")])
        keywords = keywords.rstrip(".")
        data.append([curCluster, curCount, curPercent, keywords])

    df = pd.DataFrame(
        data,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )

    return df