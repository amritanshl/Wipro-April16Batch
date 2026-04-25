import re
text = """Inveraray Castle is a Grade A listed country house near Inveraray in the county of Argyll, in western Scotland. It is located on the shore of Loch Fyne, Scotland's longest sea loch. Designed in part by William Adam and Roger Morris, it was constructed from the 1740s and is one of the earliest Gothic Revival buildings.
\n

The current building replaced an earlier 15th-century castle at which King James V stayed in September 1533. The castle, the seat of the Duke of Argyll, chief of Clan Campbell, houses a collection of more than 1,300 pikes, muskets, swords and other weapons, and is open to visitors. This photograph shows the facade of Inveraray Castle in 2010."""
numbers = """14 Times Table
14 Times Table up to 10
14 × 1 = 14	14 × 6 = 84
14 × 2 = 28	14 × 7 = 98
14 × 3 = 42	14 × 8 = 112
14 × 4 = 56	14 × 9 = 126
14 × 5 = 70	14 × 10 = 140"""

# match_is = re.findall(r"is", text)
# print(len(match_is))
# match_is = re.findall(r".", text)
# print(match_is)

# text_phone = "Call me at 999-555-6666 on twesday"

# pattern_phone = r"\d{3}-\d{3}-\d{4}"

# match_it = re.search(pattern_phone, text_phone)
# print(match_it.group())

# re.match

# text = "error 404: page not found"
# match_obj = re.search(r"404", text)
# print(match_obj.group())

# texte = "Items: Apple ($5), Banana ($2), Cherry ($10)"
# prices = re.findall(r"\$\d+", text)
# print(prices)


text = "error found in [Mod2]  and [mod3] - do it."
greedy_one = re.search(r"\[.*\]", text)
non_greedy_one = re.search(r"\[.*?\]", text)

print(greedy_one.group(0))
print("---------------")
print(non_greedy_one.group(0))