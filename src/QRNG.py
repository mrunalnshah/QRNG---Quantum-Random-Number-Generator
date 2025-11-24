# Author : Mrunal Nirajkumar Shah
# Date   : 23rd November, 2025

"""
Implementing QRandom Class for hadamard, pauli_z, zero_state, apply_gate, measure, 
quantum_random_bit, quantum_random_number implementation from scratch.

1. Qunatum Random Number Generator Using Traditional Computer (Pseudo Random).
2. Using Aer Simulator
3. Using IBM Quantum Machines
"""



from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

import numpy as np

class QRandom:
    @staticmethod
    def hadamard():
        """ 
        Returns the 2x2 Hadamard matrix.
        """
        return (1/np.sqrt(2) * np.array([[1,1], [1,-1]]))

    @staticmethod
    def pauli_z():
        """
        Pauli-Z gate (for measurement in computational basis)
        """
        return np.array([[1,0], [0, -1]])
    
    @staticmethod
    def zero_state():
        """
        |0⟩ : Zero State - lowest energy state for a qubit
        """
        return np.array([[1], [0]], dtype=complex)
    
    @staticmethod
    def apply_gate(state, gate):
        """
        returns the dot product of gate, and a state. Mostly zero_state and hadamard matrix.
        """
        return np.dot(gate, state)
    
    @staticmethod
    def measure(state):
        """
        Measures a single qubit in computational basis.
        Returns 0 or 1 randomly according to probabilities.
        """

        prob_0 = np.abs(np.pow(state[0,0],2))
        prob_1 = np.abs(np.pow(state[1,0],2))

        return np.random.choice([0,1], p=[prob_0, prob_1])
    
    @staticmethod
    def quantum_random_bit(method="simulate", backend_name=None, api_key=None, instance_id=None):
        """
        Generate a random bit.

        method: "simulate" or "real" or "pseudo-random"
        backend_name: for real devices, name of IBMQ backend
        """

        if method == "pseudo-random":
            # Start in |0>
            state = QRandom.zero_state()

            # Apply Hamarad gate to create superposition
            state = QRandom.apply_gate(state, QRandom.hadamard())

            # Measure the qubit
            return QRandom.measure(state)
        
        # Require Qiskit Functionality to run on Aer Simulator
        elif method == "simulate":
            simulator = AerSimulator()

            qc = QuantumCircuit(1,1)
            qc.h(0)
            qc.measure(0,0)

            tqc = transpile(qc, simulator)

            job = simulator.run(tqc, shots=1)
            result = job.result()

            counts = result.get_counts()
            
            return int(list(counts.keys())[0], 2)
        
        # Require Qiskit Functionality to run on IBM machine
        elif method == "real":
            service = QiskitRuntimeService(token=api_key, instance=instance_id, channel="ibm_quantum_platform")
            backend = service.backend(backend_name)
            sampler = SamplerV2(mode=backend)

            qc = QuantumCircuit(1,1)
            qc.h(0) 
            qc.measure(0,0)

            pman = generate_preset_pass_manager(optimization_level=1, backend=backend)
            isa_qc = pman.run(qc)

            job = sampler.run([isa_qc], shots=1)
            result = job.result()

            counts = result[0].data.c.get_counts()
            bit = int(list(counts.keys())[0])
            return bit
    
    @staticmethod
    def quantum_random_number(n_bits=8, method="simulate", backend_name=None, api_key=None, instance_id=None, lower_bound=0, upper_bound=255):
        """
        Generates a random integer with n_bits using Quantum Random Bit

        method: "simulate" or "real" or "pseudo-random"
        backend_name: for real devices, name of IBMQ backend
        """

        bits = [str(QRandom.quantum_random_bit(method, backend_name=backend_name, api_key=api_key, instance_id=instance_id)) for _ in range(n_bits)]
        rand_bits = int("".join(bits), 2)
        return lower_bound + (rand_bits % (upper_bound - lower_bound + 1))
    
