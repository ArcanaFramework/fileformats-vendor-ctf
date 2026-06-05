import typing as ty

import mne.io

from fileformats.core import extra_implementation, FileSet
from fileformats.vendor.ctf.biosig import Ctf


@extra_implementation(FileSet.read_metadata)
def ctf_read_metadata(ctf: Ctf, **kwargs: ty.Any) -> ty.Mapping[str, ty.Any]:
    return mne.io.read_raw_ctf(ctf, preload=False, verbose=False).info.to_json_dict()  # type: ignore[no-any-return]
