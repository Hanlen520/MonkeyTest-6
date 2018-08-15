#!/user/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/8/13 13:43
# @Author  : 疏影
# @File    : update_contact.py
from CashLoanProject.common import config
import requests
import json,datetime
from CashLoanProject.common.addSign import Sign

def update_contact(headers):
    url = config.HOST + '/v1/info/contact'
    data = {
        "contact":"[{\"name\":\"OPPO官方客服\",\"tel\":\"4001666888\"},{\"name\":\"自己\",\"tel\":\"13572489850\"},"
                  "{\"name\":\"三顾冒菜\",\"tel\":\"18092051314\"},{\"name\":\"孙力\",\"tel\":\"8617730600729\"},"
                  "{\"name\":\"盛伟1\",\"tel\":\"17089602464\"},{\"name\":\"lwld隔壁\",\"tel\":\"18691082172\"},"
                  "{\"name\":\"郑小红健\",\"tel\":\"8615109226928\"},{\"name\":\"饺子馆\",\"tel\":\"029,88262120\"},"
                  "{\"name\":\"刘晨\",\"tel\":\"8618292825591\"},{\"name\":\"张静媛招商\",\"tel\":\"15891440252\"},"
                  "{\"name\":\"钉钉免费电话\",\"tel\":\"057188157855,4001696188,4000966288,4008287660\"},"
                  "{\"name\":\"赵亚光\",\"tel\":\"13679277905\"},{\"name\":\"李娜\",\"tel\":\"15029574201\"},"
                  "{\"name\":\"张聚合\",\"tel\":\"18202944180\"},{\"name\":\"陈彬彬\",\"tel\":\"13759962993\"},"
                  "{\"name\":\"高千里\",\"tel\":\"15929963730\"},{\"name\":\"王远\",\"tel\":\"15771977731\"},"
                  "{\"name\":\"长城宽带\",\"tel\":\"18629421205\"},{\"name\":\"王亚路\",\"tel\":\"13379226031\"},"
                  "{\"name\":\"董宁\",\"tel\":\"13227886879\"},{\"name\":\"卞峰峰\",\"tel\":\"13032966519\"},"
                  "{\"name\":\"盛伟置业\",\"tel\":\"02962550317\"},{\"name\":\"王\",\"tel\":\"18192692314\"},"
                  "{\"name\":\"妈\",\"tel\":\"13991551597\"},{\"name\":\"胡少隐2\",\"tel\":\"18192897196,18729329877\"},"
                  "{\"name\":\"中软向甜HR\",\"tel\":\"18189251951\"},{\"name\":\"明德门派\",\"tel\":\"02985410027\"},"
                  "{\"name\":\"张元珍\",\"tel\":\"15202433789\"},{\"name\":\"刘先梅\",\"tel\":\"15829720602\"},"
                  "{\"name\":\"崔征\",\"tel\":\"18629379527\"},{\"name\":\"中软刘婷助理\",\"tel\":\"89633905\"},"
                  "{\"name\":\"中软任翔PM\",\"tel\":\"18192627526\"},{\"name\":\"林丹\",\"tel\":\"13892897969\"},"
                  "{\"name\":\"中软刘波PM\",\"tel\":\"18092311886\"},{\"name\":\"任翔\",\"tel\":\"18192627526\"},"
                  "{\"name\":\"自己电信\",\"tel\":\"18192496382\"},{\"name\":\"中软龙白彦组长\",\"tel\":\"18691955878\"},"
                  "{\"name\":\"中软卓兴UI\",\"tel\":\"18629408987\"},{\"name\":\"中软蕾蕾\",\"tel\":\"13519121150\"},"
                  "{\"name\":\"巴士6593师傅\",\"tel\":\"15619253359\"},{\"name\":\"賈\",\"tel\":\"13720529421\"},"
                  "{\"name\":\"徐xx\",\"tel\":\"13571496627\"},{\"name\":\"马房东\",\"tel\":\"13909290085\"},"
                  "{\"name\":\"胡永居主业\",\"tel\":\"13772116929\"},{\"name\":\"搬家公司\",\"tel\":\"88248888\"},"
                  "{\"name\":\"高电信\",\"tel\":\"18009183803\"},{\"name\":\"相鹏飞\",\"tel\":\"18091883928\"},"
                  "{\"name\":\"京东快递\",\"tel\":\"02968829359\"},{\"name\":\"papa\",\"tel\":\"13571449991\"},"
                  "{\"name\":\"中软马慧琴\",\"tel\":\"15991737693\"},{\"name\":\"张空调安装\",\"tel\":\"15029068207\"},"
                  "{\"name\":\"瑞恩1\",\"tel\":\"02989561328\"},{\"name\":\"瑞恩2\",\"tel\":\"02989183895\"},"
                  "{\"name\":\"小潇\",\"tel\":\"13572490791\"},{\"name\":\"吴租\",\"tel\":\"18267999694\"},"
                  "{\"name\":\"链川刘瑞兰\",\"tel\":\"15995438286\"},{\"name\":\"链川司小玲\",\"tel\":\"18602997967\"},"
                  "{\"name\":\"物流\",\"tel\":\"057187750556\"},{\"name\":\"汪\",\"tel\":\"18668120572\"},"
                  "{\"name\":\"齐白雪\",\"tel\":\"15209249246\"},{\"name\":\"test1\",\"tel\":\"13886248693\"},"
                  "{\"name\":\"test2\",\"tel\":\"13687292452\"},{\"name\":\"test2\",\"tel\":\"18367128674\"},"
                  "{\"name\":\"test3\",\"tel\":\"15757146879\"},{\"name\":\"test4\",\"tel\":\"13487108224\"},"
                  "{\"name\":\"test5\",\"tel\":\"13157127078\"},{\"name\":\"testA\",\"tel\":\"13587108224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"},"
                  "{\"name\":\"testB\",\"tel\":\"13157127178\"},{\"name\":\"testC\",\"tel\":\"13587128224\"}]"
    }

    s = Sign()
    new_data = s.signfun(data)
    print new_data
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    response = requests.post(url=url, headers=headers, data=new_data,verify=False)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print response
    if 200 == response.status_code:
        str_content = response.content
        dict_content = json.loads(str_content)
        print 'response:', str_content.decode("unicode-escape")

if __name__ == '__main__':
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JqemFwaS41MW1pbmd5YW8uY29tL3YxL2F1dGhvcml6YXRpb25zIiwiaWF0IjoxNTM0MTM4Nzk3LCJleHAiOjc1MzQxMzg3MzcsIm5iZiI6MTUzNDEzODc5NywianRpIjoiM3dsMWt6R214SFBoeHhQVSIsInN1YiI6OTAwMDAwMDA1fQ.G_HY_jLUatekqvMJKpZRjgkiAQwnl2ifr6V3gMg6PMU'
    headers = config.HEADER_ANDROID
    headers.update({'Authorization':'Bearer ' + token})

    update_contact(headers)