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
    return Kelvin(t_90)


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
P_c = 0
derivative_time = 50  # index, not sec


class termo():
    def __init__(self, file_path, T_o, C, A, start_index_heat, d_e):
        """
        :param file_path:           file path for data
        :param T_o:                 room temperature
        :param C:                   heat capacity
        :param A:                   area of plate
        :param start_index_heat:    starting point for heat derivative
        :param d_e:                 thickness of plate
        """
        self.file_path = file_path
        self.T_o = T_o
        self.C = C
        self.A = A
        self.start_index_heat = start_index_heat
        self.d_e = d_e

        data = pd.read_csv(self.file_path, header=None, delimiter='\t')

        Time_str = data.iloc[:, 0].astype(str).to_numpy()
        V_MEAS_str = data.iloc[:, 1].astype(str).to_numpy()

        Time_data = [float(t.replace(',', '.')) for t in Time_str]
        self.Time = list(map(lambda t: timedata2time(t, Time_data), Time_data))

        V_MEAS = [float(v.replace(',', '.')) for v in V_MEAS_str]
        self.Temp = list(map(lambda v: volt2temp(v, self.T_o), V_MEAS))

        self.peak_index = np.argmax(self.Temp)

        end_index_heat = self.start_index_heat + derivative_time
        start_index_cool = self.peak_index
        end_index_cool = self.peak_index + derivative_time

        timestamp_heat = 0  # sec, to determine value of alpha
        timestamp_cool = self.peak_index

        A_e = 4 * np.sqrt(self.A) * self.d_e
        A_tot = 2 * self.A + A_e

        """
            absorption
        """
        self.Time_interval_heat = self.Time[self.start_index_heat:end_index_heat + 1]
        self.Temp_interval_heat = self.Temp[self.start_index_heat:end_index_heat + 1]

        coeff_heat = np.polyfit(self.Time_interval_heat, self.Temp_interval_heat, deg=degree)

        self.fitted_poly_heat = np.poly1d(coeff_heat)
        self.derivative_poly_heat = np.polyder(self.fitted_poly_heat)
        # print('\ncoefficients heating: ', coeff_heat)

        self.alpha = (C / (self.A * E_s)) * self.derivative_poly_heat(timestamp_heat)

        """
            emission
        """
        self.Time_interval_cool = self.Time[start_index_cool:end_index_cool + 1]
        self.Temp_interval_cool = self.Temp[start_index_cool:end_index_cool + 1]

        coeff_cool = np.polyfit(self.Time_interval_cool, self.Temp_interval_cool, deg=degree)

        self.fitted_poly_cool = np.poly1d(coeff_cool)
        self.derivative_poly_cool = np.polyder(self.fitted_poly_cool)

        # epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
        #             (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4))) -
        #            delta_e - P_c / (2 * A * sigma * (fitted_poly_cool(timestamp_cool) ** 4 - Kelvin(T_o) ** 4)))
        # epsilon = (((- C * derivative_poly_cool(timestamp_cool)) /
        #            (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4))) -
        #           delta_e - P_c / (2 * A * sigma * (Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4)))
        self.epsilon = (((- C * self.derivative_poly_cool(timestamp_cool)) /
                         (A_tot * sigma * (self.Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4))) - P_c / (
                                2 * A * sigma * (self.Time[timestamp_cool] ** 4 - Kelvin(T_o) ** 4)))

    def plot(self):
        """
        plotting
        """
        fig = plt.figure(figsize=(10, 8))
        # Plot the original data
        plt.scatter(self.Time, self.Temp, label='Ursprungsdata', color='grey')

        # Plot the fitted polynomial curve
        plt.plot(self.Time_interval_heat, self.fitted_poly_heat(self.Time_interval_heat), color='red',
                 label='Anpassad värmningskurva',
                 linewidth=5.0)
        plt.plot(self.Time_interval_cool, self.fitted_poly_cool(self.Time_interval_cool), color='blue',
                 label='Anpassad avkylningskurva',
                 linewidth=5.0)

        plt.xlabel('Tid (sek)', fontsize=25)
        plt.ylabel('Temperatur (K)', fontsize=25)
        plt.title(f'Poly-fit av temperatur mot tid ({self.file_path})', fontsize=25)
        # plt.title(f'Poly-fit av temperatur mot tid (Koppar, svart)', fontsize=25)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend(fontsize="20")
        plt.grid(True)
        plt.show()

    def find(self):
        return f'\n*********\n{str(self.file_path)}\n*********\nmaxtemp: {self.Temp[self.peak_index]}\n\nalpha: {self.alpha}\nderivata heat: {self.derivative_poly_heat}\n\nepsilon: {self.epsilon}\nderivata cool: {self.derivative_poly_cool}', self.alpha, self.epsilon, \
            self.Temp[self.peak_index]
