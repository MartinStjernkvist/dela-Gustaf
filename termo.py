import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
inverse coefficients 0-400 *C
"""
d_0 = 0.000000E+00
d_1 = 2.592800E+01
d_2 = -7.602961E-01
d_3 = 4.637791E-02
d_4 = -2.165394E-03
d_5 = 6.048144E-05
d_6 = -7.293422E-07


def temp2volt(T_o):
    V = 0.830 + 0.04 * (T_o - 21)
    return V


def volt2temp(V, T_o):
    V_o = temp2volt(T_o)
    V_MEAS_mV = V * 10 ** 3  # voltage in mV
    V_mV = V_MEAS_mV + V_o
    t_90 = d_0 + d_1 * V_mV + d_2 * V_mV ** 2 + d_3 * V_mV ** 3 + d_4 * V_mV ** 4 + d_5 * V_mV ** 5 + d_6 * V_mV ** 6
    T_o_K = Kelvin(T_o)
    return t_90 + T_o_K


def timedata2time(timestamp, Time_data):
    """
    convert the timestamps (interval always above 0-...) to 0-...
    """
    return timestamp - Time_data[0]


def Kelvin(T):
    return T + 273.15


def C(c, m):
    return c * m


"""
constants
"""
degree = 1
Power = 310 * 10 ** -3  # W
diameter_detector = 19.5 * 10 ** -3  # m
A_detector = np.pi * (diameter_detector / 2) ** 2
E_s = Power / A_detector
sigma = 5.6704 * 10 ** (-8)  # stefan boltzmann constant
delta_e = 0.013
P_c = 0
derivative_time = 50  # index, not sec


def plot_find_alpha_and_epsilon(file_path, T_o, C, A, start_index_heat):
    """
    :param file_path:   file path for data
    :param T_o:         room temperature
    :param c:           specific heat capacity
    :param m:           mass of plate
    :param A:           area of plate
    :param degree:      degree of polynomial
    """

    data = pd.read_csv(file_path, header=None, delimiter='\t')

    Time_str = data.iloc[:, 0].astype(str).to_numpy()
    V_MEAS_str = data.iloc[:, 1].astype(str).to_numpy()

    Time_data = [float(t.replace(',', '.')) for t in Time_str]
    Time = list(map(lambda t: timedata2time(t, Time_data), Time_data))

    V_MEAS = [float(v.replace(',', '.')) for v in V_MEAS_str]
    Temp = list(map(lambda v: volt2temp(v, T_o), V_MEAS))

    peak_index = np.argmax(Temp)

    end_index_heat = start_index_heat + derivative_time
    start_index_cool = peak_index
    end_index_cool = peak_index + derivative_time

    timestamp_heat = 0  # sec, to determine value of alpha
    timestamp_cool = peak_index

    """
    absorption
    """
    Time_interval_heat = Time[start_index_heat:end_index_heat + 1]
    Temp_interval_heat = Temp[start_index_heat:end_index_heat + 1]

    coeff_heat = np.polyfit(Time_interval_heat, Temp_interval_heat, deg=degree)

    fitted_poly_heat = np.poly1d(coeff_heat)
    derivative_poly_heat = np.polyder(fitted_poly_heat)
    # print('\ncoefficients heating: ', coeff_heat)
    # print('\nDerivative Polynomial heating: ', derivative_poly_heat)

    alpha = (C / (A * E_s)) * derivative_poly_heat(timestamp_heat)
    # print(f'alpha: {alpha}')

    """
    emission
    """
    Time_interval_cool = Time[start_index_cool:end_index_cool + 1]
    Temp_interval_cool = Temp[start_index_cool:end_index_cool + 1]

    coeff_cool = np.polyfit(Time_interval_cool, Temp_interval_cool, deg=degree)

    fitted_poly_cool = np.poly1d(coeff_cool)
    derivative_poly_cool = np.polyder(fitted_poly_cool)
    # print('\ncoefficients cooling: ', coeff_cool)
    # print('\nDerivative Polynomial cooling: ', derivative_poly_cool)

    # epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
    #             (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4))) -
    #            delta_e - P_c / (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4)))
    epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
                (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4))) -
               delta_e - P_c / (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4)))
    # print(f'epsilon: {epsilon}')

    """
    plotting
    """
    plt.figure(figsize=(10, 8))
    # Plot the original data
    plt.scatter(Time, Temp, label='Original Data', color='grey')

    # Plot the fitted polynomial curve
    plt.plot(Time_interval_heat, fitted_poly_heat(Time_interval_heat), color='red', label='Fitted Curve', linewidth=5.0)
    plt.plot(Time_interval_cool, fitted_poly_cool(Time_interval_cool), color='blue', label='Fitted Curve',
             linewidth=5.0)

    plt.xlabel('Time (sec)')
    plt.ylabel('Temperature (K)')
    plt.title('Polynomial Fit of Temperature vs. Time')
    plt.legend()
    plt.grid(True)
    plt.show()


def find_alpha_and_epsilon(file_path, T_o, C, A, start_index_heat):
    """
    :param file_path:   file path for data
    :param T_o:         room temperature
    :param c:           specific heat capacity
    :param m:           mass of plate
    :param A:           area of plate
    :param degree:      degree of polynomial
    """

    data = pd.read_csv(file_path, header=None, delimiter='\t')

    Time_str = data.iloc[:, 0].astype(str).to_numpy()
    V_MEAS_str = data.iloc[:, 1].astype(str).to_numpy()

    Time_data = [float(t.replace(',', '.')) for t in Time_str]
    Time = list(map(lambda t: timedata2time(t, Time_data), Time_data))

    V_MEAS = [float(v.replace(',', '.')) for v in V_MEAS_str]
    Temp = list(map(lambda v: volt2temp(v, T_o), V_MEAS))

    peak_index = np.argmax(Temp)

    end_index_heat = start_index_heat + derivative_time
    start_index_cool = peak_index
    end_index_cool = peak_index + derivative_time

    timestamp_heat = 0  # sec, to determine value of alpha
    timestamp_cool = peak_index

    """
    absorption
    """
    Time_interval_heat = Time[start_index_heat:end_index_heat + 1]
    Temp_interval_heat = Temp[start_index_heat:end_index_heat + 1]

    coeff_heat = np.polyfit(Time_interval_heat, Temp_interval_heat, deg=degree)

    fitted_poly_heat = np.poly1d(coeff_heat)
    derivative_poly_heat = np.polyder(fitted_poly_heat)
    # print('\ncoefficients heating: ', coeff_heat)

    alpha = (C / (A * E_s)) * derivative_poly_heat(timestamp_heat)

    """
    emission
    """
    Time_interval_cool = Time[start_index_cool:end_index_cool + 1]
    Temp_interval_cool = Temp[start_index_cool:end_index_cool + 1]

    coeff_cool = np.polyfit(Time_interval_cool, Temp_interval_cool, deg=degree)

    fitted_poly_cool = np.poly1d(coeff_cool)
    derivative_poly_cool = np.polyder(fitted_poly_cool)

    # epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
    #             (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4))) -
    #            delta_e - P_c / (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4)))
    epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
                (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4))) -
               delta_e - P_c / (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4)))

    return f'\n*********\n{str(file_path)}\n*********\nsluttemp: {Temp[-1]}\n\nalpha: {alpha}\nderivata heat: {derivative_poly_heat}\n\nepsilon: {epsilon}\nderivata cool: {derivative_poly_cool}', alpha, epsilon, Temp[-1]
