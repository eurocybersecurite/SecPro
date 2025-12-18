#!/usr/bin/env python3
import argparse
import os
import json
from secpro import audit  # Supposons que ton module principal s'appelle audit

def scan(target_path):
    """
    Parcourt tous les fichiers du dossier target_path
    et applique les fonctions d'audit de SecPro.
    """
    results = []

    if not os.path.exists(target_path):
        print(f"[Error] Le chemin {target_path} n'existe pas.")
        return

    for root, dirs, files in os.walk(target_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Appelle la fonction d'audit principale (à adapter selon ton code)
            try:
                report = audit.analyze_file(file_path)  # <-- ton code SecPro ici
                results.append({
                    "file": file_path,
                    "issues": report.get("issues", []),
                    "summary": report.get("summary", {})
                })
            except Exception as e:
                results.append({
                    "file": file_path,
                    "error": str(e)
                })

    # Affichage lisible
    print(json.dumps(results, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(
        description="SecPro CLI - Audit et remédiation cybersécurité"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Commande scan
    scan_parser = subparsers.add_parser(
        "scan", help="Scanner un dossier ou fichier pour audit SecPro"
    )
    scan_parser.add_argument(
        "--target", "-t", required=True, help="Chemin vers le dossier ou fichier à analyser"
    )

    args = parser.parse_args()

    if args.command == "scan":
        scan(args.target)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
