r1=input("tu perro ladra ")
if(r1=="si"):
    print("es un canino")
    r2=input("tu perro es muerde ")
    if(r2=="si"):
        print("tu perro es peligroso")
        print("te recomiendo que le coloqu es un bozal")
    else:
        print("no recomiendo el bozal") 
else:
    print("No es canino")
    
print("-------------------------------programa 2 netflix --------------------------------")
m1="le gusta la accion"
m1=True
if(m1==True):
    print("como le gusta la accion Recomendar mision final")
    #vio
    m2="spider hero"
    m2=True
    m3=input("¿viste battle? ")
    if(m2==True and m3=="si"):
        print("te gustan los super heroes")
        m4="le gustan los super heroes"
        m4=True 
        if(m4==True):
            print("recomendar amanecer mutante")
    
    else:
        print("no le gustan los super heroes")
        print ("recomendar otra cosa")
print("-------------------------------programa 3 hospital --------------------------------")

h1="paciente"
h1=True
h2="fiebre"
h2=True
h3="dolor de garganta"
h3=True
h4="estornudos"
h4=True
if(h2==True and h3==True):
    print("infeccion de garganta")
    h5="infeccion de garganta"
    h5=True

    if(h4==True and h2==False):
        print("alergia")
        h9="alergia"
        h9=True
        print("antihistaminico")  
            
if (h5==True and h2==True ):
    print("Posible Gripe") 
    h6="posible gripe"
    h6=True
if(h6==True and h4==True):
    print("Sospecha Gripe")
    h7="sospecha gripe"
    h7=True
                
if(h7==True):
    print("Prueba Influenza")
    h8="prueba influenza"
    h8=True
    
