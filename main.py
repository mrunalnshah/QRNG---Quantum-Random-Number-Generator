# Author : Mrunal Nirajkumar Shah
# Date   : 23rd November, 2025

# Testing my Quantum Random Number Generator Code.

# Our code from scratch
from src.QRNG import QRandom
from src.visualize import visualize_random_numbers

import os


def main():
    ipseudo_random = []
    isimulate = []
    ireal = []

    for _ in range(5):
        # My Quantum Random Number Generator Library Code
        ipseudo_random.append(QRandom.quantum_random_number(8, method="pseudo-random"))
        isimulate.append(QRandom.quantum_random_number(8, method="simulate"))

    api_key = "YOUR OWN API"
    backend_name = "SELECT YOUR QPU MACHINE"
    instance_id = "YOUR CRN NUMBER"
    for _ in range(5):
        ireal.append(QRandom.quantum_random_number(8, method="real", backend_name=backend_name, api_key=api_key, instance_id=instance_id)) 


    if not os.path.exists("plots"):
        os.makedirs("plots")

    visualize_random_numbers(ipseudo_random=ipseudo_random, isimulate=isimulate, ireal=ireal)


if __name__ == "__main__":
    main()