
from abc import ABC, abstractmethod



class Whatsapp(ABC) :
    @abstractmethod
    def make_call(self, contact):
        """Every WhatsApp call must implement the make_call method."""
        pass
    
    def display_contact(self, contact):
        print(f"Calling {contact}...")
class VideoCall(Whatsapp):
    def make_call(self, contact, video_quality="HD"):
        print(f"Making a video call to {contact} with {video_quality} quality...")

class VoiceCall(Whatsapp):
    def make_call(self, contact):
        print(f"Making a voice call to {contact}...")