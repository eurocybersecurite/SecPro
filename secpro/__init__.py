# secpro/__init__.py
__version__ = "0.1.1"

import os
from pathlib import Path

class SecPro:
    """
    Moteur SecPro principal.
    Fournit l'analyse de fichiers et dossiers pour les vulnérabilités.
    """

    @staticmethod
    def scan_file(file_path: str):
        """
        Analyse un fichier Python et retourne un dictionnaire avec les problèmes détectés.
        Ici on simule l'analyse pour exemple ; tu peux intégrer ton moteur réel.
        """
        p = Path(file_path)
        issues = []

        if not p.exists():
            issues.append(f"Fichier {file_path} introuvable")
        elif p.is_file() and p.suffix == ".py":
            # Exemple d'analyse : recherche de 'eval' dans le code
            try:
                with open(p, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f, start=1):
                        if "eval(" in line:
                            issues.append(f"Ligne {i}: utilisation de eval()")
            except Exception as e:
                issues.append(f"Erreur lecture fichier: {e}")
        else:
            issues.append(f"Non analysé: {file_path} n'est pas un fichier .py")

        summary = {"lines": sum(1 for _ in open(file_path, "r", encoding="utf-8")) if p.exists() and p.is_file() else 0,
                   "warnings": len(issues)}

        return {"issues": issues, "summary": summary}

    def scan(self, path: str):
        """
        Scanne un fichier ou dossier entier
        """
        p = Path(path)
        all_results = []

        if p.is_file():
            all_results.append(self.scan_file(str(p)))
        elif p.is_dir():
            for f in p.rglob("*.py"):
                all_results.append(self.scan_file(str(f)))
        else:
            all_results.append({"issues": [f"Chemin introuvable: {path}"], "summary": {"lines":0,"warnings":1}})

        return all_results
