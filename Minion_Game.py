def minion_game(string):
    # your code goes here
    vowel = 'AEIOU'
    vowel_gamer  = 0
    consonant_gamer  = 0    
    for i in range(len(string)):
        if string[i] in vowel:
                vowel_gamer +=  len(string) - i      
        else:
                consonant_gamer  += len(string) - i
    if  consonant_gamer > vowel_gamer:        
        print(f'Stuart {consonant_gamer}')
    elif consonant_gamer < vowel_gamer: 
        print(f'Kevin {vowel_gamer}')
    else:
        print('Draw')
if __name__ == '__main__':
