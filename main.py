import os, platform

def modo(select):
    if(select == '1'):
        file = input("Write the file name:\n")
        with open(file) as f:
            modulos=[]
            for line in f:
                line = line.strip("\n")
                modulos.append(line)
        print(modulos)
        for modulo in modulos:
            importar(modulo)
    if(select == '2'):
        modulos = input("Write the module names separated by commas:\n Example: numpy,pandas\n")
        modulos = modulos.split(",")
        for modulo in modulos:
            importar(modulo)
    if(select == '3'):
        if(platform.system() == 'Windows'):
            os.system("cls")
            print(platform.system())

        else:
            print(platform.system())
            os.system("clear")
        quit()
            
def importar(modulo):
    try:
        __import__(modulo)
        print(modulo + " is installed")
    except:
        print("Not Installed")
        install_yesno = input("Do you want to install " + modulo + "? yes or no\n")
        if(install_yesno == 'yes'):
            try:
                os.system("pip install "+modulo)
                print(modulo + " is now installed")
            except:
                print(modulo + " could not be installed")
print ("""
    1.Use a .txt file or a .* file, one module by line
    2.Manually write modules
    3.Exit/Quit
    """)
modo(input(""))
