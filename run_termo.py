from termo import plot_find_alpha_and_epsilon, find_alpha_and_epsilon, C
import matplotlib.pyplot as plt

square_mm_to_square_m = 10 ** -6

"""
constants
"""
c_Al = 0.89  # J / (g *C)
c_Cu = 0.385

m_Cu_blank = 44.7
m_Cu_repad = 12.7
m_Cu_bucklig = 44.5
m_Al_blank = 7.4
m_Al_repad = 14
m_Al_bucklig = 14.9
m_Cu_svart = 23.6
m_Cu_vit = 22.8

A_Cu_blank = 2500 * square_mm_to_square_m
A_Cu_repad = 2600 * square_mm_to_square_m
A_Cu_bucklig = 2576 * square_mm_to_square_m
A_Al_blank = 2401 * square_mm_to_square_m
A_Al_repad = 2500 * square_mm_to_square_m
A_Al_bucklig = 2626 * square_mm_to_square_m
A_Cu_svart = 2500 * square_mm_to_square_m
A_Cu_vit = 2500 * square_mm_to_square_m

C_Cu_blank = C(c_Cu, m_Cu_blank)
C_Cu_repad = C(c_Cu, m_Cu_repad)
C_Cu_bucklig = C(c_Cu, m_Cu_bucklig)
C_Al_blank = C(c_Al, m_Al_blank)
C_Al_repad = C(c_Al, m_Al_repad)
C_Al_bucklig = C(c_Al, m_Al_bucklig)
C_Cu_svart = C(c_Cu, m_Cu_svart)
C_Cu_vit = C(c_Cu, m_Cu_vit)

test_time1 = 10
test_time2 = 30

'''aluminium'''

file_path_Al_blank_v1 = 'aluminium_blank'
_, alpha_Al_blank_v1, epsilon_Al_blank_v1, Temp_max_Al_blank_v1 = find_alpha_and_epsilon(file_path_Al_blank_v1, 22.1,
                                                                                         C_Al_blank, A_Al_blank,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_blank_v1, 22.1, C_Al_blank, A_Al_blank, test_time1)

file_path_Al_blank_v2 = 'aluminium_blank_v2'
# högt epsilon jämfört med v1 och andra aluminium
_, alpha_Al_blank_v2, epsilon_Al_blank_v2, Temp_max_Al_blank_v2 = find_alpha_and_epsilon(file_path_Al_blank_v2, 22.4,
                                                                                         C_Al_blank, A_Al_blank,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_blank_v2, 22.4, C_Al_blank, A_Al_blank, test_time1)

file_path_Al_bucklig_v1 = 'aluminium_bucklig_2'
_, alpha_Al_bucklig_v1, epsilon_Al_bucklig_v1, Temp_max_Al_bucklig_v1 = find_alpha_and_epsilon(file_path_Al_bucklig_v1,
                                                                                               22.2, C_Al_bucklig,
                                                                                               A_Al_bucklig, test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_bucklig_v1, 22.2, C_Al_bucklig, A_Al_bucklig, test_time1)

file_path_Al_bucklig_v2 = 'aluminium_bucklig_v2'
_, alpha_Al_bucklig_v2, epsilon_Al_bucklig_v2, Temp_max_Al_bucklig_v2 = find_alpha_and_epsilon(file_path_Al_bucklig_v2,
                                                                                               22.3, C_Al_bucklig,
                                                                                               A_Al_bucklig, test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_bucklig_v2, 22.3, C_Al_bucklig, A_Al_bucklig, test_time1)

file_path_Al_repad_v1 = 'aluminium_repad'
_, alpha_Al_repad_v1, epsilon_Al_repad_v1, Temp_max_Al_repad_v1 = find_alpha_and_epsilon(file_path_Al_repad_v1, 21.9,
                                                                                         C_Al_repad, A_Al_repad,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_repad_v1, 21.9, C_Al_repad, A_Al_repad, test_time1)

file_path_Al_repad_v2 = 'aluminium_repad_v2'
_, alpha_Al_repad_v2, epsilon_Al_repad_v2, Temp_max_Al_repad_v2 = find_alpha_and_epsilon(file_path_Al_repad_v2, 22.3,
                                                                                         C_Al_repad, A_Al_repad,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Al_repad_v2, 22.3, C_Al_repad, A_Al_repad, test_time1)

'''koppar'''

