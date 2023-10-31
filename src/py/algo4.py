def restore_genome(n, fragments):
    genome = ""
    for fragment in fragments:
        for letter in fragment:
            if letter not in genome:
                genome += letter
    return genome

n = int(input("Enter the number of genome fragments: "))
fragments = []
for _ in range(n):
    fragments.append(input("Enter a fragment: "))

genome = restore_genome(n, fragments)
print("Reconstructed genome: ", genome)