
import ctypes as ct
import os


def main():
    lib_path = os.path.join(os.path.dirname(__file__), 'dllCircles_02.dll')
    lib = ct.CDLL(lib_path)
    #lib = ct.cdll.LoadLibrary(r"C:/Users/Eliza/Desktop/libCpp/dllCircles_02.dll" )
    FLOAT = ct.c_float
    DOUBLE = ct.c_double
    #PFLOAT = ct.POINTER(FLOAT)
    #INT = ct.c_int

    lib.calculatePositon.argtypes = [DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE]
    lib.calculatePositon.restype = ct.c_double

    lib.createTabOfPositions.argtypes = [DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE]
    #lib.calculatePositon.restype = ct.void

    sizeToPass = DOUBLE(5)
    result = lib.calculatePositon(sizeToPass, sizeToPass, sizeToPass, sizeToPass, sizeToPass)
    #print(""+str(result))

    #promień1, promień2, odległości między obiema środkami, PI, PI , całkowity czas, zmiana czasu!!
    result = lib.createTabOfPositions(6.0, 2.0, 7.0, 3.14, 3.14, 5.0, 0.01)

    #input()
    size = int(input("Podaj numer: "))


if __name__ == "__main__":
    main()
    #size = int(input("Podaj wartosc "))
