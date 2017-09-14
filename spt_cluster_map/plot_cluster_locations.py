import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp

def bin_data(pixels,NPIX):
    binned_pixels = np.zeros(NPIX, dtype=float)
    
    for i in pixels:
        binned_pixels[i] = binned_pixels[i]+1.0

    return binned_pixels

def main():
    # Load in the data
    ra, dec = np.loadtxt('cluster_RADEC.txt', unpack=True) 

    # Set up the healpix map and plot the pixels
    NSIDE = 64
    NPIX = hp.pixelfunc.nside2npix(NSIDE)

    # Convert RA and DEC to pixel number
    pixels = hp.pixelfunc.ang2pix(NSIDE, ra, dec, lonlat=True)

    # Count the number of objects in each pixel
    density_map = bin_data(pixels, NPIX)

    # Plot the map of N per pixel
    hp.mollview(density_map, title='Cluster Map')#, max=0.0005)
    plt.savefig('cluster_map.png')
    plt.clf()



if __name__ == "__main__":
    main()
