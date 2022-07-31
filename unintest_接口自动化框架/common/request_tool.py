import requests

class RequestTool:

    def request(self,url,method,headers=None,data=None,json=None):
        mt=method.lower() #转小写
        if mt=='get':
            if data:
                response = requests.get(url=url, headers=headers, params=data)
            else:
                response = requests.get(url=url,headers=headers,params=json)
        elif mt == 'post':
            response =  requests.get(url=url,headers=headers,data=data,json=json)
        # response是接口的响应,response是一个对象，text,content;

        return response.content.decode('utf8') # expectation

class SessionTool():
    session=requests.Session()


    def request(self,url,method,headers=None,data=None,json=None):
        mt=method.lower() #转小写
        if mt=='get':
            if data:
                response = self.session.get(url=url, headers=headers, params=data)
            else:
                response = self.session.get(url=url,headers=headers,params=json)
        elif mt == 'post':
            response =  self.session.get(url=url,headers=headers,data=data,json=json)
        # response是接口的响应,response是一个对象，text,content;

        return response.content.decode('utf8') # expectation

    def close(self):
        self.session.close()