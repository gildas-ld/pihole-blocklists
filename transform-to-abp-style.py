import re

def read_domains(file_path):
    with open(file_path, "r") as file:
        domains = file.readlines()
    domains = [domain.strip() for domain in domains]
    return domains

# Transformer les domaines
def transform_domains(domains):
    transformed_domains = set()
    for domain in domains:
        # Extraire le domaine principal
        main_domain = re.findall(r"[^.]+\.[^.]+$", domain)
        if main_domain:
            transformed_domains.add(f"||{main_domain[0]}^")
    return transformed_domains

def write_transformed_domains(file_path, transformed_domains):
    with open(file_path, "w") as file:
        for domain in transformed_domains:
            file.write(domain + "\n")

input_file = "./to_transform.txt"
output_file = "./transformed_domains.txt"

domains = read_domains(input_file)

transformed_domains = transform_domains(domains)

write_transformed_domains(output_file, transformed_domains)

print(f"OK.")
