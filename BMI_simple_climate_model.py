from bmipy import Bmi
import numpy as np
from numpy.typing import NDArray, Any
from simple_climate_model import The_Very_Simple_climate_model

class BMI_Simple_climate_model(Bmi):
    """solve the simple climate model taken from https://scied.ucar.edu/activity/very-simple-climate-model-activity. It follows the structure given in the BMI documentation."""

    _name = "The Simple climate model"
    _input_var_names = ("plate_surface__temperature",)
    _output_var_names = ("plate_surface__temperature",)

    def __init__(self) -> None:
        """Create a BmiHeat model that is ready for initialization."""
        # self._model: Heat | None = None
        self._model: The_Very_Simple_climate_model
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
                self._model = The_Very_Simple_climate_model(file_obj)

        self._values = {"temperature": self._model.temperature, "C02_concentration": self._model.CO2_concentration}
        self._var_units = {"temperature": "Celcius", "C02_concentration": "ppm"}
        self._var_loc = {"temperature": "node", "C02_concentration": "node"}
        self._grids = {0: ["temperature"], 1: ["C02_concentration"]}
        self._grid_type = {0: "scalar", 1: "scalar"}

    def update(self) -> None:
        """Advance model by one time step."""
        self._model.update_model_state()
    
    def finalize(self) -> None:
        """Finalize model."""
        del self._model

    def get_var_grid(self, name: str) -> int:
        """return the grid id for a given variable"""
        for grid_id, var_names in self._grids.items():
            if name in var_names:
                return grid_id
        raise ValueError(f"Variable {name} not found.")

    # The rest of the BMI functions are omitted for brevity. 