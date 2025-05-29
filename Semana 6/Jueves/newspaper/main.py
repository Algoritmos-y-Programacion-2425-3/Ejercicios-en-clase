from employee import Writer, WriterManager

def main():
    writer = Writer("Daniela","V24475812")
    article = writer.write_article()
    article.show()

main()