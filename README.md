## Description

Scan a tree of media files for audio class probabilities using
[YAMNet](https://www.tensorflow.org/hub/tutorials/yamnet).

## Usage

Create a venv and install dependencies:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt

Run the entry point.  It takes a directory name as an argument.  The directory
will be recursively walked.

    python3 scanner.py ~/aux/audio_features_test

The tool will calculate probabilities using YAMNet.  The probabilities for each
file will be stored in a JSON file.

The end output is an Excel sheet, 'out.xlsx'.

## Hardware requirements

Note that this can't be run on systems without AVX extension, as Tensorflow
fails.

Check for 'avx' flag in /proc/cpuinfo.

This will manifest through an 'illegal hardware instruction' error when
importing Tensorflow.
