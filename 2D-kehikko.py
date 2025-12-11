
from Pynite.FEModel3D import FEModel3D
import os
import matplotlib
# Use non-GUI backend so the script can run in headless environments
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Luo uusi FEM-malli
model = FEModel3D()

# Lisää solmut (x, y, z)
model.add_node('N1', 0, 0, 0)
model.add_node('N2', 6, 0, 0)
model.add_node('N3', 6, 4, 0)
model.add_node('N4', 0, 4, 0)

# Lisää materiaalit ja poikkileikkaukset (Pynite API)
E = 210e6      # Young's modulus
G = 81e6       # Shear modulus
Iy = 8.1e-6    # m4
Iz = 8.1e-6    # m4
J = 1.6e-5     # m4
A = 0.02       # m2

model.add_material('steel', E, G, 0.3, 7850)
model.add_section('S1', A, Iy, Iz, J)

# Lisää palkit käyttäen materiaalin nimeä ja poikkileikkausta
model.add_member('M1', 'N1', 'N2', 'steel', 'S1')
model.add_member('M2', 'N2', 'N3', 'steel', 'S1')
model.add_member('M3', 'N3', 'N4', 'steel', 'S1')
model.add_member('M4', 'N4', 'N1', 'steel', 'S1')
model.add_member('M5', 'N1', 'N3', 'steel', 'S1')

# Lisää tuennat (kiinnitetään N1 ja N2)
model.def_support('N1', True, True, True, True, True, True)
model.def_support('N2', True, True, True, True, True, True)

# Lisää kuorma (esim. pystysuora pistekuorma solmuun N3)
model.add_node_load('N3', 'FY', -100)  # -100 kN alas

# Suorita analyysi
model.analyze()

# Tulosta siirtymät
def _first_disp(val):
    """Return a numeric displacement from value which may be a float or a dict of load-case values."""
    if isinstance(val, dict):
        # Try common keys then fall back to first value
        for k in ('Combo 1', 'Case 1', 'combo 1', 'case 1'):
            if k in val:
                return val[k]
        # fallback
        return next(iter(val.values()))
    return val

for node_name in ['N1', 'N2', 'N3', 'N4']:
    node = model.nodes[node_name]
    dx = _first_disp(node.DX)
    dy = _first_disp(node.DY)
    print(f"Solmu {node_name}: dx = {dx:.6f} m, dy = {dy:.6f} m")

# Piirrä muodonmuutos (skaalattuna)
x = [model.nodes[n].X for n in ['N1', 'N2', 'N3', 'N4', 'N1']]
y = [model.nodes[n].Y for n in ['N1', 'N2', 'N3', 'N4', 'N1']]
dx = [_first_disp(model.nodes[n].DX)*100 for n in ['N1', 'N2', 'N3', 'N4', 'N1']]
dy = [_first_disp(model.nodes[n].DY)*100 for n in ['N1', 'N2', 'N3', 'N4', 'N1']]

plt.plot(x, y, label='Alkuperäinen')
plt.plot([x[i]+dx[i] for i in range(5)], [y[i]+dy[i] for i in range(5)], label='Muodonmuutos (x100)')
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Kehikon FEM-analyysi')
# Save figure next to the script using a non-GUI backend
output_path = os.path.join(os.path.dirname(__file__), '2D-kehikko.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Figure saved to: {output_path}")
