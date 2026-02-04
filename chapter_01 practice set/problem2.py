
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Its me pawan, trying to learn python programming. Its not hard but not easy at all because you have be consistant and disciplined to learn it.")
engine.runAndWait()