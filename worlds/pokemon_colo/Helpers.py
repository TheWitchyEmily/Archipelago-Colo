class StringByteFunction:
    @staticmethod
    def string_to_bytes(user_string: str, encoded_length: int) -> bytes:
        """
        Encodes a provided string to UTF-8. Padding added until expected length is reached.
        Raise an exception if provided string is longer than provided length
        
        :param user_string: String to encode to bytes
        :param encoded_length: Expected length of provided string.
        """
        encoded_string = user_string.encode('utf-8')

        if len(encoded_string) < encoded_length:
            encoded_string += b'\x00' * (encoded_length - len(encoded_string))
        elif len(encoded_string) > encoded_length:
            raise Exception("Provided string '" + user_string + "' was langer than the expected byte length of '" + str(encoded_length) + "', which will not be accepted by the info file.")
        return encoded_string

    @staticmethod
    def byte_string_strip_null_terminator(bytes_input: bytes):
        return bytes_input.decode().strip("\0")
