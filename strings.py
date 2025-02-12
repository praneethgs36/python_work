#favorite_language = "python   "
#favorite_language = favorite_language.rstrip()

#print(f"{favorite_language} is nice")

bitcoin_url = "https//:bitcoin.org"
bitcoin_url = bitcoin_url.removeprefix("https//:")
#print(bitcoin_url)
bitcoin_url = bitcoin_url.removesuffix(".org")

print(bitcoin_url)
