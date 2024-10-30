'''
EJERCICIO 13: Escribe un programa para leer un archivo e imprime el contenido del mismo (línea por línea) todo en mayúsculas. Ejecutando el programa se verá como sigue:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: POSTMASTER@COLLAB.SAKAIPROJECT.ORG
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500

Puedes descargar el archivo desde
www.py4e.com/code3/mbox-short.txt
'''

def main():
    file_name = input('Enter a file name: ')
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.upper().strip())
    except FileNotFoundError:
        print('File not found')

if __name__ == '__main__':
    main()