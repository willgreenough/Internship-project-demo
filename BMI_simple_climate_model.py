

class BMI_Simple_climate_model(Bmi):
    """Solve the heat equation for a 2D plate."""

    _name = "The 2D Heat Equation"
    _input_var_names = ("plate_surface__temperature",)
    _output_var_names = ("plate_surface__temperature",)

    def __init__(self) -> None:
        """Create a BmiHeat model that is ready for initialization."""
        # self._model: Heat | None = None
        self._model: Heat
        self._values: dict[str, NDArray[Any]] = {}
        self._var_units: dict[str, str] = {}
        self._var_loc: dict[str, str] = {}
        self._grids: dict[int, list[str]] = {}
        self._grid_type: dict[int, str] = {}

        self._start_time = 0.0
        self._end_time = float(np.finfo("d").max)
        self._time_units = "s"

    def initialize(self, filename: str | None = None) -> None:
        """Initialize the Heat model.

        Parameters
        ----------
        filename : str, optional
            Path to name of input file.
        """
        if filename is None:
            self._model = Heat()
        elif isinstance(filename, str):
            with open(filename) as file_obj:
                self._model = Heat.from_file_like(file_obj)
        else:
            self._model = Heat.from_file_like(filename)

        self._values = {"plate_surface__temperature": self._model.temperature}
        self._var_units = {"plate_surface__temperature": "K"}
        self._var_loc = {"plate_surface__temperature": "node"}
        self._grids = {0: ["plate_surface__temperature"]}
        self._grid_type = {0: "uniform_rectilinear"}

    def update(self) -> None:
        """Advance model by one time step."""
        self._model.advance_in_time()