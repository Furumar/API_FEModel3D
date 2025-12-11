# API_FEModel3D

Small demo + documentation for using the `Pynite` FEModel3D API.

This repository contains:

- `2D-kehikko.py` — example 2D frame script using the installed `Pynite` API. Saves a plot as `2D-kehikko.png`.
- `verify_install.py` — simple verifier that imports required packages and prints versions.
- `requirements.txt` — pinned dependencies used when the project was prepared.
- `API_FEModel3D.md` — extracted public API and usage examples for `Pynite.FEModel3D`.

Quick start (Windows PowerShell)

1. Create a virtual environment and activate it:

```powershell
cd 'C:\Users\MarcoFuru\OneDrive\Laskentaohjelma Python MF'
C:/Users/MarcoFuru/AppData/Local/Programs/Python/Python314/python.exe -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install requirements:

```powershell
.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Verify imports:

```powershell
.venv\Scripts\python.exe verify_install.py
```

4. Run the example frame script (headless — will save a PNG):

```powershell
.venv\Scripts\python.exe 2D-kehikko.py
# Output image: 2D-kehikko.png
```

Notes

- The example script uses the `Pynite` package API (installed as `Pynite`) and saves the plotted deformation to `2D-kehikko.png` in the project folder.
- `API_FEModel3D.md` contains method signatures, parameter details and short usage examples (including `Reporting.create_report`).

Contributing

Feel free to open issues and pull requests. If you want me to add CI (GitHub Actions) that runs `verify_install.py` on push, tell me and I'll add a workflow.

License

Add a `LICENSE` file if you want to publish this repo publicly with a specific license.
