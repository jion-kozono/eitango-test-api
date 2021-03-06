from typing import List
from routers import word
from spreadsheet import sheet1, sheet2

from schemas import word as word_schema
from util.datetime import get_now

# 単語帳一覧取得
def getAllBooks():
    book_name_list_of_list = sheet1.get("F2:F")
    book_names = list(map(lambda book_name_list: book_name_list[0], book_name_list_of_list))
    filtered_book_names = list(set(book_names))
    return filtered_book_names

# 範囲内単語一覧取得
def getRangeWords(book_name: str, first: int, last: int, is_only_week: bool):
    list_of_dicts = sheet1.get_all_records()
    words = list(filter(lambda i: i["book_name"] == book_name and first <= i["word_num"] <= last and int(i["is_correct"]) == -1, list_of_dicts))\
        if is_only_week else list(filter(lambda i: i["book_name"] == book_name and first <= i["word_num"] <= last, list_of_dicts))
    # 最終学習時刻を更新
    if words:
        updateStudyTime(isTest=False)
    return words

# 苦手単語一覧取得
def getAllWeekWords():
    list_of_dicts = sheet1.get_all_records()
    if list_of_dicts:
        updateStudyTime(isTest=False)
    # 最終学習時刻を更新
    words = [i for i in list_of_dicts if i["is_correct"] == -1] # 内包表記で表してみた
    # words = list(filter(lambda i: i["is_correct"] == -1, list_of_dicts))
    if words:
        updateStudyTime(isTest=False)
    return words


def postIsCorrect(is_correct_dict_list: List[word_schema.PostIsCorrectInput]):
    cell_list_to_update = []
    for is_correct_dict in is_correct_dict_list:
        # idで該当箇所を検索
        id_cell = sheet1.find(is_correct_dict.id)
        is_correct_list = list(map(lambda y: y.is_correct, filter(lambda x: x.id == id_cell.value, is_correct_dict_list)))
        # 一つでも間違っていたらその単語は苦手になる
        if -1 in is_correct_list:
            is_correct_dict.is_correct = -1

        # 取得したidと同じ行のisCorrectを取得
        is_correct_cell = sheet1.acell(f'H{id_cell.row}')
        cell_value = int(is_correct_cell.value)
        print(type(is_correct_dict.is_correct))
        # 取得したisCorrectを解答のものと比較して、値を反転させるか判断
        is_correct_cell.value = (- cell_value) if cell_value != is_correct_dict.is_correct else 0
        if is_correct_cell.value != 0: # 値が変わらない場合は更新用配列に入れない
            cell_list_to_update.append(is_correct_cell)

    # まとめて更新
    if cell_list_to_update:
        sheet1.update_cells(cell_list_to_update)

    # 最終解答時刻を更新
    updateStudyTime(isTest=True)

def updateStudyTime(isTest: bool):
    now = get_now()
    update_col = 2 if isTest else 1
    sheet2.update_cell(2, update_col, now)