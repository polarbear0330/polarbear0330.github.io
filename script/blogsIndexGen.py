import os
def genIndex(BlogDir, relativeBlogDir, IndexFile, indexFileTitle):
    rootPath = "../"
    blogDir = rootPath + BlogDir

    indexFile = rootPath + IndexFile
    # indexFileTitle = "# 牧野的个人博客"
    blogFileLink = "{0}. [{1}]({2}{1}/index)"


    indexFile = open(indexFile, "w", encoding="UTF-8")
    indexFile.write(indexFileTitle + "\n\n<br>\n\n")

    dirs = os.listdir(blogDir)
    for name in dirs:
        # print(name)
        if os.path.isdir(blogDir + "/" + name):
            # print(name)
            indexFile.write(blogFileLink.format(1, name, relativeBlogDir) + "\n\n")
            indexFile.write("    <br>" + "\n\n")

    indexFile.close()

if __name__ == "__main__":
    BlogDir = "blogs"
    relativeBlogDir = "blogs/"
    IndexFile = "index.md"
    indexFileTitle = "# 牧野的个人博客"
    genIndex(BlogDir, relativeBlogDir, IndexFile, indexFileTitle)

    BlogDir = "blogs/español_estudio"
    relativeBlogDir = ""
    IndexFile = "blogs/español_estudio/index.md"
    indexFileTitle = "# Spanish For Beginners"
    genIndex(BlogDir, relativeBlogDir, IndexFile, indexFileTitle)