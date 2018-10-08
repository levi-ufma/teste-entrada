from pymatgen.ext.matproj import MPRester
from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram
from pymatgen.analysis.phase_diagram import PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry

entrada2 = [ComputedEntry("Li16Sn4S16", -150.73334384, -9.5)]

# Obtain all existing Li-Fe-O phases using the Materials Project REST API
with MPRester("Fvlb5EsNq71JxDy3") as m:
    mp_entries = m.get_entries_in_chemsys(["Li", "Sn", "S"])

# Process entries using the MaterialsProjectCompatibility
compat = MaterialsProjectCompatibility()
mp_entries = compat.process_entries(mp_entries)

entrada2.extend(mp_entries)

# Generate and plot Li-Fe-O phase diagram
pd = PhaseDiagram(entrada2)
plotter = PDPlotter(pd)
plotter.show()
