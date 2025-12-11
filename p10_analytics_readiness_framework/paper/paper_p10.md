
# P10 – Analytics Readiness Framework (ARF) for Data‑Driven Organizations  

## 1. Abstract  

Organizations hablan de “ser data‑driven”, pero pocas cuentan con una forma clara de medir qué tan preparadas están realmente para operar apoyadas en datos. Este trabajo propone un **Analytics Readiness Framework (ARF)** de cinco niveles, junto con una métrica cuantitativa de readiness que combina dimensiones de personas, procesos, datos, tecnología y gobierno.  

Sobre esta base se construye un pequeño dataset simulado y se generan figuras reproducibles (en Python) que ilustran la distribución de niveles de madurez y el score global de readiness. El enfoque está pensado para ser utilizado en contextos reales: diagnóstico inicial, planificación de hoja de ruta analítica, priorización de iniciativas y comunicación ejecutiva.  

---

## 2. Contexto y Motivación  

En la práctica, muchas compañías invierten en herramientas (BI, nubes, data lakes) sin responder preguntas más profundas:  

- ¿Existen procesos estables para capturar, limpiar y compartir datos?  
- ¿Los equipos de negocio confían en los indicadores?  
- ¿Hay gobierno mínimo y responsables claros sobre definiciones y calidad?  
- ¿Las capacidades analíticas están centralizadas, dispersas o inexistentes?  

Sin un **lenguaje común de madurez**, los debates quedan atrapados en opiniones (“nos falta cultura”, “no hay recursos”, “falta gestión”). El objetivo de este framework es bajar la discusión al terreno de:  

- Dimensiones explícitas.  
- Niveles reconocibles.  
- Métricas replicables.  

---

## 3. Modelo de Madurez: ARF‑1 a ARF‑5  

Se propone un modelo de cinco niveles:  

- **ARF‑1 – Ad‑hoc / Hero mode**  
  - Reportes manuales, poco repetibles.  
  - Dependencia de “héroes” que saben dónde están los datos.  
  - No hay ownership claro ni definiciones estándar.  

- **ARF‑2 – Reporting básico**  
  - Algunos dashboards o reportes recurrentes.  
  - Métricas definidas de forma parcial, con discrepancias entre áreas.  
  - Procesos de carga semi‑manuales; poca automatización.  

- **ARF‑3 – Analítica operacionalizada**  
  - Pipelines recurrentes para indicadores clave.  
  - Catálogo mínimo de datos críticos.  
  - Roles definidos (dueños de dominio, responsables de calidad).  
  - Primeros modelos o scoring en uso controlado.  

- **ARF‑4 – Data‑Driven en dominios clave**  
  - Decisiones relevantes apoyadas en modelos y simulaciones.  
  - Gobierno de datos formalizado, con comités y políticas.  
  - Capacidades analíticas distribuidas: negocio + TI + data.  

- **ARF‑5 – Data Mesh / Producto de datos**  
  - Datos tratados como producto con ciclo de vida completo.  
  - Equipos autónomos mantienen y exponen data products confiables.  
  - Observabilidad de datos, linaje y contratos bien definidos.  

Este esquema permite ubicar a una organización de forma cualitativa, pero para análisis comparables se requiere avanzar hacia un **score numérico de readiness**.  

---

## 4. Dimensiones del Score de Readiness  

El score global de readiness (entre 0 y 100) combina cinco dimensiones:  

1. **Personas & Cultura (P)**  
   - Habilidades analíticas en equipos clave.  
   - Apertura a experimentación y uso de datos.  

2. **Procesos & Operación (O)**  
   - Existencia de procesos estables para ingestión, limpieza y publicación.  
   - Frecuencia y disciplina en el uso de métricas.  

3. **Datos & Calidad (D)**  
   - Integridad, completitud, consistencia.  
   - Trazabilidad mínima y catálogo básico.  

