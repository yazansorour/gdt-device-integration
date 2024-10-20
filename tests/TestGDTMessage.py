import unittest
from classes.GDTMessage import GDTMessage
from enums.GDTMessageDataTag import GDTMessageDataTag

class TestGDTMessage(unittest.TestCase):
    def setUp(self):
        self.message_data = {
            'ROOT_DATA_TRANSFER_SET_TYPE': '6302',
            'SENTENCE_LENGTH': '',
            'DEVICE_METHOD': 'PEndo',
            'RECEIVER_GDT_ID': 'PEndo',
            'SENDER_GDT_ID': 'PCS_AM',
            'SET_TYPE_USED': '2',
            'VERSION_GDT': '02.10',
            'PATIENT_NUMBER': 'PatID-20241016-123456799',
            'PATIENT_NAME': 'Mosaab',
            'PATIENT_FIRST_NAME': 'Beliq',
            'PATIENT_BIRTH_DATE': '05101998',
            'PATIENT_SEX': '1',
            'PATIENT_HEIGHT': '178.00',
            'PATIENT_WEIGHT': '25.00',
            'TEST_ID': 'PEndo'
        }

    def test_gdt_message_build(self):
        # Create a GDT message
        gdt_message = GDTMessage()
        
        # Convert the items to a list
        items = list(self.message_data.items())
        
        # Loop through the data dictionary and append lines to the message
        for index, (key, value) in enumerate(items):
            field_tag = getattr(GDTMessageDataTag, key)
            if index == len(items) - 1:
                gdt_message.appendLine(field_tag, value, isLast=True)
            else:
                gdt_message.appendLine(field_tag, value)

        # Build the final message
        gdtMessage = gdt_message.buildMessage()

        with open('tests/TestGDT/TestGDT.gdt' ,'w', encoding='cp437') as file:
            file.write(gdtMessage)


        expectedResult = ''
        with open('GDT/IN/EXP-GDT.gdt' , 'r') as file:
            expectedResult = file.read()

        resultMessage = '' 
        with open('tests/TestGDT/TestGDT.gdt','r') as file:
            resultMessage = file.read()


        self.assertEqual(resultMessage, expectedResult)