def quadrado_geom(lado):
    """Retorna a área e o perímetro de um quadrado."""
    return {
        "area": lado ** 2,
        "perimetro": 4 * lado,
    }

if __name__ == "__main__":
    lado = 5.0
    resultado = quadrado_geom(lado)
    print(f"Lado: {lado}")
    print(resultado)