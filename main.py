import numpy as np
import time

def f(x):
    return 4 / (1 + x**2)

def trapezoid_integral(a, b, N):
    x = np.linspace(a, b, N + 1)
    y = f(x)
    dx = (b - a) / N
    integral = (dx / 2) * np.sum(y[:-1] + y[1:])
    return integral

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menghitung nilai integral, galat RMS, dan waktu eksekusi
for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integral(0, 1, N)
    end_time = time.time()
    
    # Menghitung galat RMS
    error = np.abs(pi_ref - pi_approx)
    rms_error = np.sqrt(np.mean(error**2))
    
    # Mengukur waktu eksekusi
    execution_time = end_time - start_time
    
    print(f"N = {N}")
    print(f"Pi Approximation = {pi_approx}")
    print(f"RMS Error = {rms_error}")
    print(f"Execution Time = {execution_time} seconds\n")
