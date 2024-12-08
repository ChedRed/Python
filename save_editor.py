from SavConverter import read_sav, sav_to_json

props = read_sav("/Users/ryanchou/Library/Application Support/Epic/ES2/Saved/SaveGames/ThisThat_PREVIEW_.sav")
json_data = sav_to_json(props, string=True)
print(json_data)
