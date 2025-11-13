def Caesar(text,offset,mode):
    list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    offset=int(offset)
    for i in text:
        if i in list_1:
            if mode == 'encryption':
                if list_1.index(i)+offset+1<=len(list_1):
                    text[i]=list_1[list_1.index(i)+offset]
                else:
                    text[i]=list_1[list_1.index(i)+offset+1-len(list_1)]
            elif mode=='decryption':
                if offset<list_1.index(i)+1:
                    text[i]=list_1[list_1.index(i)-offset]
                else:
                    text[i]=list_1[len(list_1)-1-(offset-list_1.index(i))]
    return text
print(Caesar('abc',2,'encryption'))
