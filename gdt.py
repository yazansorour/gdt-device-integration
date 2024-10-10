from helpers.GDTMessage import GDTMessage
from enums.GDTMessageDataTag import GDTMessageDataTag
from enums.GDTMessageType import GDTMessageType

# Data for the GDT message
data = {
    'PATIENT_TITLE': 'Mr.',
    'PATIENT_NAME': 'Yazan Mo',
    'PATIENT_FIRST_NAME': 'Yazan'
}

# Create a GDT message
gdt_message = GDTMessage(GDTMessageType.ROOT_DATA_REQUEST)

# Loop through the data dictionary and append lines to the message
for key, value in data.items():
    # Use the key to get the corresponding enum value
    field_tag = getattr(GDTMessageDataTag, key)
    gdt_message.appendLine(field_tag, value)

# Build the final message
tt = gdt_message.buildMessage()

# Print the complete message
print(tt)