file_path_Cu_blank_v1 = 'koppar_blank'
# väldigt lågt epsilon jämfört med v2
_, alpha_Cu_blank_v1, epsilon_Cu_blank_v1, Temp_max_Cu_blank_v1 = find_alpha_and_epsilon(file_path_Cu_blank_v1, 21.8,
                                                                                         C_Cu_blank, A_Cu_blank,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_blank_v1, 21.8, C_Cu_blank, A_Cu_blank, test_time1)

file_path_Cu_blank_v2 = 'koppar_blank_v2'
_, alpha_Cu_blank_v2, epsilon_Cu_blank_v2, Temp_max_Cu_blank_v2 = find_alpha_and_epsilon(file_path_Cu_blank_v2, 22.0,
                                                                                         C_Cu_blank, A_Cu_blank,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_blank_v2, 22.0, C_Cu_blank, A_Cu_blank, test_time1)

file_path_Cu_bucklig_v1 = 'koppar_bucklig'
_, alpha_Cu_bucklig_v1, epsilon_Cu_bucklig_v1, Temp_max_Cu_bucklig_v1 = find_alpha_and_epsilon(file_path_Cu_bucklig_v1,
                                                                                               21.8, C_Cu_bucklig,
                                                                                               A_Cu_bucklig, test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_bucklig_v1, 21.8, C_Cu_bucklig, A_Cu_bucklig, test_time1)

file_path_Cu_bucklig_v2 = 'koppar_bucklig_v2'
# ganska lågt epsilon jämfört med v1
_, alpha_Cu_bucklig_v2, epsilon_Cu_bucklig_v2, Temp_max_Cu_bucklig_v2 = find_alpha_and_epsilon(file_path_Cu_bucklig_v2,
                                                                                               22.2, C_Cu_bucklig,
                                                                                               A_Cu_bucklig, test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_bucklig_v2, 22.2, C_Cu_bucklig, A_Cu_bucklig, test_time1)

file_path_Cu_repad_v1 = 'koppar_repad_misstänkt_2'
# helt klart dålig platta
_, alpha_Cu_repad_v1, epsilon_Cu_repad_v1, Temp_max_Cu_repad_v1 = find_alpha_and_epsilon(file_path_Cu_repad_v1, 22.2,
                                                                                         C_Cu_repad, A_Cu_repad,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_repad_v1, 22.2, C_Cu_repad, A_Cu_repad, test_time1)

file_path_Cu_repad_v2 = 'koppar_repad_misstänkt_v2'
# helt klart dålig platta
_, alpha_Cu_repad_v2, epsilon_Cu_repad_v2, Temp_max_Cu_repad_v2 = find_alpha_and_epsilon(file_path_Cu_repad_v2, 21.9,
                                                                                         C_Cu_repad, A_Cu_repad,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_repad_v2, 21.9, C_Cu_repad, A_Cu_repad, test_time1)

'''grundupg'''

file_path_Cu_svart_v1 = 'koppar_svart'
_, alpha_Cu_svart_v1, epsilon_Cu_svart_v1, Temp_max_Cu_svart_v1 = find_alpha_and_epsilon(file_path_Cu_svart_v1, 22,
                                                                                         C_Cu_svart, A_Cu_svart,
                                                                                         test_time2)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_svart_v1, 22, C_Cu_svart, A_Cu_svart, test_time2)

file_path_Cu_svart_v2 = 'koppar_svart_v2'
_, alpha_Cu_svart_v2, epsilon_Cu_svart_v2, Temp_max_Cu_svart_v2 = find_alpha_and_epsilon(file_path_Cu_svart_v2, 22.0,
                                                                                         C_Cu_svart, A_Cu_svart,
                                                                                         test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_svart_v2, 22.0, C_Cu_svart, A_Cu_svart, test_time1)

file_path_Cu_vit_v1 = 'koppar_vit'
_, alpha_Cu_vit_v1, epsilon_Cu_vit_v1, Temp_max_Cu_vit_v1 = find_alpha_and_epsilon(file_path_Cu_vit_v1, 21.9, C_Cu_vit,
                                                                                   A_Cu_vit, test_time1)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_vit_v1, 21.9, C_Cu_vit, A_Cu_vit, test_time1)

file_path_Cu_vit_v2 = 'koppar_vit_v2'
_, alpha_Cu_vit_v2, epsilon_Cu_vit_v2, Temp_max_Cu_vit_v2 = find_alpha_and_epsilon(file_path_Cu_vit_v2, 22.2, C_Cu_vit,
                                                                                   A_Cu_vit, test_time2)
print(_)
plot_find_alpha_and_epsilon(file_path_Cu_vit_v2, 22.2, C_Cu_vit, A_Cu_vit, test_time2)

