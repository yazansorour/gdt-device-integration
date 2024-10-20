from classes.GDTMessage import GDTMessage
from enums.GDTMessageDataTag import GDTMessageDataTag
from classes.GDTNetworkConnection import GDTNetworkConnection

message6301 = {
    'ROOT_DATA_TRANSFER_SET_TYPE': '6302',  # Message type
    'SENTENCE_LENGTH': '',
    'DEVICE_METHOD': 'PEndo',                # Length of the message
    'RECEIVER_GDT_ID': 'PEndo',              # Receiver ID
    'SENDER_GDT_ID': 'PCS_AM',              # Sender ID (same as before)
    'SET_TYPE_USED': '2',                     # Type of data transfer
    'VERSION_GDT': '02.10',                    # Version of the GDT
    'PATIENT_NUMBER': 'PatID-20241016-123456799',              # Patient number
    'PATIENT_NAME': 'Mosaab',           # Surname
    'PATIENT_FIRST_NAME': 'Beliq',            # First name
    'PATIENT_BIRTH_DATE': '05101998',          # Date of birth (DDMMYY)
    'PATIENT_SEX': '1',                      # Sex: 1=male, 2=female
    'PATIENT_HEIGHT': '178.00',                 # Height in cm
    'PATIENT_WEIGHT': '25.00',
    'TEST_ID': 'PEndo'                   # Weight in kg
}

# Create a GDT message
gdt_message = GDTMessage()

# Convert the items to a list
items = list(message6301.items())

# Loop through the data dictionary and append lines to the message
for index, (key, value) in enumerate(items):
    # Use the key to get the corresponding enum value
    field_tag = getattr(GDTMessageDataTag, key)
    if (index == len(items) - 1):
        gdt_message.appendLine(field_tag , value , isLast=True)
    else:
        gdt_message.appendLine(field_tag, value)

# Build the final message
tt = gdt_message.buildMessage()

filePath = 'GDT/IN/EXP-GDT.gdt'

with open(filePath ,'w', encoding='cp437') as file:
	file.write(tt)

print(f"Exported GDT : \n{tt}")

gdtNetwork = GDTNetworkConnection('GDT/IN' , 'GDT/OUT')

#gdtNetwork.sendFile('EXP-GDT.gdt')

gdtNetwork.cleanRemoteFolderFiles(gdtNetwork.inDestinationDirectoryPath)