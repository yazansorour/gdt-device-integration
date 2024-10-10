from enum import Enum

class GDTMessageType(Enum):
    ROOT_DATA_REQUEST = '6300'
    ROOT_DATA_TRANSFER = '6301'
    NEW_TEST_REQUEST = '6302'
    TEST_DATA_TRANSFER = '6310'
    TEST_DATA_DISPLAY = '6311'