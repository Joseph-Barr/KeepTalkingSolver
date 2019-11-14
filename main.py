from .models import SimonSays, Bomb, Passwords

# Main loop
b = Bomb()
b.serialVowel = True
b.strikes = 1
s = SimonSays(b)
s.solve()
s.__repr__()
