import time
import random

users = []
regtime = 36
extime = 18
logfile = "lotterylog.txt"

def save():
    with open(logfile, "w") as f:
        f.write("Users:\n")
        for u in users:
            f.write(u + "\n")

def register():
    start = time.time()
    extended = False

    while time.time() - start < regtime or extended:
        remain = int(regtime - (time.time() - start))
        
        if remain <= 0:
            print("\n⏳ Registration closed! Picking winner...\n")
            save()
            break

        if remain % 600 == 0:
            print(f"\n⏳ {remain // 60} min left")

        if time.time() - start >= regtime + (extime if extended else 0):
            print("\n⏳ Registration over! Picking winner...\n")
            save()
            break

        u = input("Username: ").strip()

        if u and time.time() - start < regtime + (extime if extended else 0) and u not in users:
            users.append(u)
            print(f"\n✅ '{u}' registered!\n")
        else:
            print("\n❌ Invalid or duplicate, or registration closed.\n")

        print(f"📢 Users: {len(users)}\n")

        if len(users) < 5 and not extended and time.time() - start >= regtime:
            print("\n⚠️ Extending registration.")
            extended = True
            start += extime

def pick():
    if users:
        winner = random.choice(users)
        print(f"\n🎉 Winner: {winner} 🎉\n🏆 Users: {len(users)}\n")

        with open(logfile, "a") as f:
            f.write(f"\nWinner: {winner}\n")
    else:
        print("\n🚫 No users, lottery canceled.\n")

def main():
    print("\n🎟️ Simple Lottery System! 🎟️\n")
    register()
    pick()

main()
