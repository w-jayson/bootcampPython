contatos = {"weslley@gmail.com": {"nome": "Weslley", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["weslley@gmail.com"] = {"nome": "Wes"}

print(contatos["weslley@gmail.com"])  # {"nome": "Weslley", "telefone": "3333-2221"}

print(copia["weslley@gmail.com"])  # {"nome": "Wes"}
