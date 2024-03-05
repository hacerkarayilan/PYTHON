def is_all_vowels(word):
    vowels="aeiouAEIOU"
    count=0
    for i in word:
        for a in i:
            if a in vowels:
                count+=1
    if count==len(word):
        return True
    else:
        return False
    
is_all_vowels("hacer")        
        