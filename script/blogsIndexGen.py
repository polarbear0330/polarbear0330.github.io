import os

rootPath = "../"
blogDir = "{}blogs".format(rootPath)

indexFile = "{}index.md".format(rootPath)
indexFileTitle = "# 牧野的个人博客"
blogFileLink = "{0}. [{1}](blogs/{1}/index)"


indexFile = open(indexFile, "w", encoding="UTF-8")
indexFile.write(indexFileTitle + "\n\nutf-8<br>\n\n")

dirs = os.listdir(blogDir)
for name in dirs:
    indexFile.write(blogFileLink.format(1, name) + "\n\n")
    indexFile.write("    <br>" + "\n\n")

indexFile.close()