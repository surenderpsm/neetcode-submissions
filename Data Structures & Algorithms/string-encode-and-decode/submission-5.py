class Solution:
    # The simplest brute force approach is to use a delimiter character that is not present in the constraints,
    # But for a generalized approach where any character is in the input domain, then how do we differentiate.

    # we can use a length based structuring. for example if we have ['abc123', '6:abcabc', 'name is leo']
    # encoded string will be "6:abc1238:6:abcabc11:name is leo"
    # and the decoding run through's job is to parse exactly how many characters we need from the lenght given..
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # header is of format length of string followed by a colon(:)
            header = str(len(string)) + ':'
            # append to encoded result
            encoded_string+=header+string
        return encoded_string

    # encode is working as expected.

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        # remember to clear buffer once digit is collected.
        length_buffer = ""
        next_string = True
        current_length = -1
        # remember to clear buffer when full string is collected.
        current_string = ""
        for char in s:
            # if length buffer is empty, then we are looking for the string.
            if next_string:
                if char == ':':
                    # empty buffer into current_length
                    try:
                        current_length = int(length_buffer)
                        next_string = False
                        if current_length == 0:
                            decoded_list.append("")
                            next_string = True
                    except ValueError as e:
                        print(str(current_length) + " is not a valid header")
                        # return till what was decoded
                        return decoded_list
                    length_buffer = ""
                else:
                    length_buffer+=char
            else:
            # if current length is not zero
                if current_length:
                    current_string+=char
                    current_length-=1
            # else clear current string into list
                if not current_length:    
                    decoded_list.append(current_string)
                    current_string = ""
                    next_string = True
                    current_length = -1
        
        return decoded_list



# rough work

# example for decoding: "3:abc10:abcdefghij"

# starting out, we know that header is what we're expecting. 

# lenbuf += char. 

# if lenbuf is not empty and we see a colon, then we clear buffer and dump it as an int into current length.




