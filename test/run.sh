#!/bin/bash

# Connect to the remote server and run commands
ssh klarko01@b103ws11 << EOF
rm -r Decomposition-Algorithms-for-Scalable-Quantum-Annealing/
git clone https://github.com/Larkoss/Decomposition-Algorithms-for-Scalable-Quantum-Annealing.git
cd Decomposition-Algorithms-for-Scalable-Quantum-Annealing/
export DWAVE_API_TOKEN=DEV-06975103e50142c4c36d07209c087d532ed6bcce
python3 validate_DBR.py &
EOF
#scp klarko01@b103ws10:/home/students/cs/2019/klarko01/Decomposition-Algorithms-for-Scalable-Quantum-Annealing/results.txt .