emps = []

print("=====员工信息管理系统=====")
print("请输入员工信息(输入done结束输入)")

while True: 
    name = input("\n请输入员工姓名: ")
    if name.lower() == "done": 
        break
    
    while True: 
        try: 
            gender = input("请输入员工性别(男/女): ")
            if gender not in ["男", "女"]: 
                print("性别请输入男或女")
                continue
            work_age = int(input("请输入工龄(年): "))
            pre_tax_salary = float(input("请输入税前工资(元): "))
            tax_rate = float(input("请输入税率(如0.15表示15%): "))
            if not 0 <= tax_rate <= 1: 
                print("税率请输入0-1之间的小数(如0.2表示20%)!")
                continue
            break
        except ValueError: 
            print("输入格式错误！工龄为整数, 工资/税率为数字(如10000、0.15)")
    
    after_tax_salary = pre_tax_salary * (1 - tax_rate)
    
    emps.append({
        "name":  name,
        "gender":  gender,
        "work_age":  work_age,
        "pre_tax":  pre_tax_salary,
        "tax_rate":  tax_rate,
        "after_tax":  after_tax_salary
    })
    print(f"已添加员工: {name}")


def get_str_width(s): 
    width = 0
    for char in s: 
        if '\u4e00' <= char <= '\u9fff':
            width += 2
        else: 
            width += 1
    return width


print("\n" + "="*80)
print("员工信息汇总表")
print("="*80)


col_widths = {
    "name":  10,
    "gender":  6,
    "work_age":  6,
    "pre_tax":  14,
    "tax_rate":  12,
    "after_tax":  14
}

header_parts = [
    f"姓名".ljust(col_widths["name"]),
    f"性别".ljust(col_widths["gender"]),
    f"工龄".ljust(col_widths["work_age"]),
    f"税前工资(元)".ljust(col_widths["pre_tax"]),
    f"税率".ljust(col_widths["tax_rate"]),
    f"税后工资(元)".ljust(col_widths["after_tax"])
]
header = f"| {' | '.join(header_parts)} |"
print(header)

sep = f"|{'-' * (len(header)-2)}|"
print(sep)

for emp in emps: 
    name_str = emp["name"].ljust(col_widths["name"])
    gender_str = emp["gender"].ljust(col_widths["gender"])
    work_age_str = str(emp["work_age"]).ljust(col_widths["work_age"])
    pre_tax_str = f"{emp['pre_tax']: .2f}".ljust(col_widths["pre_tax"])
    tax_rate_str = f"{emp['tax_rate']*100: .2f}%".ljust(col_widths["tax_rate"])
    after_tax_str = f"{emp['after_tax']: .2f}".ljust(col_widths["after_tax"])
    
    row_parts = [name_str, gender_str, work_age_str, pre_tax_str, tax_rate_str, after_tax_str]
    row = f"| {' | '.join(row_parts)} |"
    print(row)

print(sep)
print(f"| {'总计员工数: {}'.format(len(emps)).ljust(len(header)-4)} |")
print("="*80)