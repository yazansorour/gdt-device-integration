from classes.GDTMessage import GDTMessage
from enums.GDTMessageDataTag import GDTMessageDataTag
from enums.GDTMessageType import GDTMessageType
from helpers.GDTHelpers import GDTHelpers
from classes.GDTConnection import GDTSender , GDTReceiver

message6300 = {
    'ROOT_DATA_TRANSFER_SET_TYPE': '6300',
    'SENTENCE_LENGTH': '444',
    'RECEIVER_GDT_ID': 'PEendo',
    'SENDER_GDT_ID': 'PHD_PCS',
    'SET_TYPE_USED' : '3',
    'VERSION_GDT':'2.0',
    'PATIENT_NUMBER':'123321'
}

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
#dt_message.fileSizeTotal += 5
#tt = tt.replace('0098100',f'0148100{gdt_message.fileSizeTotal:005d}')

"""
file_path = 'GDT/IN/PCS_AM_Test_Exam_Moab.gdt'
with open(file_path, 'w',encoding='cp437') as file:
    file.write(tt)
"""

print(tt)
