import os
import shutill


class GDTNetworkConnection:

	def __init__(self):
		self.remoteIPAddress = ''

		# In folder path
		self.inSourceDirectoryPath = ''
		self.inDestinationDirectoryPath = ''

		# Export Folders path
		self.exportSourceDirectoryPath = ''
		self.exportDestinationDirectoryPath = ''

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
	def cleanRemoteFolderFiles():
		return 0

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




