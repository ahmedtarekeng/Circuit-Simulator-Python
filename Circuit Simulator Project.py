import tkinter as tk										# imported libraries that are needed
from tkinter import ttk, messagebox, PhotoImage				# tkinter needed for GUI, matplot needed to plot V, I, and t
import matplotlib.pyplot as plt								# numpy needed for mathematical equations
import numpy as np

class CircuitSimulator:
    def __init__(self):
        self.main_window = tk.Tk()  						# Create the main application window
        self.main_window.title("Circuit Simulator") 		# Add title to GUI window that pops up
        self.create_widgets()								# Starts the create_widgets function that sets up the GUI
        self.show_image()
        
    def create_widgets(self):
        # Adds a greeting label
        ttk.Label(self.main_window, text="Welcome to our Circuit Simulator!, 	Team 19  ✪ ω ✪ ").grid(column=0, row=0, padx=10, pady=10)

        # Circuit topology selection with label and combobox that reads only, adjusting both widgets to the same first row.
        ttk.Label(self.main_window, text="Select Circuit Topology:").grid(column=0, row=1, padx=10, pady=5)
        self.topology = ttk.Combobox(self.main_window, values=["Series RC Circuit", "Series RL Circuit", "Parallel RC Circuit",
                                                               "Parallel RL Circuit", "Series Resistor-Diode Circuit",
                                                               "Series RLC Circuit", "Parallel RLC Circuit"], state= 'readonly')
        self.topology.grid(column=1, row=1, padx=10, pady=5)
        
        # Upon choice of topology, show_image function is called
        self.topology.bind("<<ComboboxSelected>>", lambda event: self.show_image())
        
        # Label and entry box that asks the user for the Resistor value.
        ttk.Label(self.main_window, text="Resistor (R) [Ω]:").grid(column=0, row=2, padx=10, pady=5)
        self.resistor = ttk.Entry(self.main_window)
        self.resistor.grid(column=1, row=2, padx=10, pady=5)

        # Label and entry box that asks the user for the Capacitor value.
        ttk.Label(self.main_window, text="Capacitor (C) [F]:").grid(column=0, row=3, padx=10, pady=5)
        self.capacitor = ttk.Entry(self.main_window)
        self.capacitor.grid(column=1, row=3, padx=10, pady=5)

        # Label and entry box that asks the user for the Inductor value.
        ttk.Label(self.main_window, text="Inductor (L) [H]:").grid(column=0, row=4, padx=10, pady=5)
        self.inductor = ttk.Entry(self.main_window)
        self.inductor.grid(column=1, row=4, padx=10, pady=5)

        # Label and entry box that asks the user for the Peak Voltage value.
        ttk.Label(self.main_window, text="Peak Voltage (Vpeak) [V]:").grid(column=0, row=5, padx=10, pady=5)
        self.peak_voltage = ttk.Entry(self.main_window)
        self.peak_voltage.grid(column=1, row=5, padx=10, pady=5)

        # Label and entry box that asks the user for the circuit's Frequency value.
        ttk.Label(self.main_window, text="Frequency (f) [Hz]:").grid(column=0, row=6, padx=10, pady=5)
        self.frequency = ttk.Entry(self.main_window)
        self.frequency.grid(column=1, row=6, padx=10, pady=5)

        # Label and entry box that asks the user for the diode's saturation current 'Is' value.
        ttk.Label(self.main_window, text="Reverse Saturation Current (Is) [A]:").grid(column=0, row=7, padx=10, pady=5)
        self.is_current = ttk.Entry(self.main_window)
        self.is_current.grid(column=1, row=7, padx=10, pady=5)
        
        # 2 Labels that changes after simulation to show the required results.
        ttk.Label(self.main_window, text="Results: ").grid(column=0, row =8, padx=10, pady=10)
        
        self.result = ttk.Label(self.main_window, text="")
        self.result.grid(column=1, row =8, padx=10, pady=10)                              


        # Image Placeholder
        self.img_label = ttk.Label(self.main_window)
        self.img_label.grid(column=2, row=0, rowspan=7, padx=10, pady=5)
        
        # Simulate Button 
        self.simulate_button = ttk.Button(self.main_window, text="Simulate", command=self.simulate)
        self.simulate_button.grid(column=0, row=9, columnspan=2, padx=10, pady=10)
        
        # Function that shows the toplogy's image upon choice
    def show_image(self):
         topology = self.topology.get()
         img_path = ""
         if topology == "Series RC Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\series_rc.png"
         elif topology == "Series RL Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\series_rl.png"
         elif topology == "Parallel RC Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\parallel_rc.png"
         elif topology == "Parallel RL Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\parallel_rl.png"
         elif topology == "Series Resistor-Diode Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\series_resistor_diode.png"
         elif topology == "Series RLC Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\series_rlc.png"
         elif topology == "Parallel RLC Circuit":
             img_path = "C:\\Users\\ahmed\\Desktop\\Python\\images\\parallel_rlc.png"

         if img_path:
             img = PhotoImage(file=img_path)
             self.img_label.config(image=img)
             self.img_label.image = img
             
    
        # Simulate function that collects data from entry boxes and calls the specified topology function
    def simulate(self):
        try:
            R = float(self.resistor.get())
            C = float(self.capacitor.get())
            L = float(self.inductor.get())
            Vpeak = float(self.peak_voltage.get())
            f = float(self.frequency.get())
            Is = float(self.is_current.get())
            
            topology = self.topology.get()
            if topology == "Series RC Circuit":
                result = self.simulate_series_rc(R, C, Vpeak)
            elif topology == "Series RL Circuit":
                result = self.simulate_series_rl(R, L, Vpeak)
            elif topology == "Parallel RC Circuit":
                result = self.simulate_parallel_rc(R, C, Vpeak, f)
            elif topology == "Parallel RL Circuit":
                result = self.simulate_parallel_rl(R, L, Vpeak, f)
            elif topology == "Series Resistor-Diode Circuit":
                result = self.simulate_series_resistor_diode(R, Vpeak, f, Is)
            elif topology == "Series RLC Circuit":
                result = self.simulate_series_rlc(R, L, C, Vpeak, f)
            else:
                result = self.simulate_parallel_rlc(R, L, C, Vpeak, f)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")
        self.result.config(text=result)
        
        # Function that simulates the Series RC Circuit
    def simulate_series_rc(self, R, C, Vpeak):
        tau = R * C
        t = np.linspace(0, 5 * tau, 1000)
        V = Vpeak *(1- np.exp(-t / tau))
        
        
        plt.figure()
        plt.plot(t, V)
        plt.title("Voltage across Capacitor in Series RC Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        plt.grid()
        plt.show()
        #return (f"Tau is equal to", tau, "Voltage is equal to", V)
        return  f"Tau: {tau}s, Vc(0): {Vpeak}V, Ic(0): {Vpeak / R:.2e}A"
    
        # Function that simulates the series RL Circuit
    def simulate_series_rl(self, R, L, Vpeak): 
        tau = L / R
        t = np.linspace(0, 5 * tau, 1000)
        I = (Vpeak / R) * (1 - np.exp(-t / tau))
        
        plt.figure()
        plt.plot(t, I)
        plt.title("Current in Inductor in Series RL Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Current [A]")
        plt.grid()
        plt.show()
        
        return f"Tau: {tau:.2e}s, Ir(0): {Vpeak / R:.2e}A, Vl(0): {Vpeak}V"
    
        # Function that simulates the Parallel RC Circuit
    def simulate_parallel_rc(self, R, C, Vpeak, f):
        tau = R * C
        omega = 2 * np.pi * f
        t = np.linspace(0, 5 * tau, 1000)
        V = Vpeak * np.sin(omega*t)
        Xc = 1/(omega*C)
        impedence = (R*Xc)/(R+Xc)
        I= V/Xc
        plt.figure()
        plt.plot(t, V, label = 'Voltage across capacitor')
        plt.title("Parallel RC Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V]")
        plt.grid()
        plt.legend()
        plt.show()
        return f"Tau: {tau}sec, Vout(0): {V}V, Ic(0): {I:.2e}A, Impedence: {impedence:.2}",

        # Function that simulates the Parallel RL Circuit
    def simulate_parallel_rl(self, R, L, Vpeak, f):
        omega = 2 * np.pi * f
        tau = L / R
        t = np.linspace(0, 5 * tau, 1000)
        V = Vpeak * np.sin(omega*t)
        I = (V / R) * (1 - np.exp(-t / tau))
        Xl = omega * L

        plt.figure()
        plt.plot(t, I, label = "Current across inductor")
        plt.title("Parallel RL Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Current [A]")
        plt.grid()
        plt.legend()
        plt.show()
        return f"Tau: {tau:.2e}s, Ir(0): {Vpeak / R:.2e}A, Vl(0): {Vpeak}V"

        # Function that simulates the Series Resistor-diode Circuit
    def simulate_series_resistor_diode(self, R, Vpeak, f, Is):
        omega = 2 * np.pi * f
        t = np.linspace(0, 2/f, 1000)
        V = Vpeak * np.sin(omega * t)
        I = np.where(V < 0, 0, (V - 0.7) / R)
        Vdiode = np.where ( V < 0, 0, (V-0.7))

        plt.figure()
        plt.plot(t, Vdiode, label='Voltage across Diode')
        plt.plot(t, I, label='Current in Diode')
        plt.title("Series Resistor-Diode Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V] / Current [A]")
        plt.grid()
        plt.legend()
        plt.show()
        return f"Vd(peak): {Vpeak}V, Id(peak): {Is * (np.exp(Vpeak / 0.025) - 1):.2e}A"
 
        # Function that simulates the Series RLC Circuit
    def simulate_series_rlc(self, R, L, C, Vpeak, f):
        omega = 2 * np.pi * f
        t = np.linspace(0, 1/f, 1000)
        V = Vpeak * np.sin(omega * t)
        Xc= 1/(omega*C)
        Xl = omega* L
        Z= np.sqrt(R*R+ pow((Xl-Xc),2))
        I = V/Z
        j = np.sqrt(-1)
        Vr = I * R
        Vl = I * Xl
        Vc = I * Xc

        plt.figure()
        plt.plot(t, Vc, label='Voltage across Capacitor')
        plt.plot(t, Vl, label='Voltage across inductor')
        plt.plot(t, I, label='Current in Circuit')
        plt.title("Series RLC Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V] / Current [A]")
        plt.grid()
        plt.legend()
        plt.show()

        return f"V(0): {Vpeak}V, I(0): {(Vpeak / L):.2e}A"

        # Function that simulates the Parallel RLC Circuit
    def simulate_parallel_rlc(self, R, L, C, Vpeak, f):
        omega = 2 * np.pi * f
        t = np.linspace(0, 1/f, 1000)
        V = Vpeak * np.sin(omega * t)
        Xc= 1/(omega*C)
        Xl = omega* L
        Ic = V/(-Xc)
        Il = V/(Xl)
        Ir = V/ R
        I = Ic + Il + Ir
        
        plt.figure()
        plt.plot(t, V, label='Source Voltage')
        plt.plot(t, I, label='Current in Circuit')
        plt.title("Parallel RLC Circuit")
        plt.xlabel("Time [s]")
        plt.ylabel("Voltage [V] / Current [A]")
        plt.grid()
        plt.legend()
        plt.show()

        return f"V(0): {Vpeak}V, I(0): {(Vpeak / L):.2e}A"

   
        # Function that starts the GUI
    def run(self):
        self.main_window.mainloop()  # Start the Tkinter event loop

# Main application block
if __name__ == "__main__":
    app = CircuitSimulator()  # Create an instance of the class
    app.run()  # Run the application
