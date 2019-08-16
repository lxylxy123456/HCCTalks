# HCC Talks
* Note: currently all talks are in Chinese. 
* All talks are to be written in LaTeX beamer. 
* Old talk files (written in LibreOffice Impress) are in
	[odp](https://github.com/lxylxy123456/HCCTalks/tree/odp) branch. 

## Make
* Run `make ALL` to generate all pdf files to `/tmp/` directory. 
	* To change output directory, use `TMP=/new/output/dir`. 
* Run `make clean_tmp` to remove all temporary files. 
* Run `make clean` to remove all generated files. 
* All generated files, though may not up-to-date, are in 
	[make](https://github.com/lxylxy123456/HCCTalks/tree/make) branch

## 已移植到beamer的幻灯片

### PythonTalk
1.	基本类型 (int, float, bool)
2.	复杂类型 (list, dict, tuple, str)
3.	循环函数 (for, while)
4.	判断函数 (if, import)
5.	常用方法 (print, help, max,min,all,any,hash, input, open, os.system, in)
6.	(list.sort, 函数, str.encode, 进制转换, datetime)
7.	(random, sys.stdout, sys.argv, uuid, getch, qrcode, del(_))
8.	实际应用 (生成二维码, 批量处理文本, 裁剪图片, 批量下载附件)
9.	函数式编程
10.	多线程编程
11.	用pdb调试程序

### BashTalk
1.	目录操作 (ll, ls, pwd, cd; du, df, tree, find; cat, mkdir; rm, mv, cp)
2.	文件操作 (grep; head, tail, cut; wc, md5sum, sha1sum;| ; more, less, nano, vi; hexdump; diff)
3.	(uname, top, ps -aux, sync, ifconfig, lspci, free; <, >, <<, >>; sleep, time, date; /, //, *, ?, ., .., ~, ;, \\, &&, ||; linux目录; 常用文件; 设备和挂载点)
4.	(su, sudo; history, .bash_history; rpm, dnf, yum; 7za; nano)

### GitTalk
1. 使用Git

### RegExpTalk
1.	正则表达式使用方法

## 尚未移植到beamer的幻灯片
* 请参考[odp](https://github.com/lxylxy123456/HCCTalks/tree/odp)分支

### AstronomyTalk
1.	天文学软件使用方法

### IntroductionToComputerEngineering
1.	一些常用的开源软件介绍

### DjangoTalk
0.	[prep] SQL + HTML
1.	DjangoBook 1 ~ 3
2.	DjangoBook 3 ~ 4
3.	DjangoBook 4 ~ 4
4.	DjangoBook 5 ~ 5
5.	DjangoBook 12, 14

### HTMLTalk
1.	HTMLTalk 1
2.	HTMLTalk 2

