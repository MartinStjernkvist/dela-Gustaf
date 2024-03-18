import numpy as np

dim = 5 * 5 * 0.5 * 10 ** (3 * (-3))  # m
U = 4.56  # V
a = 0.5 * 10 ** (-3)  # m
e = 1.602 * 10 ** -19
B = 0.135  # T

I = [(0.5 + i) * 10 ** -3 for i in range(10)]  # mA

V_H_1_mV = [2.3, 6.9, 11.4, 16.1, 20.7, 25.3, 30.0, 34.6, 39.3, 44.1]
V_H_background_1_mV = [3.4, 10.4, 17.4, 24.3, 31.3, 38.3, 45.2, 52.3, 59.4, 66.4]

V_H_2_mV = [1.7, 5.1, 8.6, 12.0, 15.4, 18.9, 22.3, 25.8, 29.2, 32.7]
V_H_background_2_mV = [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 1.0, 1.2, 1.3, 1.5]

V_H_diff_1 = [(V_H_1_mV[i] - V_H_background_1_mV[i]) * 10 ** -3 for i in range(len(V_H_1_mV))]
V_H_diff_2 = [(V_H_2_mV[i] - V_H_background_2_mV[i]) * 10 ** -3 for i in range(len(V_H_2_mV))]


def R(I):
    return U / I


R = list(map(R, I))
print(f'\nR: {R}')


def R_H(V_H, I):
    return V_H * a / (I * B)


R_H_1 = [R_H(v, i) for v, i in zip(V_H_diff_1, I)]
R_H_2 = [R_H(v, i) for v, i in zip(V_H_diff_2, I)]

R_H_1_mean = np.mean(R_H_1)
R_H_2_mean = np.mean(R_H_2)

print(f'\nR_H_1: {R_H_1}\nR_H_1_medel: {R_H_1_mean}')
print(f'\nR_H_2: {R_H_2}\nR_H_2_medel: {R_H_2_mean}')

q_1 = - e
q_2 = + e


def n(R_H, q):
    return 1 / (q * R_H)


print(f'\nn_1: ', n(R_H_1_mean, q_1))
print(f'n_2: ', n(R_H_2_mean, q_2))