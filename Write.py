with open('text.txt', 'r') as reader:
    content = reader.readlines() # [Amma, Anna, Akka, nanu , ammu, ME]
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


