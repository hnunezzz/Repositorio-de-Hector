'''
Héctor de Jesús Núñez Avena
Grupo 5-3
Sistemas distribuidos
Rotación de eje en un vector

'''
import numpy as np


def rot_x(x, y, z, theta):
    '''
    Rota un punto 3D alrededor del eje X un ángulo theta.

    Parameters:
        x (float): es la coordenada en el eje X del punto original
        y (float): es la coordenada en el eje Y
        z (float): es la coordenada en el eje Z
        theta (float): es el ángulo de rotación en radianes

    Returns:
        np.ndarray: regresa el vector rotado como array de numpy de dimensión (3,).
    '''
    punto = np.array([x, y, z]) # guardamos en la variable punto un vector numpy con x, y, z
    R = np.array([[1, 0, 0],
                  [0, np.cos(theta), -np.sin(theta)], # np.cos para calcular cosenos y np.sin para calcular senos
                  [0, np.sin(theta),  np.cos(theta)]])
    return R @ punto # se usa @ para hacer una multiplicación matricial y retornamos un nuevo vector ya rotado


def rot_y(x, y, z, theta):
    '''
    Rota un punto 3D alrededor del eje Y un ángulo theta.

    Parameters:
        x (float): es la coordenada en el eje X
        y (float): es la coordenada en el eje Y
        z (float): es la coordenada en el eje Z
        theta (float): es el ángulo de rotación en radianes

    Returns:
        np.ndarray: vector rotado como array de numpy de dimensión (3,).
    '''
    punto = np.array([x, y, z])
    R = np.array([[ np.cos(theta), 0, np.sin(theta)],
                  [0, 1, 0],
                  [-np.sin(theta), 0, np.cos(theta)]])
    return R @ punto


def rot_z(x, y, z, theta):
    '''
    Rota un punto 3D alrededor del eje Z un ángulo theta.

    Parameters:
        x (float): es la coordenada en el eje X
        y (float): es la coordenada en el eje Y
        z (float): es la coordenada en el eje Z
        theta (float): es el ángulo de rotación en radianes

    Returns:
        np.ndarray: vector rotado como array de numpy de dimensión (3,).
    '''
    punto = np.array([x, y, z])
    R = np.array([[np.cos(theta), -np.sin(theta), 0],
                  [np.sin(theta),  np.cos(theta), 0],
                  [0, 0, 1]])
    return R @ punto


def rotar(x, y, z, theta, axis):
    '''
    Rota un punto 3D alrededor de un eje especificado ('x', 'y' o 'z').

    Parameters:
        x (float): es la coordenada en el eje X
        y (float): es la coordenada en el eje Y
        z (float): es la coordenada en el eje Z
        theta (float): es el ángulo de rotación en radianes
        axis (str): eje de rotacion; puede tomar valor 'x', 'y' o 'z'.

    Returns:
        np.ndarray: vector rotado dependiendo el valor de axis como array de numpy de dimensión (3,).
    '''
    axis = axis.lower() # usamos lower para aceptar tanto minusculas como mayusculas
    if axis == 'x':
        return rot_x(x, y, z, theta)
    elif axis == 'y':
        return rot_y(x, y, z, theta)
    elif axis == 'z':
        return rot_z(x, y, z, theta)
    else:
        raise ValueError("El eje debe ser 'x', 'y' o 'z'") # indicamos un ValueError en caso de que el usuario no introduzca los caracteres deseados


#Pruebas

if __name__ == "__main__":
    
    punto = (1, 0, 0) # vector original

    grados = 90 # angulo en grados
    
    theta = np.deg2rad(grados)  # conversión a radianes

    print(f"Vector original: {punto}")

    print("Rotación en Z 90°:", np.round(rotar(*punto, theta, 'z'), 4)) # Rotación en Z (usamos np.round a 4 decimales para redondear numeros y de un 0 cerrado)
    
    print("Rotación en Y 90°:", np.round(rotar(*punto, theta, 'y'), 4)) # Rotación en Y 
    
    print("Rotación en X 90°:", np.round(rotar(*punto, theta, 'x'), 4)) # Rotación en X 
