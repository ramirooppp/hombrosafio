import os
import json
import hashlib

REPO_OWNER = "ramirooppp"
REPO_NAME = "hombrosafio"
BRANCH = "main"

def generate_manifest():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mods_dir = os.path.join(base_dir, "mods")
    
    if not os.path.exists(mods_dir):
        print(f"[Error] La carpeta de mods no existe en: {mods_dir}")
        return

    mods = []
    for f in sorted(os.listdir(mods_dir)):
        if f.endswith(".jar"):
            path = os.path.join(mods_dir, f)
            with open(path, "rb") as fp:
                sha1 = hashlib.sha1(fp.read()).hexdigest()
            size = os.path.getsize(path)
            
            raw_url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/mods/{f}"
            mods.append({
                "name": f,
                "sha1": sha1,
                "size": size,
                "url": raw_url,
                "required": True
            })

    manifest = {
        "pack_name": "Hombrosafio 4",
        "pack_version": "0.14.0",
        "game_version": "26.3",
        "loader_version": "0.19.5",
        "server_ip": "158.23.58.93:25565",
        "java_version": "25",
        "mods": mods
    }

    manifest_path = os.path.join(base_dir, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as fp:
        json.dump(manifest, fp, indent=2, ensure_ascii=False)

    print(f"[OK] Manifest actualizado con éxito para {REPO_OWNER}/{REPO_NAME} ({len(mods)} mods) en: {manifest_path}")

if __name__ == "__main__":
    generate_manifest()
