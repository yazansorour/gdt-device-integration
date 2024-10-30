import os
import shutil


class GDTNetworkConnection:

	@staticmethod
	def sendFile(filePath , destinationDir):

		sourceFile =  filePath
		destinationFileName = os.path.join(destinationDir , os.path.basename(sourceFile))

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
	@staticmethod
	def cleanRemoteFolderFiles(directoryPath):
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

	@staticmethod
	def getRemoteFiles(sourceDir , remoteDir):
		isCopiedSuccessfly = False
		copiedFiles = []
		destinationFiles = set(os.listdir(remoteDir))
		if len(destinationFiles):
			for file in destinationFiles:
				sourceFile = os.path.join(sourceDir, file)
				destinationFile = os.path.join(remoteDir , file)
				if not os.path.exists(sourceFile):
					try:
						if os.path.isfile(destinationFile):
							shutil.copy(destinationFile , sourceFile)
							copiedFiles.append(sourceFile)
							print(f"Copied Successfully : {destinationFile}")
							isCopiedSuccessfly = True
						else:
							print(f"is not a file : {destinationFile}")

					except Exception as e:
						print(f"Error copying file {destinationFile} : {e}")
						isCopiedSuccessfly = False
				else:
					print(f"The file already exists in the folder: {destinationFile}")
			if (isCopiedSuccessfly == True):
				GDTNetworkConnection.cleanRemoteFolderFiles(remoteDir)
		return copiedFiles
	




