import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Funciones para el ajuste exponencial y cálculos estadísticos
def ajuste_exponente(n, T):
    """
    Ajusta un modelo de potencia T = A * n^B a los datos (n, T).
    Devuelve los parámetros A y B.
    """
    log_n = np.log(n)
    log_T = np.log(T)
    
    N = len(n)
    sum_log_T_log_n = np.sum(log_T * log_n)
    sum_log_T = np.sum(log_T)
    sum_log_n = np.sum(log_n)
    sum_log_n_sq = np.sum(log_n ** 2)

    B = (N * sum_log_T_log_n - sum_log_T * sum_log_n) / (N * sum_log_n_sq - sum_log_n ** 2)
    log_A = (sum_log_T - B * sum_log_n) / N
    A = np.exp(log_A)

    return A, B

def calcular_r2(n, T_real, A, B):

    T_predicho = A * (n ** B)
    ss_res = np.sum((T_real - T_predicho) ** 2) 
    ss_tot = np.sum((T_real - np.mean(T_real)) ** 2) 
    R2 = 1 - (ss_res / ss_tot)
    return R2

def calcular_chi_cuadrado(n, T_real, A, B):
  
    T_predicho = A * (n ** B)
    chi2_valor = np.sum((T_real - T_predicho) ** 2 / T_predicho)
    gl = len(n) - 2  # Grados de libertad
    p_valor = 1 - chi2.cdf(chi2_valor, gl)  # p-valor asociado
    
    return chi2_valor, p_valor

# Datos de tiempo de ejecución para Quicksort y Mergesort
runtime_qs = np.array([
    [1.385818, 1.384341, 1.384140, 1.386150, 1.383565],  # List 1
    [2.892215, 2.891096, 2.891577, 2.893829, 2.891222],  # List 2
    [4.445842, 4.481678, 4.452973, 4.450928, 4.450758],  # List 3
    [6.068797, 6.036199, 6.031617, 6.027026, 6.034869],  # List 4
    [7.653127, 7.689329, 7.653584, 7.639974, 7.666140],  # List 5
    [9.274329, 9.261073, 9.276486, 9.305112, 9.286586],  # List 6
    [10.960954, 10.959580, 10.938592, 10.934368, 10.935601],  # List 7
    [12.563861, 12.594634, 12.569935, 12.589570, 12.573120],  # List 8
    [14.268894, 14.268346, 14.266580, 14.278928, 14.230752],  # List 9
    [15.918620, 15.926294, 15.953472, 15.917556, 15.953832],  # List 10
    [17.569322, 17.588513, 17.571993, 17.596986, 17.583468],  # List 11
    [19.300968, 19.370587, 19.256301, 19.285297, 19.278155],  # List 12
    [20.991854, 21.069830, 21.026550, 21.005639, 20.996180],  # List 13
    [22.714470, 22.856862, 22.778895, 22.799358, 22.720617],  # List 14
    [24.453539, 24.511680, 24.405023, 24.396452, 24.406406],  # List 15
    [26.150361, 26.252884, 26.162321, 26.157161, 26.177191],  # List 16
    [27.898817, 27.813879, 27.833490, 27.862367, 27.827223],  # List 17
    [29.576041, 29.602637, 29.702097, 29.685257, 29.689094],  # List 18
    [31.427308, 31.333300, 31.295492, 31.362782, 31.472783],  # List 19
    [33.125519, 33.011012, 32.976043, 32.995252, 32.974608]   # List 20
])

runtime_ms = np.array([
    [1.680628, 1.654949, 1.652900, 1.656845, 1.653733],  # List 1
    [3.444859, 3.443257, 3.444491, 3.443581, 3.446578],  # List 2
    [5.268275, 5.286098, 5.274715, 5.269208, 5.289469],  # List 3
    [7.172657, 7.140638, 7.152467, 7.151795, 7.148451],  # List 4
    [8.971495, 8.986355, 8.958275, 8.985883, 8.964846],  # List 5
    [10.949872, 10.939289, 10.965354, 10.960126, 10.978112],  # List 6
    [12.873123, 12.892061, 12.894302, 12.899459, 12.910580],  # List 7
    [14.859925, 14.873749, 14.891301, 14.871834, 14.834878],  # List 8
    [16.790910, 16.789143, 16.802121, 16.809610, 16.772360],  # List 9
    [18.613773, 18.636901, 18.642212, 18.625728, 18.642213],  # List 10
    [20.639924, 20.643030, 20.672473, 20.712082, 20.762349],  # List 11
    [22.771825, 22.784200, 22.765867, 22.788265, 22.779880],  # List 12
    [24.691573, 24.807046, 24.653429, 24.648676, 24.741058],  # List 13
    [26.765960, 26.819914, 26.811762, 26.832844, 26.869280],  # List 14
    [28.775857, 28.706523, 28.598756, 28.622842, 28.684348],  # List 15
    [30.815437, 30.883685, 30.886500, 30.843161, 30.868733],  # List 16
    [32.971445, 33.032880, 32.955959, 32.940081, 32.837494],  # List 17
    [35.029724, 35.044797, 34.967969, 34.957281, 34.981498],  # List 18
    [36.901725, 36.739118, 36.864702, 37.021695, 36.949902],  # List 19
    [38.687900, 38.751216, 38.534074, 38.515979, 38.500764]   # List 20
])

# Procesamiento de datos
cantidad_datos = np.arange(10, 210, 10)  # Tamaños de lista (en millones)
avg_qs = np.mean(runtime_qs, axis=1)  # Promedio de tiempos para Quicksort
avg_ms = np.mean(runtime_ms, axis=1)  # Promedio de tiempos para Mergesort

# Ajuste exponencial
A_qs, B_qs = ajuste_exponente(cantidad_datos, avg_qs)
A_ms, B_ms = ajuste_exponente(cantidad_datos, avg_ms)

# Gráfico de los datos
plt.scatter(cantidad_datos, avg_qs, color='red', label="Quicksort", s=10)
plt.scatter(cantidad_datos, avg_ms, color='blue', label="Mergesort", s=10)

# Curvas de ajuste
x_vals = np.linspace(min(cantidad_datos), max(cantidad_datos), 400)
y_qs_fit = A_qs * (x_vals ** B_qs)
y_ms_fit = A_ms * (x_vals ** B_ms)

plt.plot(x_vals, y_qs_fit, color='red', linestyle='dashed', label=f"Funcion Quicksort: {A_qs:.3f} n^{B_qs:.3f}")
plt.plot(x_vals, y_ms_fit, color='blue', linestyle='dashed', label=f"Funcion Mergesort: {A_ms:.3f} n^{B_ms:.3f}")

# Configuración del gráfico
plt.xlabel("Tamaño de la lista (Millones)")
plt.ylabel("Tiempo de ejecución (Segundos)")
plt.title("Quicksort vs Mergesort")
plt.legend()
plt.grid(True)

# Guardar el gráfico
plt.savefig('mi_grafica_corregida.png')

# Cálculo de R^2 y chi-cuadrado
R2_qs = calcular_r2(cantidad_datos, avg_qs, A_qs, B_qs)
R2_ms = calcular_r2(cantidad_datos, avg_ms, A_ms, B_ms)

chi2_qs, p_qs = calcular_chi_cuadrado(cantidad_datos, avg_qs, A_qs, B_qs)
chi2_ms, p_ms = calcular_chi_cuadrado(cantidad_datos, avg_ms, A_ms, B_ms)

