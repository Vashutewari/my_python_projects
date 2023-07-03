import os
if __name__ == '__main__':
     while(True):
         enter=input("enter what you want me to speak : ")

         if (enter=="exit"):

              print("exited")

         else:
             command = f"Powershell Add-Type -AssemblyName System.Speech;" \
              f" (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{enter}')"

             os.system(command)

