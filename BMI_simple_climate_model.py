from bmipy import Bmi
import numpy as np
from numpy.typing import NDArray
from typing import Any
from very_simple_climate_model import Very_Simple_Climate_Model
import yaml

class BMI_Simple_Climate_Model(): #note, does not inherit from BMI as only a partial implementation
    """solve the simple climate model taken from https://scied.ucar.edu/activity/very-simple-climate-model-activity. It follows the structure given in the BMI documentation."""

    _name = "The Simple climate model"
    _input_var_names = ("climate_sensitivity", "initial_temperature", "inital_CO2_concentration")
    _output_var_names = ("temperature","C02_concentration")

    def __init__(self) -> None:
        """Create a BmiHeat model that is ready for initialization."""
        # self._model: Heat | None = None
        self._model: Very_Simple_Climate_Model
        self._values: dict[str, NDArray[Any]] = {}
        self._var_units: dict[str, str] = {}
        self._var_loc: dict[str, str] = {}
        self._grids: dict[int, list[str]] = {}
        self._grid_type: dict[int, str] = {}

        self._start_time = 0.0
        self._end_time = float(np.finfo("d").max)
        self._time_units = "y"

    def initialize(self, filename: str | None = None) -> None:
        """Initialize the climate model.

        Parameters
        ----------
        filename : str, optional
            Path to name of input file.
        """
        with open(filename) as file_obj:
                file_obj = yaml.safe_load(file_obj)
                self._model = Very_Simple_Climate_Model(file_obj)

        self._values = {"temperature": self._model.temperature, "C02_concentration": self._model.CO2_concentration}
        self._var_units = {"temperature": "Celcius", "C02_concentration": "ppm"}
        self._var_loc = {"temperature": "node", "C02_concentration": "node"}
        self._grids = {0: ["temperature"], 1: ["C02_concentration"]}
        self._grid_type = {0: "scalar", 1: "scalar"}

    def update(self) -> None:
        """Advance model by one time step."""
        self._model.update_model_state(self._model.time_step)
        self._values["temperature"] = self._model.temperature
        self._values["C02_concentration"] = self._model.CO2_concentration
    
    def finalize(self) -> None:
        """Finalize model."""
        del self._model

    #devlop some getter functions
    def get_var_grid(self, name: str) -> int:
        """return the grid id for a given variable"""
        for grid_id, var_names in self._grids.items():
            if name in var_names:
                return grid_id
        raise ValueError(f"Variable {name} not found.")

    def get_current_time(self) -> float:
        """return the current model time"""
        return self._model.get_time()

    def get_time_units(self) -> str:
        """return the model time units"""
        return self._time_units
    
    def get_value(self, name: str, dest: NDArray[Any]) -> None:
        """get the value of a model variable"""
        dest[:] = self._values[name]
    
    # The rest of the BMI functions are omitted for brevity. 

if __name__ == "__main__":
    model = BMI_Simple_Climate_Model()
    model.initialize("config.YAML")
    model.update()
    model.finalize()