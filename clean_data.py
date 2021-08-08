cleaned = []

with open('data.csv', 'r') as f:
    lines = f.readlines()

    for line in lines:
        if line.strip() != ',':
            cleaned.append(line)

with open('cleaned_data.csv', 'w') as f:
    f.writelines(cleaned)