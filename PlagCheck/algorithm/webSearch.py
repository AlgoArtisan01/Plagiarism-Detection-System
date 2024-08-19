from PlagCheck.algorithm import ConsineSim
from googleapiclient.discovery import build


#Registered API Token
searchEngine_Id = '04fe417dd12de4e2b'
searchEngine_API = 'AIzaSyBUR02Qp6G8djXrARY1YvTvySXeBOOfSh0'



def searchWeb(text, output, c):
    text = text
    # print(text)
    try:
        resource = build("customsearch", 'v1',
                         developerKey=searchEngine_API).cse()
        result = resource.list(q=text, cx=searchEngine_Id).execute()
        searchInfo = result['searchInformation']
        # print(searchInfo)
        if(int(searchInfo['totalResults']) > 0):
            maxSim = 0
            itemLink = ''
            numList = len(result['items']) 
            if numList >= 5:
                numList = 5
            for i in range(0, numList):
                item = result['items'][i]
                content = item['snippet']
                simValue = ConsineSim.cosineSim(text, content)
                maxSim = round(maxSim,2)

                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item['link']
                if item['link'] in output:
                    itemLink = item['link']
                    break
            if itemLink in output:
                print('if', maxSim)
                output[itemLink] = output[itemLink] + 1
                c[itemLink] = ((c[itemLink] *
                                (output[itemLink]-1) + maxSim)/(output[itemLink]))
            else:
                print('else', maxSim)
                print(text)
                print(itemLink)
                output[itemLink] = 1
                c[itemLink] = maxSim
    except Exception as e:
        print(text)
        print(e)
        print('Web Error !!')
        return output, c, 1
    return output, c, 0
