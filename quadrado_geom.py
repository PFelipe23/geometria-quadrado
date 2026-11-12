from math import sqrt


def quadrado_geom(lado):
    """Retorna a área, o perímetro e a diagonal de um quadrado de lado positivo."""
    if lado <= 0:
        raise ValueError("O lado deve ser positivo.")

    return {
        "area": lado ** 2,
        "perimetro": 4 * lado,
        "diagonal": lado * sqrt(2),
    }

if __name__ == "__main__":
    lado = 5.0
    resultado = quadrado_geom(lado)
    print(f"Lado: {lado}")
    print(resultado)