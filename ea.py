#ea的全程是easy api（easy bilibili api）
from bilibili_api import user, sync,video

def rd(strr):
    if strr=='uuid':
        f=open('uuid.txt', 'r')
        uuid=int(f.read())
        return uuid
print("***********Easy API bilibili已加载***********")
'''
这是使用文档：
只要部分，主要看每个def后面
官方API简易化：
#######get_relation_info#######
psend():#输出uuid
fans():#输出用户粉丝数
follow():#输出用户关注数
whisper():#输出用户悄悄关注数
blackfans():#输出用户黑名单数
#######get_user_info#######
uname():#获取用户昵称
sex():#获取用户性别
face_url():#获取用户头像url
sign():#获取用户简介
level():#获取用户等级[只能获取lv.x]
top_photo():#获取用户空间横幅URL
live_room_url():#获取用户直播间地址
live_room_title():#获取用户直播间标题
birthday():#获取用户生日xx-xx格式
#######get_user_info#######
get_new_video_BV():#获取用户最新视频BV号

自创API：
#------视频数据------#
get_video_play(bvid):#获取视频播放量
get_video_like(bvid):#获取视频点赞量
get_video_favorite(bvid):#获取视频收藏量
get_video_danmaku(bvid):#获取视频弹幕量
get_video_reply(bvid):#获取视频评论量
get_video_coin(bvid):#获取视频硬币量
get_video_share(bvid):#获取视频分享量
get_video_title(bvid):#获取视频标题
get_video_cover_url(bvid):#获取视频封面url
'''
#######get_relation_info#######
def psend():#输出uuid
    uuid=rd('uuid')
    print('uuid=',uuid)
def fans():#输出用户粉丝数
    uuid=rd('uuid')
    u=user.User(uuid)
    return sync(u.get_relation_info())["follower"]
def follow():#输出用户关注数
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_relation_info())["following"]
def whisper():#输出用户悄悄关注数
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_relation_info())["whisper"]
def blackfans():#输出用户黑名单数
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_relation_info())["black"]

#######get_user_info#######

def uname():#获取用户昵称
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["name"]
def sex():#获取用户性别
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["sex"]
def face_url():#获取用户头像url
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["face"]
def sign():#获取用户简介
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["sign"]
def level():#获取用户等级[只能获取lv.x]
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["level"]
def top_photo():#获取用户空间横幅URL
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["top_photo"]
def live_room_url():#获取用户直播间地址
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["live_room"]["url"]
def live_room_title():#获取用户直播间标题
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["title"]
def birthday():#获取用户生日xx-xx格式
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_user_info())["birthday"]

#######get_user_info#######

def get_new_video_BV():#获取用户最新视频BV号
    uuid = rd('uuid')
    u = user.User(uuid)
    return sync(u.get_videos())["list"]["vlist"][0]["bvid"]

#------视频数据------#

def get_video_play(bvid):#获取视频播放量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["view"]
def get_video_like(bvid):#获取视频点赞量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["like"]
def get_video_favorite(bvid):#获取视频收藏量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["favorite"]
def get_video_danmaku(bvid):#获取视频弹幕量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["danmaku"]
def get_video_reply(bvid):#获取视频评论量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["reply"]
def get_video_coin(bvid):#获取视频硬币量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["coin"]
def get_video_share(bvid):#获取视频分享量
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_stat())["share"]
def get_video_title(bvid):#获取视频标题
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_info())["title"]
def get_video_cover_url(bvid):#获取视频封面url
    bvid=bvid
    v=video.Video(bvid=bvid)
    return sync(v.get_info())["pic"]
