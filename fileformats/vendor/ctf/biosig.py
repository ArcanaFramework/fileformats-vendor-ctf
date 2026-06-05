from fileformats.core.mixin import WithMagicNumber
from fileformats.generic import Directory, BinaryFile
from fileformats.application import Xml
from fileformats.biosig import Meg


class CtfMeg4(WithMagicNumber, BinaryFile, Meg):
    """
    CTF MEG4 binary data file (.meg4) — raw sensor data in CTF's proprietary format.
    The resource file (.res4) in the same .ds directory describes the channel layout.
    """

    ext = ".meg4"
    # First 8 bytes: "MEG41CP\0" (CTF MEG4 format version identifier)
    magic_number = b"MEG41CP\x00"


class CtfRes4(WithMagicNumber, BinaryFile, Meg):
    """
    CTF resource file (.res4) — binary header describing channel layout, sampling
    rate, sensor positions, and filter settings for the accompanying .meg4 data.
    """

    ext = ".res4"
    # First 8 bytes: "MEG41RS\0" (CTF resource file version identifier)
    magic_number = b"MEG42RS\x00"


class CtfInfo(Xml, Meg):
    """
    CTF dataset info file (.infods) — XML file containing dataset-level metadata
    such as subject info, acquisition date, and operator notes.
    """

    ext = ".infods"


class Ctf(Directory, Meg):
    """
    CTF format MEG (directory-based, proprietary format for CTF MEG devices)
    Core files include *.meg4/*.res4/*.infods under .ds directory
    """

    ext = ".ds"

    content_types = (CtfMeg4, CtfRes4, CtfInfo)
