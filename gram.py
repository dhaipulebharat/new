import random
import json

import language_tool_python

def get_response(msg):
    print(msg)
    tool = language_tool_python.LanguageTool('en-US')#config={'maxSpellingSuggestions':1})
    matches = tool.check(msg)
 
    len(matches)
    ki=""
    for i in range(len(matches)):
        print(matches[i])
        ki+=str(matches[i])+"\n\n\n"
        print("-"*100)
        print()

    my_mistakes = []
    my_corrections = []
    start_positions = []
    end_positions = []
    
    for rules in matches:
        if len(rules.replacements)>0:
            start_positions.append(rules.offset)
            end_positions.append(rules.errorLength+rules.offset)
            my_mistakes.append(msg[rules.offset:rules.errorLength+rules.offset])
            my_corrections.append(rules.replacements[0])
        
    
        
    my_new_text = list(msg)
    
    
    for m in range(len(start_positions)):
        for i in range(len(msg)):
            my_new_text[start_positions[m]] = my_corrections[m]
            if (i>start_positions[m] and i<end_positions[m]):
                my_new_text[i]=""
        
    my_new_text = "".join(my_new_text)
    my_new_text

    er=list(zip(my_mistakes,my_corrections))
    c=""
    for k in er:
        c+=str(k)+"\n"
        print(k)

   # text = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
    cor=str(tool.correct(msg))
    cor+="\n\n\nCORRECTIONS:\n\n"+c+"\n"#+ki
   # print(cor)
    return cor


if __name__ == "__main__":
    print("Enter te text:")
    while True:
        # sentence = "do you use credit cards?"
        #sentence = input("You: ")
        sentence = 'A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'
        resp = get_response(sentence)
        print(resp)
        break
        print()

