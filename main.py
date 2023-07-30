import tkinter as tk
import tkinter.filedialog
import pypdf
import os

def show_dialog():
    root = tk.Tk()
    root.withdraw()

    filetypes = [("PDFファイル", "*.pdf")]
    target_file = tkinter.filedialog.askopenfilenames(filetypes=filetypes, title="ファイルを開く")

    list_files = list(target_file)
    return list_files

def pdf_merger(file_name):
    print("[info]結合するファイルを選択してください")

    merger = pypdf.PdfMerger()
    list_files = show_dialog()

    for file in list_files :
        merger.append(file)

    path = os.getcwd()
    merger.write(file_name + ".pdf")
    merger.close()

    print("[info]ファイルの結合が完了しました。")


def main():

    file_name = input("[info]結合後のpdfファイル名を入力してください:")

    DirectoryCommand = input("[info]結合するファイルの出力先ディレクトリを指定しますか？(y/n):")

    if DirectoryCommand == "y":
        Directory = input("[info]ディレクトリを入力してください:")
        os.chdir(Directory)

        pdf_merger(file_name)

    elif DirectoryCommand == "n":
        pdf_merger(file_name)

    else:
        print("[info]入力が間違っています。")


if __name__ == '__main__':
    main()

