def main():
    with open('alice.txt', 'r', encoding='utf-8') as f:
        contents = f.readlines()
        
    chapter1 = contents[52:267] # this is a list so you can slice it like: chapter1[0]
    print(chapter1[0]) # this is to check if the list contains the correct elements where chapter1[0] is title
    print(chapter1[-7]) # this prints the last WORD in the list to see if it is indeed the last work of chapter1
    
    with open('chapter1.txt', 'w') as f:
        f.writelines(chapter1)
        
        
main()