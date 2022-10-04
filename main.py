from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtyle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)