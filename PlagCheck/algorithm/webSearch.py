from dotenv import load_dotenv
import os
from PlagCheck.algorithm import ConsineSim
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Get API credentials from .env
searchEngine_Id = os.getenv('SEARCH_ENGINE_ID')
searchEngine_API = os.getenv('SEARCH_ENGINE_API_KEY')

def searchWeb(text, output, c):
    try:
        resource = build("customsearch", 'v1', developerKey=searchEngine_API).cse()
        result = resource.list(q=text, cx=searchEngine_Id).execute()
        searchInfo = result['searchInformation']

        if int(searchInfo['totalResults']) > 0:
            maxSim = 0
            itemLink = ''
            numList = min(len(result['items']), 5)
            for i in range(numList):
                item = result['items'][i]
                content = item['snippet']
                simValue = ConsineSim.cosineSim(text, content)
                simValue = round(simValue, 2)

                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item['link']
                if item['link'] in output:
                    itemLink = item['link']
                    break

            if itemLink in output:
                print('if', maxSim)
                output[itemLink] += 1
                c[itemLink] = ((c[itemLink] * (output[itemLink] - 1) + maxSim) / output[itemLink])
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
