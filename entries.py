from pymatgen.ext.matproj import MPRester
from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.analysis.phase_diagram import PhaseDiagram
from pymatgen.analysis.phase_diagram import PDPlotter
from pymatgen.entries.computed_entries import ComputedEntry


# Assimilate VASP calculations into ComputedEntry object. Let's assume that
# the calculations are for a series of new LixFeyOz phases that we want to
# know the phase stability.
#drone = VaspToComputedEntryDrone()
#queen = BorgQueen(drone, rootpath=".")
#entries = queen.get_data()



#print("Entries", entries)
entrada2 = [ComputedEntry("Li16Sn4S16", -150.73334384, -9.5)]



#print("Entrada 2", entrada2)

#print(type(entrada2))
#entrada2.as_dict()



# Obtain all existing Li-Fe-O phases using the Materials Project REST API
with MPRester("Fvlb5EsNq71JxDy3") as m:
    mp_entries = m.get_entries_in_chemsys(["Li", "Sn", "S"])

# Combined entry from calculated run with Materials Project entries

#entrada.extend(mp_entries)

#print(mp_entries)
#print(type(entrada))


# Process entries using the MaterialsProjectCompatibility
compat = MaterialsProjectCompatibility()
mp_entries = compat.process_entries(mp_entries)

entrada2.extend(mp_entries)

# Generate and plot Li-Fe-O phase diagram
pd = PhaseDiagram(entrada2)
plotter = PDPlotter(pd)
plotter.show()