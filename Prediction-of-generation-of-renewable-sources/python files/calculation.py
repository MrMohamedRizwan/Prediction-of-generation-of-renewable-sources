import numpy as np

# Define the variables and functions
T=60
η = 0.8  # efficiency
I = lambda λ, θ: np.sin(θ) / λ**2  # spectral radiance
A = lambda λ: 1.0  # spectral transmittance of the atmosphere
G = lambda λ, T: np.exp(-0.0144 * (1.0 / λ - 1.0 / 0.555) * T)  # atmospheric transmittance
F = lambda λ, S: 0.99 if λ >= 0.4 and λ <= 0.7 else 0.0 if λ < 0.4 or λ > 0.7 else S  # spectral reflectance of the surface
cos = lambda θ: np.cos(θ)
S=60
# S mean cloud shading
# Define the integration ranges
λ_min = 0.3
λ_max = 1.1
θ_min = 0.0
θ_max = np.pi / 2.0

# Define the number of points for the integration
N_λ = 1000
N_θ = 1000

# Define the step size for the integration
dλ = (λ_max - λ_min) / N_λ
dθ = (θ_max - θ_min) / N_θ

# Perform the integration using a double loop
P = 0.0
for i in range(N_λ):
    λ = λ_min + i * dλ
    for j in range(N_θ):
        θ = θ_min + j * dθ
        P += η * I(λ, θ) * A(λ) * G(λ, T) * F(λ, S) * cos(θ) * dλ * dθ

print("The result of the integration is:", P)
