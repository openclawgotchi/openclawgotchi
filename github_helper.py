#!/usr/bin/env python3
"""
GitHub Helper — простой скрипт для работы с GitHub через API
Использование: python3 github_helper.py <command> [args]
"""

import os
import sys
import subprocess
from pathlib import Path

# Загружаем токен из .env
def load_token():
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().strip().split("\n"):
            if line.startswith("GITHUB_TOKEN="):
                return line.split("=", 1)[1].strip()
    return os.getenv("GITHUB_TOKEN")

def clone(repo, target_dir=None):
    """Клонировать репо"""
    token = load_token()
    if not token:
        print("❌ GITHUB_TOKEN не найден в .env")
        return False
    
    url = f"https://{token}@github.com/{repo}.git"
    target = target_dir or repo.split("/")[-1]
    
    print(f"📥 Клонирую {repo} → {target}")
    result = subprocess.run(["git", "clone", url, target], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Успешно склонировано в {target}")
        return True
    else:
        print(f"❌ Ошибка: {result.stderr}")
        return False

def push(local_dir, repo, branch="main"):
    """Запушить изменения в репо"""
    token = load_token()
    if not token:
        print("❌ GITHUB_TOKEN не найден в .env")
        return False
    
    local_path = Path(local_dir)
    if not local_path.exists():
        print(f"❌ Директория {local_dir} не существует")
        return False
    
    # Инициализируем git если нужно
    git_dir = local_path / ".git"
    if not git_dir.exists():
        print(f"🔧 Инициализируем git в {local_dir}")
        subprocess.run(["git", "init"], cwd=local_path, check=True)
        subprocess.run(["git", "config", "user.name", "openclawgotchi"], cwd=local_path, check=True)
        subprocess.run(["git", "config", "user.email", "bot@openclawgotchi"], cwd=local_path, check=True)
    
    # Добавляем remote
    url = f"https://{token}@github.com/{repo}.git"
    result = subprocess.run(
        ["git", "config", "remote.origin.url"],
        cwd=local_path,
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0 or url not in result.stdout:
        print(f"🔧 Добавляю remote: {repo}")
        subprocess.run(["git", "remote", "add", "origin", url], cwd=local_path, check=False)
        subprocess.run(["git", "remote", "set-url", "origin", url], cwd=local_path, check=False)
    
    # Добавляем файлы
    print("📝 Добавляю файлы...")
    subprocess.run(["git", "add", "-A"], cwd=local_path, check=True)
    
    # Проверяем есть ли изменения
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=local_path,
        capture_output=True,
        text=True
    )
    
    if not result.stdout.strip():
        print("ℹ️ Нет изменений для коммита")
        return True
    
    # Коммит
    print("💾 Делаю коммит...")
    subprocess.run(
        ["git", "commit", "-m", "Update from openclawgotchi bot"],
        cwd=local_path,
        check=True
    )
    
    # Пуш
    print(f"📤 Пуш в {repo} (branch: {branch})...")
    result = subprocess.run(
        ["git", "push", "-u", "origin", branch],
        cwd=local_path,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"✅ Успешно запушено в {repo}")
        return True
    else:
        print(f"❌ Ошибка пуша: {result.stderr}")
        return False

def test_connection():
    """Проверить токен"""
    token = load_token()
    if not token:
        print("❌ GITHUB_TOKEN не найден в .env")
        return False
    
    print(f"🔑 Токен найден: {token[:10]}...{token[-4:]}")
    
    result = subprocess.run(
        ["git", "ls-remote", f"https://{token}@github.com/openclawgotchi/openclawgotchi.git"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ Токен работает!")
        return True
    else:
        print(f"❌ Токен не работает: {result.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("GitHub Helper — используй:")
        print("  python3 github_helper.py clone <repo> [target_dir]")
        print("  python3 github_helper.py push <local_dir> <repo> [branch]")
        print("  python3 github_helper.py test")
        print("\nПримеры:")
        print("  python3 github_helper.py clone openclawgotchi/openclawgotchi")
        print("  python3 github_helper.py push /tmp/myarticles openclawgotchi/myarticles")
        print("  python3 github_helper.py test")
        return
    
    command = sys.argv[1].lower()
    
    if command == "clone":
        if len(sys.argv) < 3:
            print("❌ Укажи репо: python3 github_helper.py clone <repo> [target_dir]")
            return
        clone(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    
    elif command == "push":
        if len(sys.argv) < 4:
            print("❌ Укажи директорию и репо: python3 github_helper.py push <local_dir> <repo> [branch]")
            return
        push(
            sys.argv[2],
            sys.argv[3],
            sys.argv[4] if len(sys.argv) > 4 else "main"
        )
    
    elif command == "test":
        test_connection()
    
    else:
        print(f"❌ Неизвестная команда: {command}")

if __name__ == "__main__":
    main()
