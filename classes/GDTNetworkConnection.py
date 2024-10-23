import os
import shutil


class GDTNetworkConnection:

	def __init__(self , inSourceDirectoryPath , inDestinationDirectoryPath, exportSourceDirectoryPath , exportDestinationDirectoryPath):
		self.remoteIPAddress = ''

		# In folder path for requsting test result
		self.inSourceDirectoryPath = inSourceDirectoryPath
		self.inDestinationDirectoryPath = inDestinationDirectoryPath

		# Export Folders path for receving test result
		self.exportSourceDirectoryPath = exportSourceDirectoryPath
		self.exportDestinationDirectoryPath = exportDestinationDirectoryPath

	def sendFile(self,fileName):

		sourceFile = self.inSourceDirectoryPath + f"/{fileName}"
		destinationFileName = os.path.join(self.inDestinationDirectoryPath , os.path.basename(sourceFile))

		# Check if the file already exists in the network folder
		if not os.path.exists(destinationFileName):
			try:
				shutil.copy(sourceFile , destinationFileName)
				print(f"Copied Successfully : {destinationFileName}")
			except Exception as e:
				print(f"Error while copying file : {e}")
		else:
			print(f"The file already exists in the network folder : {destinationFileName}")

	
	# TODO: when the report and the images copied successfully clean the folders  
	def cleanRemoteFolderFiles(self, directoryPath):
	    try:
	        for filename in os.listdir(directoryPath):
	            file_path = os.path.join(directoryPath, filename)
	            if os.path.isfile(file_path):
	                os.remove(file_path)
	                print(f"Removed file: {file_path}")
	            """
	            elif os.path.isdir(file_path):
	                shutil.rmtree(file_path)
	                print(f"Removed directory: {file_path}")
	            """
	    except Exception as e:
	        print(f"Error while cleaning directory: {e}")


	def getRemoteFiles():
		destinationFiles = set(os.listdir(remoteFolderPath))
		for file in remoteFiles:
			sourceFile = os.path.join(self.exportSourceDirectoryPath, file)
			destinationFile = os.path.join(self.exportDestinationDirectoryPath , file)

			if not os.path.exists(sourceFile):
				try:
					if os.path.isfile(destinationFile):
						shutil.copy(destinationFile , sourceFile)
						print(f"Copied Successfully : {destinationFile}")
					else:
						print(f"is not a file : {destinationFile}")

				except Exception as e:
					print(f"Error copying file {destinationFile} : {e}")
			else:
				print(f"The file already exists in the folder: {destinationFile}")




