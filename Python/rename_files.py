import os 

def files_rename():
	directory = input("Enter the 'full' directory: ")

	for filename in enumerate(os.listdir(directory)):
#		print("Filenames ", filename)
		filename1 = list(filename)
#		print("Filenames1 ", filename1)
		filename2 = list(filename1[1])
#		print("Filenames2 ", filename2)



		new = ""
		for x in filename2:
			new = new + x
		name = directory + filename[1]
		rename = directory + new
		
		print("name ",name)
#		print("rename ",rename)
#		os.rename(name, rename)

files_rename()

