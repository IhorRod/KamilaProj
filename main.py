import pandas as pd
from collections import Counter


def main(inp_file_name: str = "ip"):
    table: pd.DataFrame = pd.read_excel(f"{inp_file_name}.xlsx")
    lst: list = sorted([i.split(":") for i in table["IP"]],
                       key=lambda x: int(x[1]),
                       reverse=True)
    lst_count = [i[1] for i in lst]
    counter = Counter(lst_count)
    counts = [counter[i[1]] for i in lst]
    table["IP"] = [":".join(i) for i in lst]
    table["Count"] = counts
    table.to_excel(f"{inp_file_name}.xlsx")


if __name__ == '__main__':
    main()
