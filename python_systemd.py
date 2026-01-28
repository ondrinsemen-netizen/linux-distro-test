#!/usr/bin/env python3
import sys
import time

def red(text):
    return f"\033[91m{text}\033[0m"

print(red("ВНИМАНИЕ ВАШ КОМПЬЮТЕР ЗАРАЖЁН НАНОВИРУСОМ SYSTEMD💀🔥💀"))
print(red("СРОЧНО ПЕРЕЙДИТЕ НА СИСТЕМУ БЕЗ ВИРУСА SYSTEMD"))
print(red("ИЛИ ВАШ КОМПЬЮТЕР ВЗОРВЁТСЯ"))
print()

while True:
    choice = input("продолжить? (y/n): ").lower()
    
    if choice in ['y', 'д']:
        print(red("\n💀 НЕМЕДЛЕННО УДАЛЯЮ SYSTEMD..."))
        time.sleep(1)
        
        for i in range(1, 4):
            print(f"[{i}] Удаляю systemd-{['journald', 'resolved', 'networkd'][i-1]}...")
            time.sleep(0.5)
        
        print(red("\n✅ SYSTEMD УДАЛЁН!"))
        print("🐧 Теперь используйте OpenRC или runit!")
        print("P.S. можете проверить командой systemctl status systemd ")
        break
        
    elif choice in ['n', 'н']:
        print(red("\n💥 ВАШ КОМПЬЮТЕР ВЗОРВЕТСЯ ЧЕРЕЗ:"))
        for i in range(3, 0, -1):
            print(red(f"{i}..."))
            time.sleep(1)
        
        for _ in range(5):
            print(red("💥 БАХ! " * 5))
            time.sleep(0.1)
        
        print(red("\n💀 КОМПЬЮТЕР УНИЧТОЖЕН SYSTEMD"))
        break
        
    else:
        print(red("⚠️  ОТВЕТЬТЕ y ИЛИ n! SYSTEMD ВАС ЗАПУТАЛ?"))
