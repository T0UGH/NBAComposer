changeTeam = "克里夫兰骑士 阵容调整 (特里斯坦 汤普森; 勒布朗 詹姆斯; J.R. 史密斯; 凯文 洛夫; 乔治 希尔)', '0-0')"

left_index = changeTeam.find("(")+1
right_index = changeTeam.find(")")
print(changeTeam[left_index:right_index])
pieces = changeTeam[left_index:right_index].split("; ")
for piece in pieces:
    print(piece)
