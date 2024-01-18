import speech_recognition as sr


class Speakers(sr.Microphone):
    @staticmethod
    def get_pyaudio():
        """
        Imports the pyaudio module and checks its version. Throws exceptions if pyaudio can't be found or a wrong version is installed
        """
        try:
            import pyaudiowpatch as pyaudio
        except ImportError:
            raise AttributeError("Could not find PyAudio; check installation")
        from distutils.version import LooseVersion
        if LooseVersion(pyaudio.__version__) < LooseVersion("0.2.11"):
            raise AttributeError("PyAudio 0.2.11 or later is required (found version {})".format(pyaudio.__version__))
        return pyaudio
