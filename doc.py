# -*- coding:utf-8 -*-
import os
version = input("Введіть версію доповнення:")


def delete_files():
	dirfiles = os.listdir("addon/doc")
	dirfiles = ["addon/doc/"+file for file in dirfiles]
	dirfiles = [dir+"/readme.html" for dir in dirfiles if os.path.isdir(dir)]

	locale_files = os.listdir("addon/locale")
	locale_files = ["addon/locale/"+file for file in locale_files]
	locale_files = [dir+"/LC_MESSAGES/nvda.mo" for dir in locale_files if os.path.isdir(dir)]

	files = [
		"addon/manifest.ini",
		"addon/doc/style.css",
		"addon/appModules/__pycache__",
		"addon/GlobalPlugins/UnigramPlus/__pycache__",
		"addon/GlobalPlugins/WhatsAppPlus/__pycache__",
	]
	for file in dirfiles+files+locale_files:
		try:
			os.remove(file)
			print("Видалено: "+file)
		except: print("Не видалено: "+file)


def get_doc():
	path_to_doc = "addon/doc"
	dirfiles = os.listdir(path_to_doc)
	dirfiles = map(lambda name: os.path.join(path_to_doc, name), dirfiles)
	dirfiles = [dir for dir in dirfiles if os.path.isdir(dir)]

	for file in dirfiles:
		lang = file[-2:]
		file_object = open(file+"/readme.md", "r", encoding="utf-8")
		text = file_object.read()
		file_object.close()
		action_doc(text, lang)

def action_doc(file, lang):
	global version
	file = file.split("\n")
	file = [row for row in file if row != ""]
	url_for_donate = "https://unigramplus.diaka.ua/donate"
	def is_version(s):
		if s.startswith("###") and version in s: return True
		else: return False
	start_index = next((index for index in range(2, len(file)) if file[index].startswith("*") and is_version(file[index-1])), 0)
	if start_index == 0: return
	end_index = next((index for index in range(start_index, len(file)) if file[index] == "" or file[index].startswith("###")), len(file))
	print("Результат")
	text = "\n".join(file[start_index:end_index])
	print(text)
	text_donate = ""
	# Перевіримо чи наявна інформація про донати цією мовою
	if os.path.exists("donate/"+lang+".txt"):
		file_object = open("donate/"+lang+".txt", "r", encoding="utf-8")
		text_donate = file_object.read()
		file_object.close()
	else:
		file_object = open("donate/en.txt", "r", encoding="utf-8")
		text_donate = file_object.read()
		file_object.close()
	text = text+"\n\n"+text_donate
	file_object = open("doc/"+lang+".txt", "w", encoding="utf-8")
	file_object.write(text)
	file_object.close()


get_doc()
delete_files()
input("Натисніть щось для закриття вікна")