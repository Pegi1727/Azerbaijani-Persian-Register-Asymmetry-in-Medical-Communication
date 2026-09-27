import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")

scenarios = [
    "Scenario 1\n(Colloquial Az Patient)",
    "Scenario 2\n(Formal Educated Patient)",
    "Scenario 3\n(Elevated Technical Az Patient)"
]
# مقادیر گزارش‌شده به سمت استفاده از زبان فارسی (یا شیفت به فارسی)
persian_reliance_metric = [30.0, 60.0, 100.0]  # نمرات مقیاس بازنمایی‌شده در قالب شدت گرایش به فارسی

plt.figure(figsize=(7, 4.5))
plt.plot(scenarios, persian_reliance_metric, marker='o', linewidth=2.5, markersize=8, color='#c0392b')
plt.title("Inverted Register Gradient: Reported Shift to Persian by Patient Register", fontsize=11, fontweight='bold')
plt.ylabel("Reported Reliance on Persian (%) / Scale Position", fontsize=10)
plt.ylim(0, 110)
plt.tight_layout()
plt.savefig("figures_inverted_gradient.png", dpi=300)
print("Figure saved to figures_inverted_gradient.png")
