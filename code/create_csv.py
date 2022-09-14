import pandas as pd

# CONSTANTS.
path_to_json_data = "../Vocabulary/Esp/flash_cards_esp.json"
path_to_csv_data = "../Vocabulary/Esp/flash_cards_esp.csv"
# Reading data.
vocabulary_data = pd.read_json(path_or_buf=path_to_json_data)

# Normalizing cards.
cards = pd.json_normalize(vocabulary_data["cards"])

# Sorting variables.
cards = cards[["question", "answer"]]

cards.to_csv(path_or_buf=path_to_csv_data, index=False, encoding="utf-8-sig")
