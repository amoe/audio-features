Note that this can't be run on systems without AVX extension, as Tensorflow
fails.

Check for 'avx' flag in /proc/cpuinfo.

This will manifest through an 'illegal hardware instruction' error when
importing Tensorflow.