alpha_Al_blank = 0.5 * (alpha_Al_blank_v1 + alpha_Al_blank_v2)
alpha_Al_repad = 0.5 * (alpha_Al_repad_v1 + alpha_Al_repad_v2)
alpha_Al_bucklig = 0.5 * (alpha_Al_bucklig_v1 + alpha_Al_bucklig_v2)
alpha_Cu_blank = 0.5 * (alpha_Cu_blank_v1 + alpha_Cu_blank_v2)
alpha_Cu_repad = 0.5 * (alpha_Cu_repad_v1 + alpha_Cu_repad_v2)
alpha_CU_bucklig = 0.5 * (alpha_Cu_bucklig_v1 + alpha_Cu_bucklig_v2)

epsilon_Al_blank = 0.5 * (epsilon_Al_blank_v1 + epsilon_Al_blank_v2)
epsilon_Al_repad = 0.5 * (epsilon_Al_repad_v1 + alpha_Al_repad_v2)
epsilon_Al_bucklig = 0.5 * (epsilon_Al_bucklig_v1 + epsilon_Al_bucklig_v2)
epsilon_Cu_blank = 0.5 * (epsilon_Cu_blank_v1 + epsilon_Cu_blank_v2)
epsilon_Cu_repad = 0.5 * (epsilon_Cu_repad_v1 + epsilon_Cu_repad_v2)
epsilon_CU_bucklig = 0.5 * (epsilon_Cu_bucklig_v1 + epsilon_Cu_bucklig_v2)

"""
plt.figure(figsize=(10, 8))
plt.plot([1, 2, 3], [alpha_Al_repad, alpha_Al_bucklig, alpha_Al_blank])
plt.plot([1, 2, 3], [alpha_Cu_repad, alpha_CU_bucklig, alpha_Cu_blank])
plt.scatter(1, alpha_Al_repad, label='Al_repad')
plt.scatter(2, alpha_Al_bucklig, label='Al_bucklig')
plt.scatter(3, alpha_Al_blank, label='Al_blank')
plt.scatter(1, alpha_Cu_repad, label='Cu_repad')
plt.scatter(2, alpha_CU_bucklig, label='CU_bucklig')
plt.scatter(3, alpha_Cu_blank, label='Cu_blank')
plt.legend()
plt.show()

plt.figure(figsize=(10, 8))
plt.plot([1, 2, 3], [epsilon_Al_repad, epsilon_Al_bucklig, epsilon_Al_blank])
plt.plot([1, 2, 3], [epsilon_Cu_repad, epsilon_CU_bucklig, epsilon_Cu_blank])
plt.scatter(1, epsilon_Al_repad, label='Al_repad')
plt.scatter(2, epsilon_Al_bucklig, label='Al_bucklig')
plt.scatter(3, epsilon_Al_blank, label='Al_blank')
plt.scatter(1, epsilon_Cu_repad, label='Cu_repad')
plt.scatter(2, epsilon_CU_bucklig, label='CU_bucklig')
plt.scatter(3, epsilon_Cu_blank, label='Cu_blank')
plt.legend()
plt.show()
"""
alpha_list = [
    alpha_Al_blank,
    alpha_Al_repad,
    alpha_Al_bucklig,
    alpha_Cu_blank,
    alpha_Cu_repad,
    alpha_CU_bucklig]
print(list((str(e), e) for e in alpha_list))

alpha_dict = {
    'alpha_Al_blank': alpha_Al_blank,
    'alpha_Al_repad': alpha_Al_repad,
    'alpha_Al_bucklig': alpha_Al_bucklig,
    'alpha_Cu_blank': alpha_Cu_blank,
    'alpha_Cu_repad': alpha_Cu_repad,
    'alpha_CU_bucklig': alpha_CU_bucklig
}
for key, value in alpha_dict.items():
    print(f"{key}: {value}")

epsilon_list = [
    epsilon_Al_blank,
    epsilon_Al_repad,
    epsilon_Al_bucklig,
    epsilon_Cu_blank,
    epsilon_Cu_repad,
    epsilon_CU_bucklig]

epsilon_dict = {
    'epsilon_Al_blank': epsilon_Al_blank,
    'epsilon_Al_repad': epsilon_Al_repad,
    'epsilon_Al_bucklig': epsilon_Al_bucklig,
    'epsilon_Cu_blank': epsilon_Cu_blank,
    'epsilon_Cu_repad': epsilon_Cu_repad,
    'epsilon_CU_bucklig': epsilon_CU_bucklig
}

for key, value in epsilon_dict.items():
    print(f"{key}: {value}")
