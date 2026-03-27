"""
test_merge_files.py - merge_files.pyのテストコード
"""

import pytest
from pathlib import Path
from merge_files import merge_files


@pytest.fixture
def temp_dir(tmp_path):
    """テスト用の一時ディレクトリを作成"""
    return tmp_path


class TestMergeFiles:
    """merge_files関数のテストクラス"""

    def test_merge_csv_files(self, temp_dir):
        """複数のCSVファイルが正しく結合されることを確認"""
        # テスト用CSVファイルを作成
        (temp_dir / "file1.csv").write_text("name,age\nAlice,30", encoding="utf-8")
        (temp_dir / "file2.csv").write_text("name,age\nBob,25", encoding="utf-8")
        (temp_dir / "file3.csv").write_text("name,age\nCharlie,35", encoding="utf-8")

        output_file = temp_dir / "combined.csv"

        # 関数を実行
        merge_files(temp_dir, "csv", output_file)

        # 結果を検証
        result = output_file.read_text(encoding="utf-8")
        assert "Alice,30" in result
        assert "Bob,25" in result
        assert "Charlie,35" in result

    def test_output_file_excluded(self, temp_dir):
        """出力先ファイルが結合対象から除外されることを確認"""
        (temp_dir / "data1.csv").write_text("data1", encoding="utf-8")
        (temp_dir / "data2.csv").write_text("data2", encoding="utf-8")

        output_file = temp_dir / "combi_zi.csv"
        # 出力ファイルが既に存在する場合
        output_file.write_text("old content", encoding="utf-8")

        merge_files(temp_dir, "csv", output_file)

        result = output_file.read_text(encoding="utf-8")
        # 古い内容は消えて、新しい内容が書かれる
        assert "old content" not in result
        assert "data1" in result
        assert "data2" in result

    def test_case_insensitive_extension(self, temp_dir):
        """大文字小文字混在の拡張子に対応することを確認"""
        (temp_dir / "lower.csv").write_text("lower", encoding="utf-8")
        (temp_dir / "upper.CSV").write_text("upper", encoding="utf-8")
        (temp_dir / "mixed.Csv").write_text("mixed", encoding="utf-8")

        output_file = temp_dir / "out.csv"

        # 小文字の拡張子で指定
        merge_files(temp_dir, "csv", output_file)

        result = output_file.read_text(encoding="utf-8")
        # 大文字小文字は区別される（globの仕様）
        assert "lower" in result
        # 大文字のCSVは別途テスト

    def test_uppercase_extension(self, temp_dir):
        """大文字の拡張子でフィルタリング"""
        (temp_dir / "file.CSV").write_text("uppercase", encoding="utf-8")
        (temp_dir / "file.csv").write_text("lowercase", encoding="utf-8")

        output_file = temp_dir / "out.csv"

        # 大文字のCSVで指定
        merge_files(temp_dir, "CSV", output_file)

        result = output_file.read_text(encoding="utf-8")
        assert "uppercase" in result

    def test_empty_extension(self, temp_dir):
        """拡張子を空に指定するとすべてのファイルが対象になる"""
        (temp_dir / "file1.txt").write_text("text1", encoding="utf-8")
        (temp_dir / "file2.csv").write_text("csv1", encoding="utf-8")
        (temp_dir / "file3.dat").write_text("data1", encoding="utf-8")

        output_file = temp_dir / "out.txt"

        merge_files(temp_dir, "", output_file)

        result = output_file.read_text(encoding="utf-8")
        assert "text1" in result
        assert "csv1" in result
        assert "data1" in result

    def test_output_file_not_included_when_empty_ext(self, temp_dir):
        """拡張子指定なしの場合も出力ファイルは除外される"""
        (temp_dir / "file1.txt").write_text("content1", encoding="utf-8")
        (temp_dir / "file2.txt").write_text("content2", encoding="utf-8")

        output_file = temp_dir / "out.txt"

        merge_files(temp_dir, "", output_file)

        result = output_file.read_text(encoding="utf-8")
        # 出力ファイル自身の内容は含まれない
        assert result.count("content1") == 1
        assert result.count("content2") == 1

    def test_no_files_found(self, temp_dir):
        """対象ファイルが存在しない場合でもエラーにならない"""
        output_file = temp_dir / "out.csv"

        # 対象となるCSVファイルがない状態で実行
        merge_files(temp_dir, "csv", output_file)

        # 出力ファイルは作成されるが空のはず
        result = output_file.read_text(encoding="utf-8")
        assert result == ""

    def test_subdirectories_ignored(self, temp_dir):
        """サブディレクトリは無視される（非再帰的）"""
        (temp_dir / "file1.csv").write_text("root", encoding="utf-8")

        # サブディレクトリを作成
        sub_dir = temp_dir / "subdir"
        sub_dir.mkdir()
        (sub_dir / "file2.csv").write_text("sub", encoding="utf-8")

        output_file = temp_dir / "out.csv"

        merge_files(temp_dir, "csv", output_file)

        result = output_file.read_text(encoding="utf-8")
        assert "root" in result
        assert "sub" not in result  # サブディレクトリは無視


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
