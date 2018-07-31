import os

rootPath = "../"
blogDir = "{}blogs".format(rootPath)

indexFile = "{}index.md".format(rootPath)
indexFileTitle = "# 牧野的个人博客"
blogFileLink = "{0}. [{1}](blogs/{1}/index)"


indexFile = open(indexFile, "w")
indexFile.write(indexFileTitle + "\n")

dirs = os.listdir(blogDir)
for name in dirs:
    indexFile.write("<br>" + "\n")
    indexFile.write(blogFileLink.format(1, name) + "\n")

indexFile.close()