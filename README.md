# LaserProject

The files found in this repository are algorithms that contribute to the fast steering mirror network project developed by Prabrup Chana IA Summer Intern 2023
The main scripts developed serve the following purpose:
  - Using only mirror distances to work out the high accuracy positions of each mirror in a predefined cartesian coordinate system
  - Light detections script -> we now want to use aruco markers
  - Algorithm that, using vector calculations, computes if a mirror network arrangement is feasible < - needs optomisation for it to find all feasible mirror arrangements

Languages:
  -Python (with Jupyter Notebooks)
Libraries:
  -Numpy
  -Matplotlib
  -networkx
  -scipy
  -sklearn
  -optoMDC <- sdk downlaoded from optotune website (https://www.optotune.com/downloads)

  optomization.py <- script works out x,y,z position of each mirror from the distances using optomization
  mirrorArrangementAlgo.ipynb <- script takes a randomly generated set of points that define a mirror network and apply checks on it to test its feasibility. Can be combined with optomization to find a working system
  LightDetection.py <- detects light sources and produces xyz. Not very accurate
