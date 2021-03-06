import os
import sys
import glob


# Get task ID
try: 
	tid = int(sys.argv[1])
except:
	tid = 181211022

try: 
	sbeam = int(sys.argv[2])
except:
	sbeam = 0 

try: 
	ebeam = int(sys.argv[3])
except:
	ebeam = 40

# Make a temporary directory
path = '/data5/moss/alta/%i' % tid
try:
	os.mkdir(path)
except:
	print("Happili-05 path already made!")

# Loop through and copy all beams
for i in range(sbeam,ebeam):

	# Copy and rename
	node = i // 10 + 1
	#print('Checking happili-%.2d' % node)
	if node > 1:
		files = glob.glob('/data%s/apertif/%i/%.2d/crosscal/*UVFITS' % (node,tid,i))
	else:
		files = glob.glob('/data/apertif/%i/%.2d/crosscal/*UVFITS' % (tid,i))

	# Copy
	for x in files:
		stem = x.split('.UVFITS')[0].split('/')[-1]

		# Change name to standard format
		#cmd = 'cp %s %s/%s_B%.3d.UVFITS' % (x,path,stem,i)
		cmd = 'cp %s %s/WSRTA%s_B%.3d_CAL.UVFITS' % (x,path,tid,i)

		print(cmd)
		os.system(cmd)

# Send to ALTA
# Make a folder on alta
alta_path = '/altaZone/home/apertif_main/early_results'
# try:
# 	os.system('imkdir %s' % alta_path)
# except: 
# 	print("ALTA path already made!")

# Copy
os.chdir('/data5/moss/alta/')
cmd = 'python /home/moss/altadata/putdata_alta.py %s %s' % (tid,alta_path)
print(cmd)
os.system(cmd)