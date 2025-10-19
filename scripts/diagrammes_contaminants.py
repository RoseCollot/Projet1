import pandas as pd
import matplotlib.pyplot as plt
import glob, os

bracken_folder = "/data/projet1/results/bracken"
omark_folder = "/data/projet1/results/omark"

out_bracken = "/data/projet1/results/diagrammes/bracken"
out_omark = "/data/projet1/results/diagrammes/omark"
os.makedirs(out_bracken, exist_ok=True)
os.makedirs(out_omark, exist_ok=True)


# Bracken
for f in glob.glob(os.path.join(bracken_folder, "*.bracken")):
    g = os.path.basename(f).replace(".bracken", "")
    df = pd.read_csv(f, sep="\t")
    df_plot = df[df["fraction_total_reads"] >= 0.01].nlargest(10, "fraction_total_reads")
    explode = [0.05 if x < 0.05 else 0 for x in df_plot["fraction_total_reads"]]
    plt.figure(figsize=(6,6))
    plt.pie(df_plot["fraction_total_reads"], labels=df_plot["name"], autopct="%1.1f%%", explode=explode)
    plt.title(f"{g} - Bracken")
    plt.savefig(f"{out_bracken}/{g}_bracken.png")
    plt.close()
    df.to_excel(f"{out_bracken}/{g}_bracken.xlsx", index=False)


# OMARK
for f in glob.glob(f"{omark_folder}/*/*_detailed_summary.txt"):
    name = os.path.basename(f).replace("_detailed_summary.txt", "")
    clades, percents = [], []
    with open(f) as file:
        for line in file:
            if line.startswith("Clade:"):
                clades.append(line.split(":")[1].strip())
            if "Number of associated query proteins:" in line:
                perc = line.split("(")[1].split("%")[0]
                percents.append(float(perc))
    if not clades:
        continue
    df = pd.DataFrame({"clade": clades, "percent": percents})
    df_top = df.nlargest(10, "percent")
    plt.figure(figsize=(6,6))
    plt.pie(df_top["percent"], labels=df_top["clade"], autopct="%1.1f%%")
    plt.title(f"{name} - OMARK")
    plt.savefig(f"{out_omark}/{name}_omark.png")
    plt.close()

