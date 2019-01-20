import os
import sys
import glob


# Get task ID
try: 
	tid = int(sys.argv[1])
except:
	tid = 181211022

# Make a temporary directory
path = '/data5/moss/alta/%i' % tid
try:
	os.mkdir(path)
except:
	print("Path already made!")

# Loop through and copy all beams
for i in range(0,40):

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
		cmd = 'cp %s %s/%s_B%.3d.UVFITS' % (x,path,stem,i)
		print(cmd)
		#os.system()

	# Send to ALTA
	# Make a folder on alta
	alta_path = '/altaZone/home/apertif_main/early_results/%i' % tid
	os.system('imkdir %s' % alta_path)

	# Copy
	cmd = 'python /home/moss/altadata/putdata_alta.py %s %s' % (path,alta_path)
	print(cmd)
#	os.system()