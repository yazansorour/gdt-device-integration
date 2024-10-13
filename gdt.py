from classes.GDTMessage import GDTMessage
from enums.GDTMessageDataTag import GDTMessageDataTag
from enums.GDTMessageType import GDTMessageType
from helpers.GDTHelpers import GDTHelpers
from classes.GDTConnection import GDTSender , GDTReceiver

data = {
    'PATIENT_TITLE': 'Mr.',
    'PATIENT_NAME': 'Yazan Mohammed',
    'PATIENT_FIRST_NAME': 'Yazan'
}

# Create a GDT message
gdt_message = GDTMessage()

# Convert the items to a list
items = list(data.items())

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

parseMessage = gdt_message.parseMessage(tt)
# Print the complete message
print("* Message *",'\n-----------')
print(tt)
print("* Dict Message *",'\n-----------')
print(parseMessage)
print("* Tag Test *",'\n-----------')
print(GDTHelpers.getKeyByValue(parseMessage[0]['tag']))
