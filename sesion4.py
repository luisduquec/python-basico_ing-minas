#!/usr/bin/env python
# coding: utf-8

# # Introduccion a las Funciones

# ## Sintaxis

# 1. La palabra clave/reservada def
# 2. Nombre apropiado para llamar o invocar a nuestra funcion
# 3. Uso de parentesis "( )" e introducir los parametros de nuestra funcion en caso de ser necesarios (opcionales)
# 4. Dos puntos ":"
# 5. Bloque de codigo a ejecutar
# 6. Sentencia de retorno

# In[ ]:


def cubo(n):
    n3 = n**3
    print(n3)


# In[ ]:


#cubo(5)


# ## Funcion a partir de bloque de codigo (Sesion3)

# In[ ]:


asignaciones = {"juan":["nivel 1", "nivel 2", "nivel 3"], "sara":["nivel 4","nivel 5", "nivel 6"], "pedro":["nivel 7", "nivel 8", "nivel 9", "nivel 10"]}
tope = 3

def fun_asignaciones(asignaciones, tope):
    
    for s in asignaciones:
        print("el nombre de nuestro supervisor/a es:",s)
        print("los niveles asignados son:",asignaciones[s])
        if len(asignaciones[s]) > tope:
            print("por favor acudir con tu superior, puesto que tienes muchos niveles asignados")
        else:
            print("la cantidad de nieveles asignados está ok")
        print("")

#fun_asignaciones(asignaciones, tope)


# ## Probando nuestra Funcion (2 parametros)

# In[ ]:


asignaciones2 = {"juana":["nivel 0", "nivel 1", "nivel 2"], "andrea":["nivel 3","nivel 4"], "cristian":["nivel 5", "nivel 6", "nivel 7", "nivel 8"]}
tope2 = 3

#fun_asignaciones(asignaciones2, tope2)


# ## Funcion asignaciones_supervisor v1

# In[ ]:


def asignaciones_supervisor_v1():
    nombre = input("Ingrese nombre del supervisor: ")
    can_niv = int(input("¿Cuantos niveles tendra el supervisor?: "))
    niveles_supervisor = {nombre:[]}
    
    i=0
    while (i<can_niv):
        nom_nivel = input("Ingrese el nombre de un nivel: ")
        niveles_supervisor[nombre] = niveles_supervisor[nombre] + [nom_nivel]
        i=i+1
    return(niveles_supervisor)


# ## Probando nuestra Funcion asignaciones_supervisor v1

# In[ ]:


#victor = asignaciones_supervisor_v1()


# In[ ]:


#victor


# ## Funcion asignaciones_supervisor v2

# In[ ]:


def asignaciones_supervisor_v2():
    general={}
    can_sup= int(input("Ingrese la cantidad de supervisores: "))
    for i in range(0,can_sup):
        nombre = input("Ingrese nombre del supervisor: ")
        can_niv= int(input("¿Cuantos niveles tendra a su cargo?: "))
        niveles_supervisor = {nombre:[]}
        i=0
        while i < can_niv:
            nom_nivel= input("Ingrese el nombre del nivel: ")
            niveles_supervisor[nombre] = niveles_supervisor[nombre] +  [nom_nivel]
            i = i + 1
        general.update(niveles_supervisor)
    return(general)
#asignaciones_supervisor_v2()


# ## Funcion asignaciones_supervisor v3

# In[ ]:


def asignaciones_supervisor_v3():
    general = {}
    while True:
        nombre = input("Ingrese nombre del supervisor: ")
        niveles =[]
        niveles_supervisor = {nombre:niveles}
        while True:
            nom_nivel= input("Ingrese el nombre del nivel: ")
            niveles.append(nom_nivel)
            parar_ni = input("¿Desea suspender el ingreso de niveles? (s/n): ")
            if (parar_ni == "s"):
                break
            elif (parar_ni =="n"):
                pass
        general.update(niveles_supervisor)
        
        parar_sup = input("¿Desea suspender el ingreso de supervisores? (s/n): ")
        if (parar_sup =="s"):
            break
        elif (parar_sup =="n"):
            pass
            
    return(general)
#asignaciones_supervisor_v3()

