import sys
from tkinter import Tk
from Client import Client
from ClientExtend import ClientExtend
color_bg = "#245953"
if __name__ == "__main__":
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]	
	except:
		print("[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]\n")	
	# Create a new client
	print('Normal Option: 1')
	print('Extend Option: 2')
	while True:
		INPUT = int(input('Your choice: '))
		if(INPUT == 1 ):
			root = Tk()
			app = Client(root, serverAddr, serverPort, rtpPort, fileName)
			break
		elif(INPUT == 2):
			root = Tk()
			app = ClientExtend(root, serverAddr, serverPort, rtpPort, fileName)
			break
		else:
			print('Choose your version 1 [normal] or 2[extend]: ')
	app.master.title("Media Player")
	app.master.configure(bg=color_bg)
	root.mainloop()
	