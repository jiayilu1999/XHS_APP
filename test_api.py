import httpx
import asyncio
import json

# jd = {"template_id":2, "api_key_id":1,"message":"title:张掖西-山丹马场\n post:这段路一定要选窗边的位置，一定一定不要睡觉，一定一定要全程拿好手机相机随时拍照和视频。 看风吹草低见牛羊 ，看银装素裹的雪山#张掖 #旅游攻略\n keywords:张掖, 旅游攻略", "streaming":True}
share_link = "47 Luuuu发布了一篇小红书笔记，快来看吧！ 😆 G9WQvLGo1arLbGu 😆 http://xhslink.com/a/6hZvIufwzRL5，复制本条信息，打开【小红书】App查看精彩内容！"

# step 1: 通过短链获取小红书文案
async def get_rn_post_by_share_link(share_link_str):
    api_url = "https://mmt.icu/api2/wf/r1/catch_post"
    try:
        js_dict = {"share_link": share_link_str}
        response = httpx.post(url=api_url, json=js_dict,headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            js_dict = json.loads(response.text)
            return js_dict
        else:
            print(response.text)
    except Exception as e:
        print(e)
    print("远程服务器异常")
    return None

# step 2: 通过获得的post文案，调用大模型接口改写
async def test_stream(js_dict):
    async with httpx.AsyncClient() as client:
        async with client.stream('POST', f'https://mmt.icu/api2/b/llm', headers={"Content-Type":"application/json"},json=js_dict, timeout=10000) as response:
            if response.status_code != 200:
                print(f"Error: Received status code {response.status_code}")
                return
            async for chunk in response.aiter_text():
                print("Received chunk:", chunk)


post_dict = asyncio.run(get_rn_post_by_share_link(share_link))
print(post_dict)
# 提取内容，拼接成需要的形式，格式如下 title:xxx \n post:xxx \n keywords:xxx
post_content = post_dict["data"]["title"] + "\n" + post_dict["data"]["post"] + "\n" + post_dict["data"]["keywords"]
print(post_content)

# 定义api接口dict
jd = {"template_id":2, "api_key_id":1,"message":post_content, "streaming":True}

# 调用大模型改写:
asyncio.run(test_stream(jd))
