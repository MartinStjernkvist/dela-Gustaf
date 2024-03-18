import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'combined_data.txt'
data = pd.read_csv(file_path, header=None, delimiter='\t')

GaAs_final_col1_baseline_nm = data.iloc[:, 0].astype(str).to_numpy()
GaAs_final_col2_baseline_T = data.iloc[:, 1].astype(str).to_numpy()
GaAs_final_col3_meas_nm = data.iloc[:, 2].astype(str).to_numpy()
GaAs_final_col4_meas_T = data.iloc[:, 3].astype(str).to_numpy()

plt.figure(figsize=(10, 8))
    # Plot the original data

# Plot the fitted polynomial curve
plt.plot(GaAs_final_col1_baseline_nm, GaAs_final_col2_baseline_T, color='red', linewidth=5.0)
plt.plot(GaAs_final_col3_meas_nm, GaAs_final_col4_meas_T, color='blue', linewidth=5.0)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission (%)')
plt.legend()
plt.grid(True)
plt.show()