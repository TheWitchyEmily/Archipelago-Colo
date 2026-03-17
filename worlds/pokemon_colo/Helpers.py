from typing import NamedTuple, Optional
from enum import Enum

class PCLocType(Enum):
    NONE = -1
    START = 0
    TRAINER = 1
    SHADOW = 2
    CHEST = 3
    ITEM = 4
    EVENT = 5

class PCItemType(Enum):
    NONE = -1
    POKEMON = 0
    KEYITEM = 1
    ITEM = 2
    POKEBALL = 3
    BERRY = 4 
    TM = 5

class Natures(Enum):
    HARDY = 0
    LONELY = 1
    ADAMANT = 2
    NAUGHTY = 3
    BRAVE = 4
    BOLD = 5
    DOCILE = 6
    IMPISH = 7
    LAX = 8
    RELAXED = 9
    MODEST = 10
    MILD = 11
    BASHFUL = 12
    RASH = 13
    QUIET = 14
    CALM = 15
    GENTLE = 16
    CAREFUL = 17
    QUIRKY = 18
    SASSY = 19
    TIMID = 20
    HASTY = 21
    JOLLY = 22
    NAIVE = 23
    SERIOUS = 24

class StatName(Enum):
    ATTACK = 0
    DEFENSE = 1
    SP_ATTACK = 2
    SP_DEFENSE = 3
    SPEED = 4

class NatureInfo(NamedTuple):
    increase: StatName
    decrease: StatName


class PCRamData(NamedTuple):
    """
    Pokemon Colosseum Location RAM Representation. Any parameters can be left empty.

    Parameters
    --------
    ram_addr: The address of what needs to be checked or of the pointer

    ptr: If the ram_addr is a pointer or not

    ptr_offset: The offset of the ram_addr if it is a pointer

    bit_pos: The bit position if it is a bitflag address in the range of 0-7

    """
    ram_addr: Optional[int] = None
    ptr: bool = False
    ptr_offset: Optional[int] = None
    bit_pos: Optional[int] = None

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
