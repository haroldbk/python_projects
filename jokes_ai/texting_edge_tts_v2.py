import asyncio
import edge_tts
import pygame

async def speak(text,filename='output.mp3'):
    communicate = edge_tts.Communicate(text=text,
                                       voice= "en-US-EmmaNeural",
                                       rate="+25%", #25% faster
                                       pitch="-10Hz", #slightly deeper pitch
                                       volume="+10%" #10% louder 
                                       )
    await communicate.save(filename)

    # Play generated audio
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load(filename=filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
    #3. critical: unload audio file so the OS unlocks it
    pygame.mixer.music.unload()        

def play(mytext):
    #text= "Hello! This uses natural neural voices without COM cleanup issues."
    text = mytext
    asyncio.run(speak(text))
