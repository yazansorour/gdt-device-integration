from enums.GDTMessageDataTag import GDTMessageDataTag

class GDTHelpers:

    @staticmethod
    def getKeyByValue(tag_value):
        for member in GDTMessageDataTag:
            if member.value == tag_value:
                return member.name
        return None