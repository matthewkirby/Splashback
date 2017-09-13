"""
Read in the cluste catalog and save important columns
"""

import fitsio
import numpy as np

file_path = "2500d_cluster_sample_fiducial_cosmology.fits"

data, header = fitsio.read(file_path, header=True)
RA = data['RA']
DEC = data['DEC']

np.savetxt("cluster_RADEC.txt", np.array([RA, DEC]).T, header="RA DEC")
