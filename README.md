# Portafolio – Performance & Analytics en Minería

Este repositorio reúne 3 proyectos orientados a demostrar capacidades de **análisis de datos, modelamiento y visualización** aplicadas al contexto minero, con foco en mantenimiento, desempeño de activos y mejora continua.

Los proyectos están implementados en **Python (pandas, Jupyter Notebooks)** y utilizan datos simulados estructurados de forma similar a extracciones típicas de **SAP PM / ERP**.  
La idea es que la lógica y los indicadores puedan llevarse fácilmente a herramientas como **Power BI** u otras plataformas corporativas.

---

## P01 – Salud de Activos: Camiones de Extracción

**Carpeta:** `p01_salud_activos_camiones/`  

**Objetivo:** analizar la disponibilidad, MTBF, MTTR y principales causas de falla de una flota de camiones CAEX en una faena minera ficticia (“Faena Atacama Norte”).

**Tecnologías:**

- Python, pandas, matplotlib
- Jupyter Notebook

**Entregables:**

- Datos: `data/camiones_mina_mantenimiento.csv`
- Notebook: `notebooks/p01_analisis_salud_activos.ipynb`
- Imágenes: `img/`
  - `disponibilidad_promedio_por_equipo.png`
  - `horas_paro_total_por_equipo.png`
  - `top_causas_falla.png`
- Documentación: `README.md`

---

## P02 – Backlog de Mantenimiento: Priorización de Órdenes de Trabajo

**Carpeta:** `p02_backlog_mantenimiento/`  

**Objetivo:** analizar el **backlog de órdenes de trabajo** de mantenimiento y construir un **score de prioridad** que combine criticidad, antigüedad y estado de las OT, facilitando la planificación y la mejora continua (enfoque PDCA).

**Tecnologías:**

- Python, pandas, matplotlib
- Jupyter Notebook

**Entregables:**

- Datos: `data/backlog_ordenes_trabajo.csv`
- Notebook: `notebooks/p02_analisis_backlog.ipynb`
- Imágenes: `img/`
  - `backlog_por_criticidad.png`
  - `distribucion_dias_backlog.png`
  - `score_vs_dias_backlog.png`
- Documentación: `README.md`

---

## P03 – Fallas en Correas Transportadoras

**Carpeta:** `p03_fallas_correas/`  

**Objetivo:** analizar fallas en **correas transportadoras** para identificar correas, tramos y causas críticas, y simular un **escenario de mejora** donde se reduce el impacto de la causa principal en horas de paro y toneladas no producidas.

**Tecnologías:**

- Python, pandas, matplotlib
- Jupyter Notebook

**Entregables:**

- Datos: `data/fallas_correas_transportadoras.csv`
- Notebook: `notebooks/p03_analisis_fallas_correas.ipynb`
- Imágenes: `img/`
  - `horas_paro_por_correa.png`
  - `impacto_produccion_por_correa.png`
  - `top_causas_falla_correas.png`
- Documentación: `README.md`

---

## Cómo ejecutar

1. Clonar el repositorio.
2. Crear entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
