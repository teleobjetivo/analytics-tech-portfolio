
# P10 – Analytics Readiness Framework (ARF) for Data‑Driven Organizations

Este proyecto define y ejemplifica un **marco de madurez analítica (Analytics Readiness Framework, ARF)** pensado para áreas de TI, data & analytics y negocio que buscan evaluar de forma estructurada qué tan preparadas están para trabajar realmente basadas en datos.

El objetivo no es solo hacer gráficos bonitos, sino mostrar **cómo piensa un líder técnico** al momento de:
- Traducir estrategia en métricas.
- Definir dimensiones evaluables.
- Construir un score reproducible.
- Comunicar resultados en un lenguaje ejecutivo.

> Este proyecto funciona como “paper vivo”: el código genera las figuras y el documento técnico se puede versionar y extender.

---

## 🎯 Objetivos del Proyecto

1. Definir un **framework de madurez analítica** con niveles claros (ARF‑1 a ARF‑5).
2. Modelar una **métrica numérica de readiness** combinando varias dimensiones (personas, procesos, datos, tecnología, gobierno).
3. Generar **figuras reproducibles** para un informe tipo paper (bar chart de niveles y distribución de score).
4. Entregar un **documento técnico** en lenguaje profesional que pueda ser usado como:
   - base de consultoría,
   - apoyo en reuniones ejecutivas,
   - anexo técnico en procesos de selección o licitación.

---

## 📂 Estructura del Proyecto

```bash
p10_analytics_readiness_framework/
├── README.md                 # Descripción ejecutiva del proyecto
├── paper/
│   ├── paper_p10.md          # Mini-paper en formato Markdown
│   └── figures/              # Figuras generadas por el script
│       ├── arf_levels.png
│       └── arf_score_distribution.png
└── src/
    └── generate_figures_p10.py  # Script para generar figuras y dataset simulado
```

---

## 🧪 Cómo Ejecutar el Proyecto

Asumiendo que ya tienes creado y activado el entorno virtual en la carpeta raíz del portafolio (`Proyecto Mineria/.venv`):

```bash
cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
source .venv/bin/activate

# Instalar dependencias si hiciera falta
pip install pandas matplotlib

# Ejecutar el generador de figuras de P10
python p10_analytics_readiness_framework/src/generate_figures_p10.py
```

Esto generará:

- `paper/figures/arf_levels.png`
- `paper/figures/arf_score_distribution.png`

Puedes abrir luego `paper/paper_p10.md` en VS Code o cualquier editor Markdown para revisar el contenido como mini‑paper.

---

## 🧠 Qué demuestra este proyecto

Desde el punto de vista profesional, este proyecto muestra que puedes:

- **Definir marcos conceptuales** (no solo código).
- Aterrizar ideas en **métricas y dimensiones medibles**.
- Generar **artefactos ejecutivos** (figuras y documentos) para discusión estratégica.
- Trabajar con **ciencia de datos ligera + pensamiento de consultor**.

Es el tipo de iniciativa que un **Gerente TI, Head of Data, Chief Data Officer o Arquitecto** podría liderar al diseñar una hoja de ruta analítica a 2–3 años.

---

## 👤 About Me – Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

Me especializo en estructurar y escalar procesos de análisis basados en datos, generar valor desde la observación —desde la operación minera hasta la investigación astronómica— y traducir métricas complejas en decisiones claras. He trabajado en arquitectura de datos, integración de sistemas, automatización, gestión de plataformas TI y habilitación de equipos técnicos.

Exploro, investigo y construyo soluciones. Mi enfoque une el método científico, la ingeniería y la narrativa visual; desde modelos analíticos hasta proyectos de cielo profundo. Creo en el uso inteligente de la información, en la rigurosidad técnica y en la elegancia de las soluciones simples que funcionan.

- 📧 Email: `teleobjetivo.boutique@gmail.com`
- 🌐 Web: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)
- 📷 Instagram: [@tele.objetivo](https://www.instagram.com/tele.objetivo)
- 💻 GitHub (portafolio): [`teleobjetivo/analytics-tech-portfolio`](https://github.com/teleobjetivo/analytics-tech-portfolio)
