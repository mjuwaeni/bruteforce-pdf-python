import PyPDF2

pdf_file = 'dokumen.pdf'
wordlist_file = 'wordlist.txt'

with open(wordlist_file, 'r') as f:
    passwords = f.read().splitlines()

for password in passwords:
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            result = reader.decrypt(password)
            if result:
                print(f"[✓] Password ditemukan: {password}")
                break
            else:
                print(f"[-] Salah: {password}")
    except Exception as e:
        print(f"[!] Error saat membuka PDF: {e}")
