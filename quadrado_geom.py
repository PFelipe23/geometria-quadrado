def quadrado_geom(lado):
    """Retorna a área de um quadrado em um dicionário."""
    return {"area": lado ** 2}


if __name__ == "__main__":
    lado = 5.0
    resultado = quadrado_geom(lado)
    print(f"Lado: {lado}")
    print(resultado)
