from pathlib import Path

p=Path(r"C:\Users\hui.xie\Desktop\浙大项目\光谱原始数据 - 副本\modify-18")
p_1=list(p.iterdir())
for item in p_1 :
    for path_name in item.iterdir():
        temp=path_name.name.split("_")
        if temp[1] =="11":
            new_file=path_name.with_name("N_"+"10_"+temp[2])
            path_name.replace(new_file)
        elif temp[1] =="10" :
            new_file = path_name.with_name("N_" + "11_" + temp[2])
            path_name.replace(new_file)
        elif temp[1] == "17":
            new_file = path_name.with_name("N_" + "18_" + temp[2])
            path_name.replace(new_file)
        elif temp[1] == "36":
            new_file = path_name.with_name("N_" + "31_" + temp[2])
            path_name.replace(new_file)



