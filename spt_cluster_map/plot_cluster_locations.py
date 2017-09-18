import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from skymap import SurveySkymap

def main():
    ra, dec = np.loadtxt('cluster_RADEC.txt', unpack=True) 
    m = SurveySkymap()
    m.draw_des()
    m.draw_hpxbin(ra, dec)
    plt.savefig('cluster_map.png')


if __name__ == "__main__":
    main()
