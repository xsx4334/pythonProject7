# Creaza un program care va cere de la utilizator:
#
# Adresa de email
# Numele de utilizator
# Și va afisa aceasta infromatie in urmatorul format:
#
# Emailul pentru Marius a fost expediat cu succes pe adresa de email mariustricolici@hotmail.com
#
# Pentru adresa de email: mariustricolici@hotmail.com Si numele de utilizator: Marius

name = input("Introduceti numele de utilizator:")
print("Salut " + name)
email = input("Acum introduceti adresa de email:")
message = f"Emailul pentru {name} a fost expediat cu succes pe adresa de email {email} " \
          f"Pentru adresa de email: {email} Si numele de utilizator: {name}"
print(message)