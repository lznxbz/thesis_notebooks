from lzn.universal import to_path, batch_do
from ase.io import read
import numpy as np



ads_names = ["co", "h2s", "h2o", "nh3"]

def extractEnergy_singe(file_path, file_format):
    """
    Read file and extract energy in eV
    :return float: Energy in eV
    """
    if file_format == "gaussian-out":
        if file_path.stem.split("_")[-1][:3] == "cm-":
            return

    atoms = read(file_path, index=-1, format=file_format)
    return atoms.get_potential_energy()


def parseName_extractEnergy(dir):
    """
    from input directory and extract energy data

    """
    dir = to_path(dir)
    opt_name = dir.name.split("_")[1]

    # determine file type from opt method
    if dir.name.split("_")[-1] == "sp":
        file_suffix, file_format = ".log", "gaussian-out"
    elif opt_name in ["omol25", "r2scan", "matpes"]:
        file_suffix, file_format = ".traj", "traj"
    elif opt_name in ["g16", "svp"]:
        file_suffix, file_format = ".log", "gaussian-out"
    else:
        raise NameError(f"unrecognized directory format opt {opt_name}")

    print(opt_name)
    l_2d = []
    for ads_name in ads_names:
        l_2d.append(batch_do(extractEnergy_singe,
                             in_dir=dir,
                             matching=f"tio12CDa_{ads_name}_site*{file_suffix}",
                             out_dir=False,
                             file_format = file_format
                             )
                    )

    num_str = [str(len(l_2d[i]) )for i in range(len(l_2d))]
    print(f"{"+".join(num_str)} energies extracted")
    return np.array(l_2d)




if __name__ == "__main__":
    tio2_dir = to_path("~/TiO2_organized")
    dir = tio2_dir / "772_svp_opt"
    e_array = parseName_extractEnergy(dir)

    print(e_array[1])