# Author : Mrunal Nirajkumar Shah
# Date   : 23rd November, 2025

# Visualising the Random Values

import matplotlib.pyplot as plt
import seaborn as sns

def visualize_random_numbers(ipseudo_random, isimulate, ireal):
    datasets = {
        "Pseudo Random (Matrix Ops)": ipseudo_random,
        "Aer Simulator": isimulate,
        "Real IBM Hardware": ireal,
    }

    for name, data in datasets.items():
        plt.figure(figsize=(8, 5))
        plt.hist(data, bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {name}")
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f"plots/{name}_hist.png")
        plt.close()

        plt.figure(figsize=(8, 5))
        plt.plot(data, marker='o', linestyle='-', color='green')
        plt.title(f"Line Plot of {name}")
        plt.xlabel("Sample Index")
        plt.ylabel("Value")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f"plots/{name}_line.png")
        plt.close()

        plt.figure(figsize=(6, 5))
        sns.boxplot(data=data)
        plt.title(f"Box Plot of {name}")
        plt.tight_layout()
        plt.savefig(f"plots/{name}_box.png")
        plt.close()

        plt.figure(figsize=(8, 5))
        plt.scatter(range(len(data)), data, color='purple')
        plt.title(f"Scatter Plot of {name}")
        plt.xlabel("Sample Index")
        plt.ylabel("Value")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f"plots/{name}_scatter.png")
        plt.close()

        plt.figure(figsize=(8, 5))
        sns.kdeplot(data, color='red', fill=True)
        plt.title(f"Distribution (KDE) of {name}")
        plt.xlabel("Value")
        plt.tight_layout()
        plt.savefig(f"plots/{name}_kde.png")
        plt.close()

    print("All plots saved successfully in the plots folder!\n")