import os
import json

folder = "followers_and_following"

seguidores = set()
seguindo = set()

for filename in os.listdir(folder):
    if filename.endswith(".json"):
        filepath = os.path.join(folder, filename)
        print("==================================================")
        print(f"Arquivo: {filename}")
        print("==================================================")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                valores_arquivo = []
                
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict) and "string_list_data" in item:
                            for string_item in item["string_list_data"]:
                                if "value" in string_item:
                                    valor = string_item["value"]
                                    print(valor)
                                    valores_arquivo.append(valor)
                
                elif isinstance(data, dict):
                    for key in data:
                        if isinstance(data[key], list):
                            for item in data[key]:
                                if isinstance(item, dict) and "string_list_data" in item:
                                    for string_item in item["string_list_data"]:
                                        if "value" in string_item:
                                            valor = string_item["value"]
                                            print(valor)
                                            valores_arquivo.append(valor)
                
                if "followers" in filename.lower():
                    seguidores.update(valores_arquivo)
                elif "following" in filename.lower():
                    seguindo.update(valores_arquivo)
                    
        except Exception as e:
            print(f"Erro ao ler {filename}: {e}")

nao_me_seguem = seguindo - seguidores

print("==================================================")
print("Arquivo: Pessoas que não te seguem de volta")
print("==================================================")
for pessoa in sorted(nao_me_seguem):
    print(pessoa)

print("==================================================")
print("RELATÓRIO DE ANÁLISE")
print("==================================================")
print(f"Total de pessoas que você segue: {len(seguindo)}")
print(f"Total de seus seguidores: {len(seguidores)}")
print(f"Pessoas que não te seguem de volta: {len(nao_me_seguem)}")
