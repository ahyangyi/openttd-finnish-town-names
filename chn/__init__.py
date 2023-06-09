# source of table:
# https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%96%E8%AA%9E%E8%AD%AF%E9%9F%B3%E8%A1%A8/%E8%8A%AC%E8%98%AD%E8%AA%9E

import re

cons = ["", "b", "c", "d", "f", "g", "h", "j y", "ck kk k", "l ll hl", "m mm", "n", "p pp", "r rr", "s ss z", "t th dt", "v w", "x", "ts tz z"]
vowels = [
    ["", "", "布", "克", "德", "夫", "格", "赫", "伊", "克", "尔", "姆", "恩", "普", "尔", "斯", "特", "夫", "克斯", "茨"],
    ["a aa", "阿", "巴", "卡", "达", "法", "加", "哈", "亚", "卡", "拉", "马", "纳", "帕", "拉", "萨", "塔", "瓦", "克萨", "察"],
    ["ä ää ae e ee", "埃", "贝", "塞", "代", "费", "盖", "海", "耶", "凯", "莱", "梅", "内", "佩", "雷", "塞", "泰", "韦", "克塞", "采"],
    ["an", "安", "班", "坎", "丹", "凡", "甘", "汉", "扬", "坎", "兰", "曼", "南", "潘", "兰", "桑", "坦", "万", "克桑", "灿"],
    ["aan ang", "昂", "邦", "康", "当", "方", "冈", "杭", "扬", "康", "朗", "芒", "南", "庞", "朗", "桑", "唐", "旺", "克桑", "仓"],
    ["ao au", "奥", "鲍", "考", "道", "福", "高", "豪", "尧", "考", "劳", "毛", "瑙", "保", "劳", "绍", "陶", "沃", "克绍", "曹"],
    ["en eng än ang", "恩", "本", "森", "登", "芬", "根", "亨", "延", "肯", "伦", "门", "嫩", "彭", "伦", "森", "滕", "文", "克森", "岑"],
    ["i ii j", "伊", "比", "西", "迪", "菲", "吉", "希", "伊", "基", "利", "米", "尼", "皮", "里", "西", "蒂", "维", "克西", "齐"],
    ["ie ye", "耶", "比耶", "谢", "迪耶", "菲耶", "杰", "希耶", "耶", "基耶", "列", "米耶", "涅", "皮耶", "列", "谢", "蒂耶", "维耶", "克谢", "切"],
    ["in yn", "因", "宾", "辛", "丁", "芬", "金", "欣", "因", "金", "林", "明", "宁", "平", "林", "辛", "廷", "温", "克辛", "钦"],
    ["ing", "英", "宾", "辛", "丁", "芬", "京", "兴", "英", "京", "林", "明", "宁", "平", "林", "辛", "廷", "温", "克辛", "钦"],
    ["io", "约", "比奥", "肖", "迪奥", "菲奥", "吉奥", "希奥", "约", "基奥", "廖", "苗", "尼奥", "皮奥", "廖", "肖", "蒂奥", "维奥", "克肖", "齐奥"],
    ["iu", "尤", "比乌", "休", "迪乌", "菲乌", "吉乌", "休", "基乌", "柳", "缪", "纽", "皮乌", "留", "休", "蒂乌", "维乌", "克休", "丘"],
    ["ö oe", "厄", "伯", "瑟", "德", "弗", "格", "赫", "约", "克", "勒", "默", "内", "珀", "勒", "瑟", "特", "沃", "克瑟", "策"],
    ["o oo", "奥", "博", "科", "多", "福", "戈", "霍", "约", "科", "洛", "莫", "诺", "波", "罗", "索", "托", "沃", "克索", "措"],
    ["ou", "欧", "博", "科", "多", "福", "戈", "霍", "约", "科", "洛", "莫", "诺", "波", "罗", "索", "托", "沃", "克索", "措"],
    ["on", "翁", "邦", "孔", "东", "丰", "贡", "洪", "永", "孔", "隆", "蒙", "农", "蓬", "龙", "松", "通", "翁", "克松", "聪"],
    ["un", "温", "本", "昆", "敦", "丰", "贡", "洪", "云", "昆", "伦", "蒙", "农", "蓬", "伦", "松", "通", "文", "克松", "聪"],
    ["u uu", "乌", "布", "库", "杜", "富", "古", "胡", "尤", "库", "卢", "穆", "努", "普", "鲁", "苏", "图", "武", "克苏", "楚"],
    ["y yy", "于", "比", "叙", "迪", "菲", "居", "许", "于", "屈", "吕", "米", "尼", "皮", "吕", "叙", "蒂", "维", "克叙", "曲"],
    ]


def transliterate(word, is_prefix=False, is_suffix=False):
    if word == "":
        return ""
    if " " in word:
        # Not setting is_prefix and is_suffix for now
        return "".join(transliterate(w) for w in word.split(" "))
    if "-" in word:
        # Ditto
        return "-".join(transliterate(w) for w in word.split("-"))
    word = word.lower()
    result = ""

    while len(word) > 0:
        # Greedily match a consonant
        best_c = ""
        best_i = 0
        for i, c in enumerate(cons):
            for cc in c.split(" "):
                if word.startswith(cc) and len(cc) > len(best_c):
                    best_c = cc
                    best_i = i
        word = word[len(best_c):]

        # Greedily match a vowel
        best_v = ""
        best_j = 0
        for j, v in enumerate(line[0] for line in vowels):
            for vv in v.split(" "):
                if word.startswith(vv) and len(vv) > len(best_v):
                    best_v = vv
                    best_j = j

        word = word[len(best_v):]
        
        if best_i == best_j == 0:
            raise Exception("Not Finnish alphabet")

        result += vowels[best_j][best_i + 1]

    # Apply special rules
    # source: https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%96%E8%AA%9E%E8%AD%AF%E9%9F%B3%E8%A1%A8

    # Special Rule 3
    # 汉语拼音dong、nan和xi的译音用于地名的开头时，应使用汉字栋、楠和锡（而不是东、南和西），避免望文生义。
    if not is_suffix and result[0] == "东":
        result = "栋" + result[1:]
    if not is_suffix and result[0] == "南":
        result = "楠" + result[1:]
    if not is_suffix and result[0] == "西":
        result = "锡" + result[1:]

    # Special Rule 4
    # “海”出现于地名结尾时，应改为“亥”，避免望文生义。
    if not is_prefix and result[-1] == "海":
        result = result[:-1] + "亥"
 
    return result


def transliterate_list(l, is_prefix=False, is_suffix=False):
    ret = []
    for w in l:
        try:
            ret.append(transliterate(w, is_prefix, is_suffix))
        except:
            pass
    return ret
