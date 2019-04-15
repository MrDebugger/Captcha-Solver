
import pyautogui
from subprocess import call
from requests import get as ge
from speech_recognition import AudioFile,Recognizer,UnknownValueError,RequestError


class Captcha:
    def __init__(self):
        self.done = [True,'Done']
        self.error = [False,'Failed']

    # Function to solve Captcha
    def solve(self):
        try:
            sleep(3)
            # Scrolling Down the Page
            pyautogui.scroll(-1000)
            # Locating and Clicking Captcha button on Page
            cap = pyautogui.locateCenterOnScreen("files/captcha.png")
            pyautogui.click(cap)
            try:
                sleep(3)
                # Locating and Clicking Headphones button on Page
                voi = pyautogui.locateCenterOnScreen("files/voice.png")
                pyautogui.click(voi)
            except:
                try:
                    # Move out mouse from the voice button 
                    pyautogui.moveTo(200,200)
                    # Locate Voice2 Button that is little Gray
                    pyautogui.locateCenterOnScreen("files/voice2.png")
                    return self.error
                except:
                    return self.done                
        except:
            try:
                sleep(2)
                # Move out mouse from the voice button 
                pyautogui.moveTo(200,200)
                # Locate Voice2 Button that is little Gray
                pyautogui.locateCenterOnScreen("files/voice2.png")
                self.error[1] = "Captcha"
                return self.error
            except:
                return self.done
        sleep(2)
        try:
            # Locate and Right Click on the Download Button
            down = pyautogui.locateCenterOnScreen("files/down.png")
            pyautogui.rightClick(down)
            sleep(1)
            # Press down button 5 times
            pyautogui.press(['down']*5)
            sleep(1)
            # Press Enter (Cursor will be Copy Link Address)
            pyautogui.press('enter')
            # Download and Save that audio file from Link copied from above code
            with open('files/audio.mp3','wb') as file:
                r = ge(paste())
                file.write(r.content)

            sleep(2)
            if path.exists('files/audio.mp3'):
                # Convert that mp3 file into wav using ffpmeg 
                call(['files/ffmpeg.exe', '-i', 'files/audio.mp3', '-y', 'files/audio.wav'])
                sleep(2)
                AUDIO_FILE = 'files/audio.wav'

                # Code to Send That Audio File to Google and Recognize The Audio
                r = Recognizer()
                with AudioFile(AUDIO_FILE) as source:
                    audio = r.record(source) 
                try:
                    # Get the Recognized Text
                    capSolved = r.recognize_google(audio)
                    # Go to the text field and write it there
                    pyautogui.hotkey('shift','tab')
                    pyautogui.typewrite(capSolved)
                    pyautogui.press('enter')
                    sleep(5)
                    return self.done
                except UnknownValueError as e:
                    return self.error
                except RequestError as e:
                    return self.error
        except:
            self.error[1] = "Captcha"
            return self.error
