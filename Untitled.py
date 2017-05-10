def test():
  from random import choice
  
  
  hmpic=["   _____\n\
   |   |\n\
       |\n\
       |\n\
       |\n\
  _____|\n",

         "   _____\n\
   |   |\n\
   O   |\n\
       |\n\
       |\n\
  _____|\n",

      
         "   _____\n\
   |   |\n\
   O   |\n\
   |   |\n\
       |\n\
  _____|\n",

         "   _____\n\
   |   |\n\
   O   |\n\
  /|   |\n\
       |\n\
  _____|\n",

         "   _____\n\
   |   |\n\
   O   |\n\
  /|\  |\n\
       |\n\
  _____|\n",
                      
         "   _____\n\
   |   |\n\
   O   |\n\
  /|\  |\n\
  /    |\n\
  _____|\n",
                      
         "   _____\n\
   |   |\n\
   O   |\n\
  /|\  |\n\
  / \  |\n\
  _____|\n"]
  #here i force users to enter an integer for number of game they want
  x=True
  #number of game
  ngame=0
  while x:
    try:
      ngame=int(input('how many turns?'))
      if isinstance(ngame, int):
        x=False
    except:
      continue
  
  def oneletter():
    flag=False
    while not flag:
      l=input('guess letter')
      if len(l) is 1:
        flag=True
        return l
      else:
        print('1 letter only')
        
        flag=False
  wordlist=[ 'python3', 'django', 'basket', 'root']  

#rand lessens,
# randcopy stays the same,
#irm is the index of the removed l from randcopy
  for i in range(ngame):
    rand=list(choice(wordlist))
    randcopy = rand[:]
    lines=[char for char in len(rand)*'_']
    #because the first object in a list is indexed 0, to access the 1st "hmpic" when the users make their 1st mistake, i need to set "mistakes" to -1.    
    mistakes, progress=-1,0
    outtaguess, winning=False, False
    irm=[]
    print(' '.join(lines))
    while (not winning) and (not outtaguess):
      l=oneletter()
      if l in rand:
        print('letter correct\n')
        rand.remove(l)
        for idx,itm in enumerate(randcopy):
          if (itm is l) and (idx in irm):
            continue
       
          if (itm is l) and not (idx in irm):
              del lines[idx]
        
              lines.insert(idx, itm)
              print(' '.join(lines))
              irm += [idx]
              break
        progress+=1
        if progress is len(randcopy): 
          print('you won this turn!')
          winning = True
          
      else:
        print('letter wrong\n')
        mistakes += 1
        if mistakes < 6:
          print(hmpic[mistakes])
        elif mistakes == 6:
          print(hmpic[mistakes])
          print('GAME OVER, u lose! and the word is %s'% (''.join(randcopy)))
          outtaguess = True
        
Untitled.main()
