import numpy as np

class The_Very_Simple_climate_model():
    """Simple climate model taken from https://scied.ucar.edu/activity/very-simple-climate-model-activity"""
    def __init__(self, config:str) -> None:
        self.temperature = initial_temperature
        self.CO2_concentration = inital_CO2_concentration
        self.annual_CO2_contributon = annual_CO2_contribution
        self.climate_sensitivity = climate_sensitivity
        self.start_time = 0.0
        self.time_step = 

    def update_model_state(self, time_step):
        self.temperature += self.climate_sensitivity * (self.annual_CO2_contributon * time_step - self.CO2_concentration)
        self.CO2_concentration = self.CO2_concentration + self.annual_CO2_contributon * time_step
        self.start_time += time_step