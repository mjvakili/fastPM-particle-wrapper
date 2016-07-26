import numpy as np
from bigfile import BigFile, BigData


def wrapper(positions , velocities,  Lbox , cut):

    posx , posy , posz = positions[:,0], positions[:,1], positions[:,2]
    vx , vy , vz = velocities[:,0], velocities[:,1], velocities[:,2]

    out_neg_x = np.where(posx < 0)[0]
    out_pos_x = np.where(posx > Lbox)[0]
    out_neg_y = np.where(posy < 0)[0]
    out_pos_y = np.where(posy > Lbox)[0]
    out_neg_z = np.where(posz < 0)[0]
    out_pos_z = np.where(posz > Lbox)[0]

    posx[out_neg_x] += Lbox
    posx[out_pos_x] -= Lbox
    posy[out_neg_y] += Lbox
    posy[out_pos_y] -= Lbox
    posz[out_neg_z] += Lbox
    posz[out_pos_z] -= Lbox

    if cut == 2500.:

       posx.tofile("posxfastPMCICz0.562G960V2500.0S2.dat","")
       posy.tofile("posyfastPMCICz0.562G960V2500.0S2.dat","")
       posz.tofile("poszfastPMCICz0.562G960V2500.0S2.dat","")
       vx.tofile("vxfastPMCICz0.562G960V2500.0S2.dat","")
       vy.tofile("vyfastPMCICz0.562G960V2500.0S2.dat","")
       vz.tofile("vzfastPMCICz0.562G960V2500.0S2.dat","")

    elif cut == 1250.:

       cutout = np.where((posx<1250.)&(posy<1250.)&(posz<1250.))[0]
       posx = posx[cutout]
       posy = posy[cutout]
       posz = posz[cutout]
       vx = vx[cutout]
       vy = vy[cutout]
       vz = vz[cutout]

       posx.tofile("posxfastPMCICz0.562G480V1250.0S2.dat","")
       posy.tofile("posyfastPMCICz0.562G480V1250.0S2.dat","")
       posz.tofile("poszfastPMCICz0.562G480V1250.0S2.dat","")
       vx.tofile("vxfastPMCICz0.562G480V1250.0S2.dat","")
       vy.tofile("vyfastPMCICz0.562G480V1250.0S2.dat","")
       vz.tofile("vzfastPMCICz0.562G480V1250.0S2.dat","")


    elif cut == 625.:

       cutout = np.where((posx<625.)&(posy<625.)&(posz<625.))[0]
       posx = posx[cutout]
       posy = posy[cutout]
       posz = posz[cutout]
       vx = vx[cutout]
       vy = vy[cutout]
       vz = vz[cutout]

       posx.tofile("posxfastPMCICz0.562G240V625.0S2.dat","")
       posy.tofile("posyfastPMCICz0.562G240V625.0S2.dat","")
       posz.tofile("poszfastPMCICz0.562G240V625.0S2.dat","")
       vx.tofile("vxfastPMCICz0.562G240V625.0S2.dat","")
       vy.tofile("vyfastPMCICz0.562G240V625.0S2.dat","")
       vz.tofile("vzfastPMCICz0.562G240V625.0S2.dat","")


    return None


if __name__ == "__main__":


  d = BigData(BigFile('fastpmT_0.6403'), ['Position', 'Velocity'])
  positions = d['Position'][:]
  velocities = d['Velocity'][:]
  filepath = "/export/sirocco1/mv1003/fastpm/runner/"
  Lbox = 2500.0
  cut = 2500.0
  wrapper(positions , velocities , Lbox , cut)
