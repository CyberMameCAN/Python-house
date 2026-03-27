from pathlib import Path


def merge_files(aimed_dir:Path, extention_name:str, base_file:Path):
    """
    フォルダ中のテキストファイルを結合する
    拡張子を指定しない場合は、すべてのファイルを結合する(結合ファイル以外)
    
    Args:
        aimed_dir (Path): 対象フォルダ
        extention_name (str): 拡張子
        base_file (Path): 結合(出力)ファイル
    """
    # dir_path = Path(aimed_dir)
    base_file_name = base_file.name
    print(f"結合ファイル名: {base_file_name}")
    
    # CSVファイルのみ取得（出力ファイルは除外）
    if extention_name == '':
        aimed_ext = '*'
    else:
        aimed_ext = f'*.{extention_name}'
    files = [f for f in aimed_dir.glob(aimed_ext) if f.name != base_file_name]
    # files = [f for f in aimed_dir.glob("*.CSV")]
    files.sort()

    print('結合ファイル:')
    with open(base_file, "w", encoding="utf-8") as outfile:
        for file in files:
            print(f'  {file}')
            with open(aimed_dir / file, "r", encoding="utf-8") as f:
                outfile.write(f.read())
                outfile.write("\n")


def main():
    print("Merging files...")

    ## 設定
    #
    # ディレクトリの指定
    aimed_dir = "/path/to/directory"
    # 対象ファイルの拡張子
    extention_name = "CSV"
    #
    # ベースとなるファイル
    base_file = Path(aimed_dir) / "combi_zi.csv"
    
    ## 本体
    merge_files(aimed_dir, extention_name, base_file)

if __name__ == "__main__":
    main()
    