import os
name = input('enter your name sir : ')
print('Hello',name.upper())


ooo = '''
Hello Sir, I am your Virtual Assistant,

I can do few things for you
  I can open chrome for you
  I can use facebook for you
  I can watch youtube for you
  I can listen song for you
  I can use linkidin for you
  I can open whatsapp web for you
  I can open game for you

  You can simply type 'exit' or 'quit' or say me 'bye' if you wish to close the program
'''

print(ooo)
a =  True
while a:

    t = name+' sir what can i do for you sir : '
    print(t,end='')
    p = input()

    if 'dont' in p:
        print('should i quit the program sir ')
        a = input('y/n : ')
        if a == 'y' :
            break
        elif a == 'Y':
            break
        else:
            continue
    if ('open'in p or 'OPEN' in p or 'run' in p or 'RUN' in p or 'use'in p or 'USE'in p  )and  'chrome' in p or 'CHROME' in p:
        os.system('chrome')
    
    elif ('open' in p or 'OPEN' in p or 'run'in p or 'RUN' in p or 'see'in p or 'SEE' in p or 'watch' in p or 'WATCH' in p or 'use' in p or'USE' in p) and 'youtube' in p or 'YOUTUBE' in p:
        os.system('chrome   youtube.com')

    elif ('open' in p or 'OPEN' in p or 'run' in p or 'RUN' in p or'see' in p or 'SEE' in p or 'use' in p or 'USE' in p)and 'facebook' in p  or 'FACEBOOK' in p:
        os.system('chrome  facebook.com')

    elif ('open'in p  or 'OPEN' in p or 'run'in p  or 'RUN' in p or'see' in p or 'SEE' in p or 'use' in p or 'USE' in p )and 'linkedin'in p or 'LINKENDIN' in p:
        os.system('chrome  linkedin.com')

    elif ('open' in p or 'OPEN' in p or 'listen'in p  or 'LISTEN' in p or 'play' in p or 'PLAY' in p)and ('english' in p or'ENGLISH') and ('song'in p or 'SONG'in p or 'music' in p or 'MUSIC' in p ):
        os.system('chrome   https://youtu.be/W0DM5lcj6mw')

    elif ('open' in p or 'OPEN' in p  or 'run' in p or 'RUN' in p or 'see' in p or 'SEE' in p or 'use'in p or 'USE' in p) and 'whatsapp' in p or 'WHATSAPP' in p:
        os.system('chrome   https://web.whatsapp.com/')

    elif ('open' in p or 'OPEN' in p or 'paly' or 'PLAY' in p or 'run' in p or 'RUN' in p)and 'game'in p or 'GAME' in p:
        os.system('chrome   https://www.crazygames.com/game/word-wipe')
    
    elif ('open' in p or 'write' in p or'OPEN' in p or 'WRITE' in p ) and 'notepad' in p :
        os.system('notepad')
    
    elif 'exit' in p or 'quit' in p or 'bye' in p: 
        a = False

    else:
        print(ooo)
             
        
