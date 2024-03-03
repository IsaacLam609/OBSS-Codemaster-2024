# Situation
# Develop a client application that communicates with a server using WebSocket.
# The application has to send the given text to the server character-by-character.
# The message should start with "/" and each character should be translated into Morse code with its index.
# The client should wait for an acknowledgement message (which is the character being sent) from the server before sending the next character.
# After the server has received the correct message, it will respond with a UUID text in the form of Morse.

import asyncio
import websockets

text_to_be_sent = "ADIPISCING ELIT"

morse_code = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
              "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
              "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
              "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
              "?": "..--..", "!": "-.-.--", "-": "-....-", "/": "-..-.", " ": "--.--"}

def morse_code_conversion(text):    # convert string to morse code
    converted = "-..-. "                                            # add "/" at the beginning to indicate the start of a message
    for i in range(len(text)):
        index = str(i+1)
        character = text[i]
        if (character < "z") and (character > "a"):                 # convert lower case letters to upper case
            character = chr(ord(character) - ord("a") + ord("A"))
        concatenated = index + character                            # add an index to each character before sending out
        for c in concatenated:
            converted += morse_code[c] + " "                        # add a space between characters

    return converted

def text_conversion(morse):        # convert morse code to string
    converted = ""
    key_list = list(morse_code.keys())
    val_list = list(morse_code.values())
    temp = ""
    for c in morse:
        if c == " ":
            position = val_list.index(temp)
            converted += key_list[position]
            temp = ""
        else:
            temp += c
    position = val_list.index(temp)
    converted += key_list[position]

    return converted

async def send_to_websocket(text):
    uri = "ws://cm2024.obss.io:8443/morse/01HME1H7FPX3C4H1WGVFCKHF8W"
    async with websockets.connect(uri) as websocket:
        morse = morse_code_conversion(text)

        temp = ""
        for c in morse:
            successful = False
            while not successful:                       # keep sending the message to the server until its successful
                if c == " ":

                    # if the last character of the temp is a letter, it is ready to send to the server
                    index_with_char_extracted = (text_conversion(temp)[-1] >= "A") and (text_conversion(temp)[-1] <= "Z")


                    if index_with_char_extracted or (text_conversion(temp) == "/") or (text_conversion(temp)[-1] == " "):
                        await websocket.send(temp)
                        received = await websocket.recv()

                        if received == temp:           # server sends the same character to the client as acknowledgement
                            successful = True
                            temp = ""
                        elif received == "ERROR-UNRECOGNIZED-LETTER":
                            raise Exception("Error: unrecognized letter")
                    else:
                        temp += c
                        successful = True

                else:
                    temp += c
                    successful = True

        final_msg = await websocket.recv()              # receive final message from server after the whole message is sent
        print(text_conversion(final_msg))

if __name__ == "__main__":
    asyncio.run(send_to_websocket(text_to_be_sent))