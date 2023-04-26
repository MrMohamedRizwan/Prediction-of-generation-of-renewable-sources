import numpy as np
#Latitude of current location

Latitude=10.76

# efficiency of solar panel

η = 0.3

#for more efficiancy

θ= Latitude+15

#lamda represents the wavelength of light

I = lambda λ, θ: np.sin(θ) / λ**2  # spectral radiance
A = lambda λ: 1.0  # spectral transmittance of the atmosphere
G = lambda λ, T: np.exp(-0.0144 * (1.0 / λ - 1.0 / 0.555) * T)  # atmospheric transmittance
F = lambda λ, S: 0.99 if λ >= 0.4 and λ <= 0.7 else 0.0 if λ < 0.4 or λ > 0.7 else S  # spectral reflectance of the surface
cos = lambda θ: np.cos(θ)

# S mean cloud shading

S=30/100

# integration ranges
λ_min = 0.3
λ_max = 1.1
θ_min = 0.0
θ_max = np.pi / 2.0
# Time interval
T=60
#The number of points for the integration
# maximum points are taken
N_λ = 1000 
N_θ = 1000

#step size for the integration

dλ = (λ_max - λ_min) / N_λ
dθ = (θ_max - θ_min) / N_θ

# P stores the value of power

P = 0.0
for i in range(N_λ):
    λ = λ_min + i * dλ
    for j in range(N_θ):
        θ = θ_min + j * dθ
        P += η * I(λ, θ) * A(λ) * G(λ, T) * F(λ, S) * cos(θ) * dλ * dθ

print("The result of the integration is:", P*10)