class Solution:
    # The simplest brute force approach is to use a delimiter character that is not present in the constraints,
    # But for a generalized approach where any character is in the input domain, then how do we differentiate.

    # we can use a length based structuring. for example if we have ['abc123', '6:abcabc', 'name is leo']
    # encoded string will be "6:abc1238:6:abcabc11:name is leo"
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # header is of format length of string followed by a colon(:)
            header = str(len(string)) + ':'
            # append to encoded result
            encoded_string+=header+string
        return encoded_string

    # decode uses string splicing to find the next :, which gets the header and subsequently use the length to find the string.
    def decode(self, s: str) -> List[str]:
        decoded_list = []

        i = 0

        while i < len(s):

            j = s.find(':', i)

            str_length = int(s[i:j])

            i = j+1

            decoded_list.append(s[i:i+str_length])

            i+=str_length

        return decoded_list







