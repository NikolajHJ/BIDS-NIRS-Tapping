# Install MNE (if not already installed)
# pip install mne mne-bids

import os
from mne_bids import BIDSPath, read_raw_bids

# 1) Point to the root folder of your BIDS dataset
bids_root = "/data"

# 2) Specify the BIDS entities (subject, task, etc.).
#    For example, let's load subject '01', who performed the 'tapping' task.
bids_path = BIDSPath(
    subject='01',
    task='tapping',
    suffix='nirs',         # suffix = 'nirs' for fNIRS data
    extension='.snirf',    # extension = '.snirf' (or '.xdf', etc. if that’s your data format)
    root=bids_root
)

# 3) Read the fNIRS file into an MNE Raw object
raw = read_raw_bids(bids_path=bids_path, verbose=True)

# 4) Now you have an MNE Raw object with the NIRS data
print(raw)
print(raw.info)

# 5) (Optional) Plot the raw data to get a quick look
raw.plot(duration=30, n_channels=10)
