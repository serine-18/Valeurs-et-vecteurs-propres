import numpy as np

def PuissanceItérée(A, tolérance, nombre_max_iterations):
    n = len(A)
    # Vecteur aléatoire de taille n
    vecteur_initial = np.random.rand(n)
    lambda_prev = 0
    
    for iteration in range(1, nombre_max_iterations + 1):
        # Calcul du vecteur propre estimé
        vecteur_propre_estimé = np.dot(A, vecteur_initial)
        
        # Calcul de la valeur propre estimée
        lambda_estimé = np.dot(vecteur_initial, vecteur_propre_estimé)
        
        # Normalisation du vecteur propre estimé
        vecteur_initial = vecteur_propre_estimé / np.linalg.norm(vecteur_propre_estimé)
        
        # Vérification de la tolérance
        if abs(lambda_estimé - lambda_prev) < tolérance:
            return lambda_estimé, vecteur_initial
        
        lambda_prev = lambda_estimé
    
    return lambda_estimé, vecteur_initial

def Déflation(A, lambda_val, vecteur_propre):
    n = len(A)
    # Calcul de la matrice déflattée B
    B = A - lambda_val * np.outer(vecteur_propre, vecteur_propre)
    
    # Appliquer la méthode de la puissance itérée à la matrice déflattée B
    lambda2, vecteur2 = PuissanceItérée(B, tolerance, max_iterations)
    
    return lambda2, vecteur2


def fill_matrix():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        matrix = np.zeros((rows, cols))

        print("Enter matrix elements row-wise:")
        for i in range(rows):
            for j in range(cols):
                matrix[i, j] = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))

        return matrix

    except:
        print("Error")
        return None

# Exemple d'utilisation
# Remplacez la matrice A par votre matrice symétrique
A = fill_matrix()  

tolerance = float(input("Enter the tolerance: ")) 
max_iterations = int(input("Enter the number of iterations: ")) 

 
lambda1, vecteur1 = PuissanceItérée(A, tolerance, max_iterations)
B = A - lambda1 * np.outer(vecteur1 , vecteur1 )
lambda2, vecteur2 = Déflation(A, lambda1, vecteur1)
lambda3, vecteur3 = Déflation(B, lambda2, vecteur2)

print("Valeur propre 1:", lambda1)
print("Vecteur propre 1:", vecteur1)
print("Valeur propre 2:", lambda2)
print("Vecteur propre 2:", vecteur2)
print("Valeur propre 3:", lambda3)
print("Vecteur propre 3:", vecteur3)