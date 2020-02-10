#
# Simple program to modify shuffleboard csv files for use in other plotting tools
#    a work in progress, currently makes some simple plots on it's own
#
import argparse
import os.path
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Reads 2020 test shuffleboard csv file and process. If --output is specified save a copy processed data')
parser.add_argument('infile', help='shuffleboard recording csv file to processs')
parser.add_argument('--outfile', help='optional arg to specify an output filename')
args = parser.parse_args()
print(args.infile)

# check if infile exists, and if we can open it.
if os.path.isfile(args.infile):
    rdf = pd.read_csv(args.infile)
else:
    print ("Input file not found")
    exit()
	
# Get current axes
ax = plt.gca()


# Plot both shooter motors
rdf.plot(kind='line',x='Timestamp',y='network_table:///SmartDashboard/shooter1RPM:', label='shooter1RPM', ax=ax)
rdf.plot(kind='line',x='Timestamp',y='network_table:///SmartDashboard/shooter2RPM:', label='shooter2RPM', color='red',ax=ax)

# Add a major grid
ax.grid()

# Create a note with RPM target, KF, KP, KI
rpmfb = rdf.loc[0,'network_table:///SmartDashboard/Shooter RPM Feedback']
kffb = rdf.loc[0,'network_table:///SmartDashboard/Shooter KF Feedback']
kpfb = rdf.loc[0,'network_table:///SmartDashboard/Shooter KP Feedback']
kiset = rdf.loc[0,'network_table:///Shuffleboard/drive/KI']
note_text = "targetRPM={}\nKF={}\nKP={}\nKI={}".format(rpmfb, kffb, kpfb, kiset)

# Put the note on the plot somewhere
ax.text(15000, 2000, note_text, style='italic',
        bbox={'facecolor': 'green', 'alpha': 0.5, 'pad': 10})
       
# Draw the plot        
plt.show()