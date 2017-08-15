#! /usr/bin/python
# Filename: orb_evaluate.py
# Author:Turtlezhong 2017.07.28 in DM
import matplotlib.pyplot as plt
import numpy as np

groundtruth = open("./poses/00.txt")
# orb_evaluate = open("./orb_Results/stero_only_tracking/02.txt")
orb_evaluate = open("./orb_Results/stero/CameraTrajectory.txt")
# groundtruth = open("/home/m/orb_test/ORB_results/Results/stero/00.txt")
# here we got the total lines of the file
lines = groundtruth.readlines()
lines_eval = orb_evaluate.readlines()

poses = []
poses_eval = []
for line in lines:
    line = line.split()
    list(line)
    xyz_g = [line[3],line[7],line[11]]
    poses.append(xyz_g)

for line_eval in lines_eval:
    line_eval = line_eval.split()
    list(line_eval)
    xyz_eval = [line_eval[3],line_eval[7],line_eval[11]]
    poses_eval.append(xyz_eval)

x_g = []
y_g = []
z_g = []
x_eval = []
y_eval = []
z_eval = []

print poses

for item in poses:
    x_g.append((item[0]))
    y_g.append((item[1]))
    z_g.append((item[2]))

for item_eval in poses_eval:
    x_eval.append((item_eval[0]))
    y_eval.append((item_eval[1]))
    z_eval.append((item_eval[2]))
# for now we got the xyz then we need to plot it
# print x_g
x_groundtruth = np.array(x_g)
z_groundtruth = np.array(z_g)

x_evaluation = np.array(x_eval)
z_evaluation = np.array(z_eval)


# show the data
plt.xlabel('x [m]', size=14)
plt.ylabel('z [m]', size=14)
plt.plot(x_groundtruth, z_groundtruth, color='r', label='Ground Truth')
plt.plot(x_evaluation, z_evaluation, color='b', label='Visual Odometry')
plt.plot(x_groundtruth[0], z_groundtruth[0], 'o', color='green', label='Sequence Start')
plt.legend(loc='upper left')

plt.show()
# plt.savefig('images/plot1.png', format='png')
print 'save image suscessfully'



