import sys, pygame, time

def delay_print_sound(text, delay=0.05, sound_interval=3):
    
    typewriter_sound = pygame.mixer.Sound("")
    
    for index, char in enumerate(text):
        
        sys.stdout.write(char)
        sys.stdout.flush()
        
        if index % sound_interval == 0:
            typewriter_sound.play()
    
        time.sleep(delay)
    
    print()

def delay_print(text, delay=0.05):
    
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)
    print()
    
def delay_print_fast(text, delay=0.02):
    
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(delay)
    print()
    
