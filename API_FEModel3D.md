# FEModel3D API Reference

This document lists public methods of the `FEModel3D` class from the installed `Pynite` package (extracted from the installed package in the project's virtualenv).

> Class: `FEModel3D`

A 3D finite element model object. This object has methods and dictionaries to create, store, and retrieve results from a finite element model.

## Public Methods (signature + short description)

- `D(self, combo_name='Combo 1') -> NDArray[float64]` : Returns the global displacement vector for the model for the specified load combination.

- `FER(self, combo_name='Combo 1') -> NDArray[float64]` : Assembles and returns the global fixed end reaction vector for the given load combo.

- `K(self, combo_name='Combo 1', log=False, check_stability=True, sparse=True)` : Returns the model's global stiffness matrix (sparse by default).

- `Kg(self, combo_name='Combo 1', log=False, sparse=True, first_step=True)` : Returns the global geometric stiffness matrix.

- `Km(self, combo_name='Combo 1', push_combo='Push', step_num=1, log=False, sparse=True)` : Calculates the global plastic reduction matrix for nonlinear inelastic analysis.

- `P(self, combo_name='Combo 1') -> NDArray[float64]` : Assembles and returns the global nodal force vector for the specified combo.

- `add_annulus_mesh(self, name, mesh_size, outer_radius, inner_radius, thickness, material_name, ...) -> str` : Add an annulus mesh of quads.

- `add_cylinder_mesh(self, name, mesh_size, radius, height, thickness, material_name, ...) -> str` : Adds a cylindrical mesh of elements.

- `add_frustrum_mesh(self, name, mesh_size, large_radius, small_radius, height, thickness, material_name, ...) -> str` : Adds a frustrum (truncated cone) mesh.

- `add_load_combo(self, name, factors: dict, combo_tags: list|None=None)` : Adds a load combination to the model (factors is a dict mapping case names to factors).

- `add_mat_foundation(self, name, mesh_size, length_X, length_Z, thickness, material_name, ks, origin=[0,0,0])` : Adds a material foundation mesh (helper).

- `add_material(self, name: str, E: float, G: float, nu: float, rho: float, fy: float|None=None) -> str` : Adds a material to the model.

- `add_member(self, name: str, i_node: str, j_node: str, material_name: str, section_name: str, rotation: float=0.0, tension_only: bool=False, comp_only: bool=False) -> str` : Adds a physical member to the model.

- `add_member_dist_load(self, member_name: str, direction: str, w1: float, w2: float, x1: float|None=None, x2: float|None=None, case: str='Case 1')` : Adds a distributed load on a member.

- `add_member_pt_load(self, member_name: str, direction: str, P: float, x: float, case: str='Case 1')` : Adds a point load to a member.

- `add_member_self_weight(self, global_direction: str, factor: float, case: str='Case 1')` : Adds self weight to all members.

- `add_node(self, name: str, X: float, Y: float, Z: float) -> str` : Adds a new node with coordinates.

- `add_node_load(self, node_name: str, direction: str, P: float, case: str='Case 1')` : Adds a nodal load.

- `add_plate(self, name: str, i_node: str, j_node: str, m_node: str, n_node: str, t: float, material_name: str, kx_mod: float=1.0, ky_mod: float=1.0) -> str` : Adds a rectangular plate element.

- `add_plate_surface_pressure(self, plate_name: str, pressure: float, case: str='Case 1')` : Adds surface pressure to a rectangular plate.

- `add_quad(self, name: str, i_node: str, j_node: str, m_node: str, n_node: str, t: float, material_name: str, kx_mod: float=1.0, ky_mod: float=1.0) -> str` : Adds a quadrilateral element.

- `add_quad_surface_pressure(self, quad_name: str, pressure: float, case: str='Case 1')` : Adds surface pressure to a quad.

- `add_rectangle_mesh(self, name: str, mesh_size: float, width: float, height: float, thickness: float, material_name: str, ...) -> str` : Adds a rectangular mesh of quads.

- `add_section(self, name: str, A: float, Iy: float, Iz: float, J: float) -> str` : Adds a cross-section definition.

- `add_shear_wall(self, name: str, mesh_size: float, length: float, height: float, thickness: float, material_name: str, ky_mod: float=0.35, plane='XY', origin=[0,0,0])` : Adds a meshed shear wall helper.

- `add_spring(self, name: str, i_node: str, j_node: str, ks: float, tension_only: bool=False, comp_only: bool=False) -> str` : Adds a spring between nodes.

- `add_steel_section(self, name: str, A: float, Iy: float, Iz: float, J: float, Zy: float, Zz: float, material_name: str) -> str` : Adds a steel section (with section moduli).

- `analyze(self, log=False, check_stability=True, check_statics=False, max_iter=30, sparse=True, combo_tags=None, spring_tolerance=0, member_tolerance=0, num_steps=1)` : Performs first-order elastic analysis (handles tension/compression-only behavior and stepping).

- `analyze_PDelta(self, log=False, check_stability=True, max_iter=30, sparse=True, combo_tags=None)` : Performs P-Delta (second-order) analysis.

- `analyze_linear(self, log=False, check_stability=True, check_statics=False, sparse=True, combo_tags=None)` : Performs first-order static analysis (faster; no iterations per load case).

- `def_node_disp(self, node_name: str, direction: str, magnitude: float)` : Define enforced nodal displacement.

- `def_releases(self, member_name: str, Dxi: bool=False, Dyi: bool=False, Dzi: bool=False, Rxi: bool=False, Ryi: bool=False, Rzi: bool=False, Dxj: bool=False, Dyj: bool=False, Dzj: bool=False, Rxj: bool=False, Ryj: bool=False, Rzj: bool=False)` : Define member end releases.

- `def_support(self, node_name: str, support_DX: bool=False, support_DY: bool=False, support_DZ: bool=False, support_RX: bool=False, support_RY: bool=False, support_RZ: bool=False)` : Define nodal supports.

- `def_support_spring(self, node_name: str, dof: str, stiffness: float, direction: str|None=None)` : Define a spring support at a node (dof: 'DX','DY','DZ','RX','RY','RZ').

- `delete_loads(self)` : Delete all loads and derived results.

- `delete_member(self, member_name: str)` : Delete a member and its associated loads.

- `delete_node(self, node_name: str)` : Delete a node and related loads/elements.

- `delete_spring(self, spring_name: str)` : Delete a spring by name.

- `merge_duplicate_nodes(self, tolerance: float=0.001) -> list` : Remove duplicate nodes by spatial tolerance and return removed names.

- `orphaned_nodes(self)` : Return list of node names not attached to any elements.

- `rename(self)` : Renames all nodes and elements in the model (utility).

- `unique_name(self, dictionary, prefix)` : Returns next available unique name for a dictionary of objects.


## Notes
 - The `FEModel3D` instance exposes data containers such as `nodes` and `members` (dictionaries) holding `Node3D` and `Member3D` objects.
 - Methods accept load-case strings such as `'Case 1'` and combination names such as `'Combo 1'`.
 - See the installed package files (e.g. `Pynite/FEModel3D.py`, `Pynite/Analysis.py`) for implementation details and more helper utilities.

## Expanded details & examples

The sections below expand method parameter details and show short, copy-pasteable examples.

### Materials and sections

- `add_material(name, E, G, nu, rho, fy=None)` — create a material.
- `add_section(name, A, Iy, Iz, J)` — create a cross-section definition used by members.

Example:

```python
m.add_material('steel', E=210e9, G=81e9, nu=0.3, rho=7850)
m.add_section('S1', A=0.02, Iy=8.1e-6, Iz=8.1e-6, J=1.6e-5)
```

### Nodes and members

- `add_node(name, X, Y, Z)` — adds a node at coordinates.
- `add_member(name, i_node, j_node, material_name, section_name, rotation=0.0, tension_only=False, comp_only=False)` — adds a member between two nodes using a named material & section.

Example (frame geometry + members):

```python
m.add_node('N1', 0, 0, 0)
m.add_node('N2', 6, 0, 0)
m.add_member('M1', 'N1', 'N2', 'steel', 'S1')
```

### Supports and loads

- `def_support(node_name, support_DX=False, support_DY=False, support_DZ=False, support_RX=False, support_RY=False, support_RZ=False)` — boolean flags restrain DOFs when True.
- `add_node_load(node_name, direction, P, case='Case 1')` — direction: `'FX','FY','FZ','MX','MY','MZ'`.
- `add_member_pt_load(member_name, direction, P, x, case='Case 1')` — apply a point load to a member at local x.

Example:

```python
m.def_support('N1', True, True, True, True, True, True)  # fully fixed
m.add_node_load('N3', 'FY', -100.0, case='Case 1')
```

### Analysis and results

- `analyze(...)` — general analysis (iterative for tension-only behavior). Key args: `log`, `check_stability`, `check_statics`, `max_iter`, `sparse`, `num_steps`.
- `analyze_linear(...)` — faster single-pass linear solve.
- `analyze_PDelta(...)` — second-order geometric effects.
- `D(combo_name='Combo 1')` — returns global displacement vector.
- `P(combo_name='Combo 1')` — global nodal force vector.
- `K(combo_name='Combo 1', ...)` — global stiffness matrix.

Reading node displacements:

```python
m.analyze()
for name, node in m.nodes.items():
	# Node DX/DY may be a float or a dict keyed by load-case/combination
	dx = node.DX if not isinstance(node.DX, dict) else next(iter(node.DX.values()))
	dy = node.DY if not isinstance(node.DY, dict) else next(iter(node.DY.values()))
	print(name, dx, dy)
```

### Reporting

Use `Pynite.Reporting.create_report` to generate HTML or PDF reports. If `format='pdf'` the helper uses `pdfkit` + `wkhtmltopdf` (ensure wkhtmltopdf is installed or provide path via `get_wkhtmltopdf_path`).

Example:

```python
from Pynite.Reporting import create_report
create_report(m, output_filepath='my_report.html', format='html', log=True)
```

---

Generated from installed Pynite source files (`FEModel3D.py`, `Reporting.py`, `Analysis.py`) on 2025-12-11.

---

Generated from the `Pynite` package installed in the project's virtualenv on 2025-12-11.
