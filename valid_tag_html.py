codigo_html = input("")

tags_html = codigo_html.split(">")
tags_html.pop()

def validar(tags:list) -> str:
    stack = []
    for tag in tags:
        if "/" in tag: 
            if len(stack) == 0:
                return "Código Inválido"
            
            ultima_tag = stack.pop()
            index = tag.find("/")
            if ultima_tag != tag[index+1:]:
                return "Código Inválido"
            
            else:
                continue
                   
        else:
            stack.append(tag[1:]) 
            
    if len(stack) > 0:
        return "Código Inválido"
    else:
        return "Código Válido"
        
print(validar(tags_html))


