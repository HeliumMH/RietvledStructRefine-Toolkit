from datetime import datetime

# convert site occupancy of guest to uptake
str_name = input("Name of the structure: \n")
mol_per_cell = float(input("Number of molecules per unitcell: \n"))
cell_mass = float(input("Cell formula mass, g/mol: \n"))
uptake = mol_per_cell / (cell_mass / 1000)  # mmol/g

print(f"uptake calculated from refinement result is {uptake} mmol/g")

with open("uptake_log.txt", "a+") as log:
    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log.write(time + "\n")
    log.write("str_name\t\tmol_per_cell\t\tempty_cell_mass\t\tuptake\n")
    log.write(
        str_name + "\t\t" +
        str(mol_per_cell) + "\t\t" +
        str(cell_mass) + "\t\t" +
        str(uptake) + "\n")
    log.write("\n")
    log.close()