def triangel_ner(dist, bredd):
    if bredd <= 2:
        print(dist*" " + bredd*"*")
    else:
        print(dist*" " + bredd*"*")
        triangel_ner(dist+1, bredd-2)

def triangel_upp(dist, bredd):
    if bredd <= 2:
        print(dist*" " + bredd*"*")
    else:
        triangel_upp(dist+1, bredd-2)
        print(dist * " " + bredd * "*")

triangel_upp(0, 15)