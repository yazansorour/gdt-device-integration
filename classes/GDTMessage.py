class GDTMessage:
    def __init__(self, message_type):
        """
        Initialize the GDTMessage with a specific message type.

        Parameters:
        message_type (GDTMessageType): The type of the GDT message.
        """
        self.type = message_type
        self.fields = []

    def getBDTFormat(self, field_label, content):
        """
        Create a BDT line with the specified field label and content.

        Parameters:
        field_label (str): The field label to be included in the line.
        content (str): The content associated with the field label.

        Returns:
        str: A formatted BDT line including the length, field label, content, 
             and the CR LF characters at the end.
        """
        line_content = f"{field_label}{content}"
        line_length = len(line_content) + 2  # Include CR LF
        return f"{line_length:03d}{line_content}\r\n"

    def appendLine(self, field_tag, content):
        """
        Add a field to the GDT message.

        Parameters:
        field_tag (GDTMessageDataTag): The field tag enum.
        content (str): The content for the field.
        """
        line = self.getBDTFormat(field_tag.value, content)
        self.fields.append(line)

    def buildMessage(self):
        """
        Build the final GDT message string.

        Returns:
        str: A complete GDT message.
        """
        #message = f"{self.type.value} "
        message = ''
        message += ''.join(self.fields)
        return message