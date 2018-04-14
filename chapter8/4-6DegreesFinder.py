from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute("USE wikipedia")

def getUrl(pageId):
    cur.execute("SELECT url FROM pages WHERE id = %s", (int(pageId)))
    conn.commit()
    if cur.rowcount == 0:
        return None
    return cur.fetchone()[0]

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (int(fromPageId)))
    conn.commit()
    if cur.rowcount == 0:
        return None
    A=cur.fetchall()
    print("A:",A)
    return [x[0] for x in A]

def searchBreadth(targetPageId, currentPageId, depth, nodes):
    if nodes is None or len(nodes) == 0:
        return None
    if depth <= 0:
        for node in nodes:
            if node == targetPageId:
                return [node]
        return None
    print("nodes2:", nodes)
    #depth is greater than 0 -- go deeper!
    for node in nodes:
        print("node:", node)
        found = searchBreadth(targetPageId, node, depth-1, getLinks(node))
        print("found1:", found)
        print('type(found):',type(found))
        print('type(currentPageId):', type(currentPageId))
        print("currentPageId1:", currentPageId)
        if found is not None:
            found.append(currentPageId)
            #这个地方出现了问题，注意append函数该方法无返回值，但是会修改原来的列表。
            print("found:",found)
            return found
    return None

nodes = getLinks(1)
print("nodes1:",nodes)
targetPageId = 5408
for i in range(0,3):
    print("i:", i)
    found = searchBreadth(targetPageId, 1, i, nodes)
    if found is not None:
        print("found:",found)
        for node in found:
            print("getUrl(node):",getUrl(node))
        break
    else:
        print("No path found")

