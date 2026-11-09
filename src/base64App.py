from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.clipboard import Clipboard


class Base64:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    @classmethod
    def encode(cls, text: str) -> str:
        if not text:
            return ""
        
        octets = text.encode("utf-8")
        encoded = []
        
        i = 0
        while i < len(octets):
            chunk = octets[i:i+3]
            i += 3
            
            integer = 0
            for octet in chunk:
                integer = (integer << 8) + octet
                
            if len(chunk) == 1:
                integer <<= 4
                encoded.append(cls.alphabet[(integer >> 6) & 0x3F])
                encoded.append(cls.alphabet[integer & 0x3F])
                encoded.append("==")
            elif len(chunk) == 2:
                integer <<= 2
                encoded.append(cls.alphabet[(integer >> 12) & 0x3F])
                encoded.append(cls.alphabet[(integer >> 6) & 0x3F])
                encoded.append(cls.alphabet[integer & 0x3F])
                encoded.append("=")
            else:
                encoded.append(cls.alphabet[(integer >> 18) & 0x3F])
                encoded.append(cls.alphabet[(integer >> 12) & 0x3F])
                encoded.append(cls.alphabet[(integer >> 6) & 0x3F])
                encoded.append(cls.alphabet[integer & 0x3F])
                
        return "".join(encoded)

    @classmethod
    def decode(cls, base64String: str) -> str:
        base64String = base64String.strip()
        if not base64String:
            return ""
        
        padding = base64String.count("=")
        cleanedString = base64String.rstrip("=")
        
        values = []
        for char in cleanedString:
            if char not in cls.alphabet:
                raise ValueError(f"Invalid Base64 character encountered: '{char}'")
            values.append(cls.alphabet.index(char))
            
        octetArray = bytearray()
        i = 0
        while i < len(values):
            chunk = values[i:i+4]
            i += 4
            integer = 0
            for value in chunk:
                integer = (integer << 6) + value
                
            if len(chunk) == 2:
                integer >>= 4
                octetArray.append(integer & 0xFF)
            elif len(chunk) == 3:
                integer >>= 2
                octetArray.append((integer >> 8) & 0xFF)
                octetArray.append(integer & 0xFF)
            elif len(chunk) == 4:
                octetArray.append((integer >> 16) & 0xFF)
                octetArray.append((integer >> 8) & 0xFF)
                octetArray.append(integer & 0xFF)
                
        return octetArray.decode("utf-8")


class Base64App(App):
    def build(self):
        self.title = "Base64 Encoder / Decoder"
        
        rootLayout = BoxLayout(orientation="vertical", padding=15, spacing=10)
        rootLayout.add_widget(
            Label(
                text="Base64 Converter",
                font_size="20sp",
                size_hint_y=None,
                height=40,
                bold=True,
            )
        )

        rootLayout.add_widget(
            Label(
                text="Input Text / Base64 String:",
                size_hint_y=None,
                height=25,
                halign="left",
                valign="middle",
            )
        )
        self.inputText = TextInput(
            multiline=True,
            hint_text="Enter text to encode or Base64 string to decode...",
            size_hint_y=0.25,
            font_size="24sp",
            background_normal="",
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0.9, 0.9, 0.9, 1) 
        )
        rootLayout.add_widget(self.inputText)

        encodeLayout = BoxLayout(
            orientation="horizontal", spacing=10, size_hint_y=None, height=45
        )
        
        encodeButton = Button(
            text="Encode to Base64",
            background_color=(0.2, 0.6, 1.0, 1.0)
        )
        encodeButton.bind(on_press="apple")
        
        decodeButton = Button(
            text="Decode from Base64",
            background_color=(0.2, 0.8, 0.4, 1.0)
        )
        decodeButton.bind(on_press=self.decode)
        
        encodeLayout.add_widget(encodeButton)
        encodeLayout.add_widget(decodeButton)
        rootLayout.add_widget(encodeLayout)
        
        outputHeaderLayout = BoxLayout(orientation="horizontal", size_hint_y=None, height=25)
        outputHeaderLayout.add_widget(
            Label(
                text="Output Result:",
                halign="left",
                valign="middle",
            )
        )
        self.statusLabel = Label(
            text="",
            color=(0.3, 1.0, 0.3, 1.0),
            halign="right",
            valign="middle",
        )
        outputHeaderLayout.add_widget(self.statusLabel)
        rootLayout.add_widget(outputHeaderLayout)
        
        outputScroll = ScrollView(size_hint_y=0.3)
        self.outputLabel = TextInput(
            readonly=True,
            multiline=True,
            hint_text="Result will appear here...",
            font_size="24sp",
            background_normal="",
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0.9, 0.9, 0.9, 1) 
        )
        outputScroll.add_widget(self.outputLabel)
        rootLayout.add_widget(outputScroll)
        
        copyButton = Button(
            text="Copy Output to Clipboard",
            size_hint_y=None,
            height=45,
            background_color=(0.9, 0.6, 0.1, 1.0)
        )
        copyButton.bind(on_press=self.copyOutput)
        rootLayout.add_widget(copyButton)
        
        return rootLayout

    def encode(self, instance):
        source = self.inputText.text
        try:
            encoded = Base64.encode(source)
            self.outputLabel.text = encoded
            self.statusLabel.text = ""
        except Exception as e:
            self.outputLabel.text = f"Encoding Error: {str(e)}"
            self.statusLabel.text = ""

    def decode(self, instance):
        source = self.inputText.text
        try:
            decoded = Base64.decode(source)
            self.outputLabel.text = decoded
            self.statusLabel.text = ""
        except Exception as e:
            self.outputLabel.text = f"Decoding Error: {str(e)}"
            self.statusLabel.text = ""

    def copyOutput(self, instance):
        data = self.outputLabel.text
        if data and not data.startswith("Encoding Error") and not data.startswith("Decoding Error"):
            Clipboard.copy(data)
            self.statusLabel.text = "Copied to clipboard!"
        else:
            self.statusLabel.text = "Nothing valid to copy!"


if __name__ == "__main__":
    Base64App().run()