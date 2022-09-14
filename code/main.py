from pyrae import dle
import json
import pandas as pd
# constants:
ESP_FILE_PATH = "../Vocabulary/Esp/vocabulario_esp.txt"
PATH_TO_SAVE = "../Vocabulary/Esp/"
# functions:

# Words manipulation


def get_word_list(file_path):

    with open(file=file_path, mode="r", encoding="utf-8") as words:
        words = words.readlines()
    words = [word.replace(",", "").strip().lower() for word in words]
    return words


# RAE API

def search_in_rae(word):

    rae = dle.search_by_word(word)
    rae = rae.to_dict()

    # Elements.
    if "articles" in rae:
        alternative_word = rae["articles"][0]["other_entries"]
        list_of_definitions = rae["articles"][0]["definitions"]
        number_of_definitions = len(list_of_definitions)
        if len(alternative_word) > 0 and number_of_definitions == 0:
            alternative_word = alternative_word[0]["text"].replace(
                ".", "").strip()
            print(f"buscando en palabra alternativa:\n '{alternative_word}'")
            word = alternative_word
            rae = dle.search_by_word(alternative_word)
            rae = rae.to_dict()
        etymology = rae["articles"][0]["supplementary_info"]
        list_of_responses = list()
        if len(etymology) > 0:
            etymology = rae["articles"][0]["supplementary_info"][0]["text"]
            list_of_responses = [{"etymology": etymology}]

        # estos están de nuevo por si cambia la palabra en el primer if.
        list_of_definitions = rae["articles"][0]["definitions"]
        number_of_definitions = len(list_of_definitions)
        if number_of_definitions > 0:
            for definition in range(number_of_definitions):
                definition_i = list_of_definitions[definition]
                definition_i_category = definition_i["category"]["text"]
                definition_i_sentence = definition_i["sentence"]["text"]
                definition_i_example = definition_i["examples"]
                definition_i_abbreviations = definition_i["abbreviations"]
                definition_i_category_al = []
                if len(definition_i_example) > 0:
                    definition_i_example = definition_i_example[0]["text"]
                if len(definition_i_abbreviations) > 0:
                    definition_i_category_al = definition_i_abbreviations[0]["text"]
                list_of_responses.append({"n": definition+1, "sentence": definition_i_sentence,
                                          "category": definition_i_category, "category_al": definition_i_category_al,
                                          "example": definition_i_example})
        else:
            list_of_responses = f"Algo falló con {word}, averigua."
    else:
        list_of_responses = f"'{word}' no está en el diccionario RAE. Pruebe una conjugación diferente."
    return list_of_responses


def get_answer(word):

    rae_response = search_in_rae(word=word)

    if isinstance(rae_response, list):
        if "etymology" in rae_response[0]:
            et_index = 0
            et = rae_response[et_index]["etymology"]
        else:
            et_index = -1
            et = "Desconocida"
        objects_index = et_index+1
    # Principals
        principal_definition = rae_response[objects_index]["sentence"]
        principal_category = rae_response[objects_index]["category"].capitalize(
        )
        # I decided to store all the alternatives, and examples.
        principal_alternative = []
        principal_example = []
    # Non principals.
        len_definitions = len(rae_response)
        # alternative
        if all(x == [] for x in principal_alternative):
            other_alternatives = []
            for index in range(objects_index, len_definitions):
                other_alternative = rae_response[index]["category_al"]
                other_alternatives.append(other_alternative)
            if all(x == [] for x in other_alternatives) or len(other_alternatives) == 0:
                principal_alternative = "No hay usos alternativos."
            else:
                principal_alternative = ",".join(
                    string for string in other_alternatives if len(string) > 0).split(",")
                used = set()
                principal_alternative = [x for x in principal_alternative if x not in used and (
                    used.add(x) or True)]
        # examples.
        if all(x == [] for x in principal_example):
            other_examples = []
            for index in range(objects_index, len_definitions):
                other_example = rae_response[index]["example"]
                other_examples.append(other_example)
            if all(x == [] for x in other_examples) or len(other_example) == 0:
                principal_example = "No hay ejemplos."
            else:
                principal_example = "".join(
                    string for string in other_examples if len(string) > 0).split(".")[:-1]

        if et != "Desconocida":
            if principal_example != "No hay ejemplos." and principal_alternative != "No hay usos alternativos.":
                answer = f"{et}\n{principal_category}\n{principal_alternative}\n{principal_definition}\n{principal_example}"
            elif principal_example == "No hay ejemplos." and principal_alternative != "No hay usos alternativos.":
                answer = f"{et}\n{principal_category}\n{principal_alternative}\n{principal_definition}"
            elif principal_example != "No hay ejemplos." and principal_alternative == "No hay usos alternativos.":
                answer = f"{et}\n{principal_category}\n{principal_definition}\n{principal_example}"
            else:
                answer = f"{et}\n{principal_category}\n{principal_definition}"
        else:
            if principal_example != "No hay ejemplos." and principal_alternative != "No hay usos alternativos.":
                answer = f"{principal_category}\n{principal_alternative}\n{principal_definition}\n{principal_example}"
            elif principal_example == "No hay ejemplos." and principal_alternative != "No hay usos alternativos.":
                answer = f"{principal_category}\n{principal_alternative}\n{principal_definition}"
            elif principal_example != "No hay ejemplos." and principal_alternative == "No hay usos alternativos.":
                answer = f"{principal_category}\n{principal_definition}\n{principal_example}"
            else:
                answer = f"{principal_category}\n{principal_definition}"
    else:
        answer = rae_response
    return answer


def create_cards(words):

    cards = []
    for word in words:
        answer = get_answer(word=word)
        card = {"answer": answer, "question": word}
        if "no está en el diccionario RAE. Pruebe una conjugación diferente." not in answer:
            cards.append(card)
    flash_cards_data = {
        "name": "Vocabulario Español. Python Made.",
        "cards": cards
    }
    return flash_cards_data


def save_to_json(data, file_name="flash_cards_esp.json"):
    with open(f"{PATH_TO_SAVE}{file_name}", mode="w") as json_file:
        json.dump(data, json_file, indent=2)
        print(
            f"Archivo json creado! en:\n {PATH_TO_SAVE}\n con el nombre de: {file_name}")


# Code execution:
if __name__ == '__main__':
    words = get_word_list(file_path=ESP_FILE_PATH)
    flash_cards_data = create_cards(words)
    save_to_json(data=flash_cards_data)
