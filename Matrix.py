import re 

INDEX_PATT = r"^_(\d+)_(\d+)$"


class Matrix:

    def __init__(self, rows, columns):

        if rows < 0 or columns < 0:
            raise Exception("Las dimensiones de una matriz deben ser positivas")
    
        self.rows = rows
        self.columns = columns
        self.values = []

        for i in range (rows):
            actual_row = []
            for j in range (columns):
                actual_row.append(0)
            self.values.append(actual_row)
                

    def __getattr__(self, item):
        match = re.match( INDEX_PATT, item)
        if match:
            i = int(match.groups()[0])
            j = int(match.groups()[1])
            if(i < 0 or i >= self.rows or j < 0 or j >= self.columns):
                raise Exception("Indices fuera del rango de la Matriz")
            return self.values[i][j]
        return self.__getattribute__(item)

    def __setattr__(self, item, value):
        match = re.match( INDEX_PATT, item)
        if match:
            i = int(match.groups()[0])
            j = int(match.groups()[1])
            if(i < 0 or i >= self.rows or j < 0 or j >= self.columns):
                raise Exception("Indices fuera del rango de la Matriz")
            self.values[i][j] = value
        super().__setattr__(item,value)

    def __getitem__(self, pos):

        if(pos[0] < 0 or pos[0] >= self.rows or pos[1] < 0 or pos[1] >= self.columns):
            raise Exception("Indices fuera del rango de la Matriz")

        return self.values[pos[0]][pos[1]]

    def __setitem__(self, pos, new_value):

        if(pos[0] < 0 or pos[0] >= self.rows or pos[1] < 0 or pos[1] >= self.columns):
            raise Exception("Indices fuera del rango de la Matriz")

        self.values[pos[0]][pos[1]] = new_value

    def __iter__(self):
        return Iterator(self)


    def __add__(self, another):

        if self.rows != another.rows or self.columns != another.columns:
            raise("Solo se pueden sumar matrices con iguales dimensiones")

        sum = Matrix(self.rows, self.columns)

        for i in range (sum.rows):
            for j in range (sum.columns):
                sum[i,j] = self[i,j] + another[i,j]

        return sum


    def __sub__(self, another):

        if self.rows != another.rows or self.columns != another.columns:
            raise("Solo se pueden restar matrices con iguales dimensiones")

        sus = Matrix(self.rows, self.columns)

        for i in range (sus.rows):
            for j in range (sus.columns):
                sus[i,j] = self[i,j] - another[i,j]

        return sus


    def __mul__(self, another):
        if self.columns != another.rows:
            raise Exception("Deben coincidir la cantidad de columnas de la 1ra matriz con la cantidad de filas de la 2da")    

        mul = Matrix(self.rows, another.columns)

        for i in range (mul.rows):
            for j in range (mul.columns):
                actual_sum = 0
                for k in range (self.columns):
                    actual_sum = actual_sum + (self[i,k] * another[k, j])
                    mul[i,j] = actual_sum
    
        return mul


    def __str__(self):

        value_return = ""

        for i in range (self.rows):
            for j in range (self.columns):
                value_return = value_return + str(self[i,j]) + " "
            value_return = value_return + "\n"

        return value_return

class Iterator:

    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise Exception('Es un iterador de Matrix.')

        self.matrix = matrix
        self.current = 0

    def there_is_next(self):
        return self.current < self.matrix.rows * self.matrix.columns

    def __iter__(self):
        return self

    def __next__(self):
        if self.there_is_next():
            i = self.current // self.matrix.columns
            j = self.current % self.matrix.columns
            value = self.matrix.values[i][j]
            self.current += 1
            return value
        else:
            self.current = 0
            raise StopIteration('Terminamos de iterar')


if __name__ == '__main__':
    print("Bienvenido al tester de mi matris de python \nInicialmente creemos dos matrices")
    
    columnasA = int(input("cantidad de columnas de la matris A "))
    filasA = int(input("cantidad de filas de la matris A "))
    columnasB = int(input("cantidad de columnas de la matris B "))
    filasB = int(input("cantidad de filas de la matris B "))
    
    matrizA = Matrix(filasA,columnasA)
    matrizB = Matrix(filasB,columnasB)
    
    print("Ahora dame los valores de la matriz A")
    
    for i in range(filasA):
        print("dame los valores de la fila: " + str(i))
        for j in range(columnasA):
            matrizA[i,j] = int(input("valor de la  posicion " + str(j) + "," + str(i) + ":"))
    
    print("Ahora dame los valores de la matriz B")
    
    for i in range(filasB):
        print("dame los valores de la fila: " + str(i))
        for j in range(columnasB):
            matrizB[i,j] = int(input("valor de la  posicion " + str(j) + "," + str(i) + ":"))
    
    print("Matris A: \n" + str(matrizA))
    print("Matris B: \n" + str(matrizB))
    print("Matris A + B: \n" + str(matrizA + matrizB))
    print("Matris A - B: \n" + str(matrizA - matrizB))
    print("Matris A * B: \n" + str(matrizA * matrizB))

    print("Iterando matriz A")
    iterator = iter(matrizA)
    while True:
        try:
            current = next(iterator)
            print(current, end=' ')
        except StopIteration:
            print()
            break

    print("Iterando matriz B")
    for i in matrizB:
        print(i, end=' ')

    

  
 


