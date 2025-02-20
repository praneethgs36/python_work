prompt = "How many people are in your dinnner group?"
head_count = int(input(prompt))

if head_count > 8:
    print("\nPlease wait for 15 minutes.")
elif head_count <= 8:
    print("\nYour table is ready. Bon Apetit!")