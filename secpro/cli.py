#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
from secpro import SecPro  
from termcolor import colored

def analyze_file(file_path: Path):
    """
    Analyse réelle d'un fichier avec SecPro.
    Retourne un dictionnaire avec 'issues' et 'summary'.
    """
    try:
        
        result = SecPro.scan_file(str(file_path))  
        return result
    except Exception as e:
        return {
            "issues": [f"Erreur lors de l'analyse: {e}"],
            "summary": {"lines": 0, "warnings": 0}
        }

def scan_target(target_path: str):
    """
    Scanne un dossier ou un fichier.
    """
    p = Path(target_path)
    all_results = []

    if not p.exists():
        print(colored(f"Erreur: le chemin {target_path} n'existe pas.", "red"))
        return

    files_to_scan = [p] if p.is_file() else list(p.rglob("*.py"))

    for file_path in files_to_scan:
        print(colored(f"Analyse de {file_path} ...", "cyan"))
        result = analyze_file(file_path)
        all_results.append(result)

        for issue in result.get("issues", []):
            print(colored(f"  - {issue}", "yellow"))

    # Résumé global
    total_files = len(files_to_scan)
    total_issues = sum(len(r.get("issues", [])) for r in all_results)
    print("\n" + colored("=== Résumé du scan ===", attrs=["bold"]))
    print(colored(f"Fichiers analysés : {total_files}", "green"))
    print(colored(f"Total problèmes détectés : {total_issues}", "red" if total_issues > 0 else "green"))

def main():
    parser = argparse.ArgumentParser(description="SecPro CLI - Audit de sécurité automatisé")
    parser.add_argument("command", choices=["scan"], help="Commande à exécuter")
    parser.add_argument("--target", "-t", required=True, help="Fichier ou dossier à analyser")
    args = parser.parse_args()

    if args.command == "scan":
        scan_target(args.target)
    else:
        print("Commande non reconnue")

if __name__ == "__main__":
    main()