4. **Tecnología & Plataforma (T)**  
   - Herramientas y arquitectura habilitante (BI, data lake, pipelines).  
   - Automatización y orquestación.  

5. **Gobierno & Ownership (G)**  
   - Responsables claros por dominio de datos.  
   - Políticas, definiciones y procesos de cambio controlados.  

Cada dimensión se puntúa de 0 a 100, y el score global ARF se obtiene como promedio ponderado:  

\\[
\\text{ARF\_score} = 0{,}25P + 0{,}20O + 0{,}20D + 0{,}20T + 0{,}15G
\\]  

Los pesos pueden ajustarse por industria (por ejemplo, en minería la dimensión Operación puede pesar más; en banca, Gobierno).  

---

## 5. Dataset Simulado y Figuras  

El script `src/generate_figures_p10.py` construye un dataset sintético de organizaciones con variables:  

- `org_name`  
- `arf_level` (1 a 5)  
- `score_personas`, `score_procesos`, `score_datos`, `score_tecnologia`, `score_gobierno`  
- `score_global` (ARF score)  

A partir de este dataset se generan dos figuras:  

1. **Distribución de organizaciones por nivel ARF**  
   - Figura: `paper/figures/arf_levels.png`  
   - Muestra cuántas organizaciones caen en cada nivel de madurez.  

2. **Distribución del score global de readiness**  
   - Figura: `paper/figures/arf_score_distribution.png`  
   - Muestra la dispersión del readiness dentro de la muestra.  

Las figuras están pensadas para presentaciones ejecutivas, documentos técnicos o reportes de diagnóstico.  

---

## 6. Uso del Framework en la Práctica  

### 6.1. Diagnóstico Inicial  

- Aplicar un cuestionario basado en las cinco dimensiones.  
- Calcular score por dimensión y score global.  
- Identificar el nivel ARF cualitativo dominante (ARF‑2, ARF‑3, etc.).  

### 6.2. Hoja de Ruta Analítica  

- Definir metas de corto plazo (por ejemplo, pasar de ARF‑2 a ARF‑3 en dos dominios críticos).  
- Priorizar iniciativas que mejoran directamente el score (ej. estandarizar definiciones, automatizar cargas, formalizar ownership).  
- Alinear presupuesto con impactos concretos en readiness.  

### 6.3. Seguimiento y Gobierno  

- Reaplicar la evaluación cada 6–12 meses.  
- Medir la evolución del score global y por dimensión.  
- Integrar el ARF como indicador en el tablero de gestión TI / Data.  

---

## 7. Posibles Extensiones  

- Conectar este framework con **OKR de datos** (por ejemplo, objetivos de confiabilidad, adopción de dashboards, tiempo de entrega de reportes críticos).  
- Utilizar el score ARF como variable de entrada para priorizar **roadmaps de producto de datos**.  
- Integrarlo en una **plataforma tipo DataCopilot** que combine diagnóstico automático con recomendaciones de siguiente paso.  

---

## 8. Conclusión  

El Analytics Readiness Framework (ARF) propuesto no pretende ser universal ni definitivo, pero sí operable y accionable. Su valor está en:  

- Convertir conversaciones abstractas sobre “ser data‑driven” en métricas y dimensiones claras.  
- Permitir comparaciones objetivas entre áreas, países o unidades de negocio.  
- Servir como base para diseñar hojas de ruta realistas y medibles.  

Al implementarlo junto con buenas prácticas de ingeniería de datos, visualización y gobierno, el ARF se transforma en una herramienta concreta para que TI, negocio y liderazgo ejecutivo compartan un mismo mapa de madurez analítica.  

---

## 9. Autor  

**Hugo Baghetti Calderón**  
Ingeniero en Informática · Magíster en Gestión TI  
Chile – Portafolio: `analytics-tech-portfolio`  

- 📧 `teleobjetivo.boutique@gmail.com`  
- 🌐 [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- 📷 [@tele.objetivo](https://www.instagram.com/tele.objetivo)
