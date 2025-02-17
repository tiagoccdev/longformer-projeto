import os
import gdown

# Criar pasta local caso não exista
os.makedirs("C:/longformer", exist_ok=True)

# Lista de arquivos para baixar (substitua SEU_ID_AQUI pelos IDs reais)
arquivos = {
    "requirements.txt": "https://drive.google.com/uc?id=1--BnPNJcApYG78CkGenKDo1QINgiCBZ5",
    "project-rotulado.json": "https://drive.google.com/uc?id=1bO4nfXWgHagpG0G8SEsi7ezkSkCz-Ifs"
}

# Baixar arquivos
for nome, url in arquivos.items():
    output = f"C:/longformer/{nome}"
    gdown.download(url, output, quiet=False)

print("✅ Arquivos baixados para C:/longformer com sucesso!")
