class Matrix:

    def __init__(self, rows, columns):

        if rows < 0 or columns < 0:
            raise Exception("Las dimensiones de una matriz deben ser positivas")
    
        self.rows = rows
        self.columns = columns
        self.values = []

        for i in range (rows):
            actual_row = []
            for i in range (columns):
                actual_row.append(0)
            self.values.append(actual_row)

    def __getitem__(self, pos):

        if(pos[0] < 0 or pos[0] >= self.rows or pos[1] < 0 or pos[1] >= self.columns):
            raise Exception("Indices fuera del rango de la Matriz")

        return self.values[pos[0]][pos[1]]

    def __setitem__(self, pos, new_value):

        if(pos[0] < 0 or pos[0] >= self.rows or pos[1] < 0 or pos[1] >= self.columns):
            raise Exception("Indices fuera del rango de la Matriz")

        self.values[pos[0]][pos[1]] = new_value


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
    
        return mul


    def __str__(self):

        value_return = ""

        for i in range (self.rows):
            for j in range (self.columns):
                value_return = value_return + str(self[i,j]) + " "
            value_return = value_return + "\n"

        return value_return