import random, csv, os, string

os.makedirs("data", exist_ok=True)
OUT = "data/passwords.csv"
N = 5000    #number of passwords to generate

def make_password(strength):

    #Weak password
    if strength == 'weak':
        choices = ["password", "123456", "qwerty", "abc123", "letmein", "itsme"]
        base = random.choice(choices)
        tail = ''.join(random.choices(string.digits, k=random.randint(0,3)))
        return base + tail
    
    #Medium password
    if strength == 'medium':
        s = ''.join(random.choices(string.digits, k=random.randint(0,3)))
        if random.random() < 0.3:
            s = s.capitalize()
        if random.random() <0.2:
            s += random.choice("!@#$%")
        return s
    
    #Strong password
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>?"
    return ''.join(random.choices(chars, k=random.randint(12,20)))

rows = []
for _ in range(N):
    r = random.random()
    if r < 0.45:
        lab = "weak"
    elif r < 0.9:
        lab = "medium"
    else:
        lab = "strong"
    pwd = make_password(lab)
    rows.append((pwd, lab))

with open(OUT, "w", newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["password", "label"])
    w.writerows(rows)

print(f"[+] wrote {len(rows)} password to {OUT}")