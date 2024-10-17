class GDTMessage:
    def __init__(self):
        """
        Initialize the GDTMessage with a specific message type.

        Parameters:
        message_type (GDTMessageType): The type of the GDT message.
        """
        self.type = None
        self.fields = []
        self.fileSizeTotal = 0;

    def getBDTFormat(self, field_label, content, isLast=False):
        """
        Create a BDT line with the specified field label and content.

        Parameters:
        field_label (str): The field label to be included in the line.
        content (str): The content associated with the field label.
        isLast (Boolean): Check if it is the last line.

        Returns:
        str: A formatted BDT line including the length, field label, content, 
            and the CR LF characters at the end.
        """
        # Format the line content (without the length prefix)
        line_content = f"{field_label}{content}\r\n"
        
        # Calculate the line length (field label + content + CRLF)
        line_length = len(field_label) + len(content) + 5  # +2 for CR LF + 3 for nums

        # Format with 3-digit line length (including CR LF)
        formatted_line = f"{line_length:03d}{line_content}"

        self.fileSizeTotal += line_length
        # Return the formatted line
        return formatted_line

    def appendLine(self, field_tag, content , isLast=False):
        """
        Add a field to the GDT message.

        Parameters:
        field_tag (GDTMessageDataTag): The field tag enum.
        content (str): The content for the field.
        isLast (Boolean) : check if it last line 
        """
        line = self.getBDTFormat(field_tag.value, content , isLast)
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

        # Calcuate file size 
        self.fileSizeTotal += 5
        message = message.replace('0098100',f'0148100{self.fileSizeTotal:005d}')

        return message
    
    def parseMessage(self , msg):
        """
        Parse a message string into a list of dictionaries.

        Each row of the message is expected to be formatted such that:
        - The tag is located at positions 3 to 7 (4 characters).
        - The value follows the tag and extends to the second-to-last character of the row.

        Parameters:
        msg (str): The input message string containing multiple rows, separated by newline characters.

        Returns:
        list: A list of dictionaries, where each dictionary contains:
            - 'tag': The extracted tag from the row.
            - 'value': The extracted value from the row.
        """
        message = []
        for row in msg.split('\n'):
            rowMessage = {}
            rowMessage['tag'] = row[3:7]
            rowMessage['value'] = row[7:(len(row))]
            message.append(rowMessage)
        return message
    

    