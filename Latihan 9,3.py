with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

sentences = content.split(".")

unique_words = []

for sentence in sentences:
    words = sentence.strip().split()
    for word in words:
        word_cleaned = word.strip(".,?!\"';:-").lower()
        if word_cleaned not in unique_words:
            unique_words.append(word_cleaned)

print("======Isi Berita======")
print(content)

print("=======Kata Unik Pada Berita========")
print(unique_words)