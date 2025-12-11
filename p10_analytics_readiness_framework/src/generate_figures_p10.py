
"""
generate_figures_p10.py

Genera un dataset simulado de organizaciones y su nivel de Analytics Readiness,
junto con dos figuras para el paper:

- paper/figures/arf_levels.png
- paper/figures/arf_score_distribution.png
"""

import random
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# -----------------------------------------------------------------------------
# Configuración de rutas
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]  # p10_analytics_readiness_framework
PAPER_DIR = BASE_DIR / "paper"
FIG_DIR = PAPER_DIR / "figures"

PAPER_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------------------------------------------------------
# Generación de dataset simulado
# -----------------------------------------------------------------------------
random.seed(42)

orgs = []
n_orgs = 80

for i in range(1, n_orgs + 1):
    name = f"Org_{i:02d}"

    # Nivel ARF "aproximado"
    arf_level = random.choices(
        population=[1, 2, 3, 4, 5],
        weights=[0.15, 0.30, 0.30, 0.20, 0.05],
        k=1,
    )[0]

    # Scores por dimensión según nivel, con un poco de ruido
    base = {
        1: (20, 25, 20, 25, 15),
        2: (35, 40, 35, 40, 30),
        3: (55, 60, 55, 60, 50),
        4: (70, 75, 70, 75, 65),
        5: (85, 90, 85, 90, 80),
    }[arf_level]

    score_personas = max(0, min(100, random.gauss(base[0], 7)))
    score_procesos = max(0, min(100, random.gauss(base[1], 7)))
    score_datos = max(0, min(100, random.gauss(base[2], 7)))
    score_tecnologia = max(0, min(100, random.gauss(base[3], 7)))
    score_gobierno = max(0, min(100, random.gauss(base[4], 7)))

    score_global = (
        0.25 * score_personas
        + 0.20 * score_procesos
        + 0.20 * score_datos
        + 0.20 * score_tecnologia
        + 0.15 * score_gobierno
    )

    orgs.append(
        {
            "org_name": name,
            "arf_level": arf_level,
            "score_personas": round(score_personas, 1),
            "score_procesos": round(score_procesos, 1),
            "score_datos": round(score_datos, 1),
            "score_tecnologia": round(score_tecnologia, 1),
            "score_gobierno": round(score_gobierno, 1),
            "score_global": round(score_global, 1),
        }
    )

df = pd.DataFrame(orgs)
csv_path = BASE_DIR / "arf_dataset_simulado.csv"
df.to_csv(csv_path, index=False)
print(f"✅ Dataset simulado guardado en: {csv_path}")


# -----------------------------------------------------------------------------
# Figura 1: Distribución de organizaciones por nivel ARF
# -----------------------------------------------------------------------------
counts = df["arf_level"].value_counts().sort_index()

plt.figure()
counts.plot(kind="bar")
plt.xlabel("Nivel ARF")
plt.ylabel("Número de organizaciones")
plt.title("Distribución de organizaciones por nivel de Analytics Readiness")
plt.tight_layout()

fig1_path = FIG_DIR / "arf_levels.png"
plt.savefig(fig1_path)
plt.close()
print(f"✅ Figura 1 guardada en: {fig1_path}")


# -----------------------------------------------------------------------------
# Figura 2: Distribución del score global de readiness
# -----------------------------------------------------------------------------
plt.figure()
df["score_global"].plot(kind="hist", bins=10)
plt.xlabel("Score global de readiness")
plt.ylabel("Frecuencia")
plt.title("Distribución del score ARF (0–100)")
plt.tight_layout()

fig2_path = FIG_DIR / "arf_score_distribution.png"
plt.savefig(fig2_path)
plt.close()
print(f"✅ Figura 2 guardada en: {fig2_path}")
