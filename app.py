#!/usr/bin/env python3
"""
Mon premier fichier Python versionné avec Git !
"""

def saluer(nom: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour {nom} ! Bienvenue dans le monde de Git 🎉"

def calculer_somme(a: int, b: int) -> int:
    """Additionne deux nombres."""
    return a + b

def multiplier(a: int, b: int) -> int:
    """Multiplie deux nombres."""
    return a * b

def diviser(a: int, b: int) -> float:
    """Divise deux nombres avec gestion de la division par zéro."""
    if b == 0:
        raise ValueError("Impossible de diviser par zéro !")
    return a / b

if __name__ == "__main__":
    print(saluer("Développeur"))
    print(f"2 + 3 = {calculer_somme(2, 3)}")
    print(f"4 × 5 = {multiplier(4, 5)}")
    print(f"10 ÷ 2 = {diviser(10, 2)}")
    # TODO: Ajouter plus d'opérations

