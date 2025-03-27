import numpy as np

class Very_Simple_Climate_Model():
    """Simple climate model taken from https://scied.ucar.edu/activity/very-simple-climate-model-activity"""
    def __init__(self, config:str) -> None:
        self.temperature = config['initial_temperature']
        self.initial_CO2_concentration = config['initial_CO2_concentration']
        self.CO2_concentration = config['initial_CO2_concentration']
        self.annual_CO2_contribution = config['annual_CO2_contribution']
        self.climate_sensitivity = config['climate_sensitivity']
        self.time = 0.0
        self.time_step = config['time_step']

    def update_model_state(self, time_step):
        self.CO2_concentration = self.CO2_concentration + self.annual_CO2_contribution * time_step
        self.temperature = self.temperature + self.climate_sensitivity * np.log(self.CO2_concentration/self.initial_CO2_concentration)
        self.time += time_step

    def get_time(self):
        return self.time