import pygame
import win32gui
import win32con
import ea
from borax.calendars.lunardate import LunarDate
from bilibili_api import user, sync,video
import time
import requests
import os
from PIL import Image
import threading
import _thread
import cv2
#圆形头像
def circle(img_path):
    path_name = os.path.dirname(img_path)
    cir_file_name = 'cir_img.png'
    cir_path = path_name + '/' + cir_file_name
    ima = Image.open(img_path).convert("RGBA")
    size = ima.size
    # 因为是要圆形，所以需要正方形的图片
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    # 最后生成圆的半径
    r3 = int(r2/2)
    imb = Image.new('RGBA', (r3*2, r3*2),(0,0,0,0))
    pima = ima.load() # 像素的访问对象
    pimb = imb.load()
    r = float(r2/2) #圆心横坐标

    for i in range(r2):
        for j in range(r2):
            lx = abs(i-r) #到圆心距离的横坐标
            ly = abs(j-r)#到圆心距离的纵坐标
            l = (pow(lx,2) + pow(ly,2))** 0.5 # 三角函数 半径
            if l < r3:
                pimb[i-(r-r3),j-(r-r3)] = pima[i,j]

    imb.save(cir_path)
    return cir_path
#长字符串自动省略号
def long_str(text,longg):
    if len(text)>longg:
        return str(text[0:longg-3]+"...")
    else:
        return text
#刷新数据
def FF5():
    print("1")
    global jtime,uname,fans,img,img1,cover_png,title_text
    try:
            # 更新时间
            jtime = time.time()
            # 用户名
            uname = ea.uname()
            # 粉丝数
            fans = ea.fans()
            # 新视频封面
            _thread.start_new_thread(downloadd, (ea.get_video_cover_url(ea.get_new_video_BV()), "new_cover.png"))
            img = cv2.imread("new_cover.png")
            img1 = cv2.resize(img, (270, 152))  # 修改图片的尺寸
            cv2.imwrite("new_cover_chuli.png", img1)
            cover_png = pygame.image.load("new_cover_chuli.png")
            # 标题
            title_text = long_str(ea.get_video_title(ea.get_new_video_BV()), 18) + "||" + str(
                ea.get_video_play(ea.get_new_video_BV()))
    except:# 更新时间
            jtime = time.time()
            # 用户名
            uname = ea.uname()
            # 粉丝数
            fans = ea.fans()
            # 新视频封面
            _thread.start_new_thread(downloadd, (ea.get_video_cover_url(ea.get_new_video_BV()), "new_cover.png"))
            img = cv2.imread("new_cover.png")
            img1 = cv2.resize(img, (270, 152))  # 修改图片的尺寸
            cv2.imwrite("new_cover_chuli.png", img1)
            cover_png = pygame.image.load("new_cover_chuli.png")
            # 标题
            title_text = long_str(ea.get_video_title(ea.get_new_video_BV()), 18) + "||" + str(
                ea.get_video_play(ea.get_new_video_BV()))
            print("aaa")
    print("2")
    time.sleep(2)
#画文字
def draw_text_20(text,wight,hight,x,y,z):
    text = font20.render(str(text), True, (x,y ,z))
    screen.blit(text,(wight,hight))
def draw_text_40(text,wight,hight,x,y,z):
    text = font40.render(str(text), True, (x,y ,z))
    screen.blit(text,(wight,hight))
def draw_text_30(text,wight,hight,x,y,z):
    text = font30.render(str(text), True, (x,y ,z))
    screen.blit(text,(wight,hight))
def draw_text_60(text,wight,hight,x,y,z):
    text = font60.render(str(text), True, (x,y ,z))
    screen.blit(text,(wight,hight))
def draw_text_m_20(text,hight,x,y,z):
    text = font20.render(str(text), True, (x,y ,z))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, hight))
    screen.blit(text,text_rect)
def draw_text_m_30(text,hight,x,y,z,date=0):
    text = font30.render(str(text), True, (x,y ,z))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, hight))
    screen.blit(text,text_rect)
    if (date==1):
        return [text_rect[0],text_rect[1]]
    if (date==2):
        return [text.get_rect().width,text.get_rect().height]
    if (date==3):
        return [text_rect[0],text_rect[1],text.get_rect().width,text.get_rect().height]
def draw_text_m_40(text,hight,x,y,z):
    text = font40.render(str(text), True, (x,y ,z))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, hight))
    screen.blit(text,text_rect)
def draw_text_m_60(text,hight,x,y,z,date=0):
    text = font60.render(str(text), True, (x,y ,z))
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, hight))
    screen.blit(text,text_rect)
    if (date==1):
        return [text_rect[0],text_rect[1]]
    if (date==2):
        return [text.get_rect().width,text.get_rect().height]
    if (date==3):
        return [text_rect[0],text_rect[1],text.get_rect().width,text.get_rect().height]
def draw_text_mm(text,x,y,z):
    text = font20.render(str(text), True, (x,y ,z))

    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(text,text_rect)
#下载
def downloadd(url,name):#下载文件
    time.sleep(2)#防止多线程与读取撞车
    r = requests.get(url)
    with open(str(name), "wb") as code:
        code.write(r.content)
    r.close()
#自动空格
def kongge():
    f = open('有些字体会导致播放图标错位，修改该数字大小试试.txt', 'r')
    howl=f.read()
    f.close()
    aaa="                                                                                 "
    return aaa[0:int(howl)-1]
#创建主窗口
pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.NOFRAME)
pygame.display.set_caption('up主小工具——只有无边框模式才可以置顶显示哦')
#锁定默认帧数
fps = 60
fcclock = pygame.time.Clock()
#！！！依靠bug驱动请勿更改！！！设置窗口透明
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, 0, 128, win32con.LWA_ALPHA)
#窗口置顶
#win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 0, 0, win32con.SWP_NOSIZE)
#初始化
done = False
x,y=0,0
SCREEN_WIDTH,SCREEN_HEIGHT=600,400
info_object = pygame.display.Info()
font40 = pygame.font.Font('z.TTF', 40)
font60 = pygame.font.Font('z.TTF', 60)
font30 = pygame.font.Font('z.TTF', 30)
font20 = pygame.font.Font('z.TTF', 20)
weekk = ["天", "一", "二", "三", "四", "五", "六"]
yuefeng = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
riqi = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
        "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "廿十",
        "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]

face_url = ea.face_url()
downloadd(face_url, "face.png")
img = cv2.imread(circle("face.png"))
img1=cv2.resize(img,(50,50))  #修改图片的尺寸
cv2.imwrite("face_chuli.png",img1)
face_png = pygame.image.load("face_chuli.png")

shangciqiehuan1 = time.time()
shangciqiehuan2 =time.time()
times=0
yidonga=False
zhidinga=False
jtime1=time.time()-21
jtime2=time.time()-11
#加载资源图片
likep = pygame.image.load("./icon/点赞.png")
danmup=pygame.image.load("./icon/弹幕.png")
yinbip=pygame.image.load("./icon/投币.png")
shoucangp=pygame.image.load("./icon/收藏.png")
pinglunp=pygame.image.load("./icon/评论.png")
zhuanfap=pygame.image.load("./icon/分享.png")
bofangp=pygame.image.load("./icon/播放.png")
zhidingp=pygame.image.load("./icon/置顶.png")
yidongp=pygame.image.load("./icon/移动.png")

#首次刷新数据
if 1==1:
    # 用户名
    uname = ea.uname()
    # 粉丝数
    fans = ea.fans()
    lfans= 0
    # 新视频封面
    _thread.start_new_thread(downloadd, (ea.get_video_cover_url(ea.get_new_video_BV()), "new_cover.png"))
    img = cv2.imread("new_cover.png")
    img1 = cv2.resize(img, (270, 152))  # 修改图片的尺寸
    cv2.imwrite("new_cover_chuli.png", img1)
    cover_png = pygame.image.load("new_cover_chuli.png")
    # 标题
    new_video_BV=ea.get_new_video_BV()
    title_text = long_str(ea.get_video_title(new_video_BV), 15) + kongge() + str(
        ea.get_video_play(new_video_BV))
    lplaya=0
    playa=ea.get_video_play(new_video_BV)
    ttt=long_str(ea.get_video_title(new_video_BV), 15)
    # 新视频各项数据
    v = video.Video(new_video_BV)
    get_stat = sync(v.get_stat())
    llikea = 0
    lfavoritea = 0
    ldanmakua = 0
    lreplya = 0
    lcoina = 0
    lsharea = 0

    likea = get_stat["like"]
    favoritea = get_stat["favorite"]
    danmakua = get_stat["danmaku"]
    replya = get_stat["reply"]
    coina = get_stat["coin"]
    sharea = get_stat["share"]

#主循环（帧循环）
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #刷新数据
    if (time.time() - jtime1 > 20):
        try:
            # _thread.start_new_thread(FF5,())
            jtime1 = time.time()
            # 用户名
            uname = ea.uname()
            # 粉丝数
            lfans= ea.fans()-fans
            fans = ea.fans()
            # 新视频封面
            _thread.start_new_thread(downloadd, (ea.get_video_cover_url(ea.get_new_video_BV()), "new_cover.png"))
            img = cv2.imread("new_cover.png")
            img1 = cv2.resize(img, (270, 152))  # 修改图片的尺寸
            cv2.imwrite("new_cover_chuli.png", img1)
            cover_png = pygame.image.load("new_cover_chuli.png")
        except:
            # _thread.start_new_thread(FF5,())
            jtime1 = time.time()
            # 用户名
            uname = ea.uname()
            # 粉丝数
            lfans= ea.fans()-fans
            fans = ea.fans()
            # 新视频封面
            _thread.start_new_thread(downloadd, (ea.get_video_cover_url(ea.get_new_video_BV()), "new_cover.png"))
            img = cv2.imread("new_cover.png")
            img1 = cv2.resize(img, (270, 152))  # 修改图片的尺寸
            cv2.imwrite("new_cover_chuli.png", img1)
            cover_png = pygame.image.load("new_cover_chuli.png")
            #print("丢包1")
    if (time.time()- jtime2>20):
        try:
            jtime2=time.time()
            # 标题
            new_video_BV=ea.get_new_video_BV()
            title_text = long_str(ea.get_video_title(new_video_BV), 15) + kongge() + str(
                ea.get_video_play(new_video_BV))
            lplaya=ea.get_video_play(new_video_BV)-playa
            playa=ea.get_video_play(new_video_BV)
            ttt=long_str(ea.get_video_title(new_video_BV), 15)
            #新视频各项数据
            v = video.Video(new_video_BV)
            get_stat=sync(v.get_stat())
            llikea = get_stat["like"]-likea
            lfavoritea = get_stat["favorite"]-favoritea
            ldanmakua = get_stat["danmaku"]-danmakua
            lreplya = get_stat["reply"]-replya
            lcoina = get_stat["coin"]-coina
            lsharea = get_stat["share"]-sharea

            likea=get_stat["like"]
            favoritea=get_stat["favorite"]
            danmakua=get_stat["danmaku"]
            replya=get_stat["reply"]
            coina=get_stat["coin"]
            sharea=get_stat["share"]
        except:
            jtime2=time.time()
            # 标题
            new_video_BV=ea.get_new_video_BV()
            title_text = long_str(ea.get_video_title(new_video_BV), 15) + kongge() + str(
                ea.get_video_play(new_video_BV))
            lplaya=ea.get_video_play(new_video_BV)-playa
            playa=ea.get_video_play(new_video_BV)
            ttt=long_str(ea.get_video_title(new_video_BV), 15)
            #新视频各项数据
            v = video.Video(new_video_BV)
            get_stat=sync(v.get_stat())
            llikea = get_stat["like"]-likea
            lfavoritea = get_stat["favorite"]-favoritea
            ldanmakua = get_stat["danmaku"]-danmakua
            lreplya = get_stat["reply"]-replya
            lcoina = get_stat["coin"]-coina
            lsharea = get_stat["share"]-sharea

            likea=get_stat["like"]
            favoritea=get_stat["favorite"]
            danmakua=get_stat["danmaku"]
            replya=get_stat["reply"]
            coina=get_stat["coin"]
            sharea=get_stat["share"]
            #print("丢包2")
    #清除屏幕*重写准备
    screen.fill((0,0,0))
    #获取鼠标位置
    x, y = pygame.mouse.get_pos()
    #up名字
    draw_text_m_30(uname,20,255,255,255)
    #细时间
    draw_text_m_40(str(time.strftime("%H:%M:%S", time.localtime(time.time()))),55,255,255,255)
    #粗时间
    today = LunarDate.today()
    draw_text_m_20(str(time.strftime("%Y.%m.%d", time.localtime(time.time()))) + str("   星期" + weekk[int(time.strftime("%w", time.localtime(time.time())))]) + str("   " + yuefeng[today.month - 1] + riqi[today.day - 1]),80,255,255,255)
    #粉丝数
    fensiweizhi=draw_text_m_60(""+str(fans),120,255,255,255,3)
    if (lfans>0):
        draw_text_30("+"+str(lfans),fensiweizhi[0]+fensiweizhi[2],120,0,255,0)
    if (lfans<0):
        draw_text_30(str(lfans), fensiweizhi[0]+fensiweizhi[2], 120, 255, 0, 0)
    #up头像框
    screen.blit(face_png, (fensiweizhi[0]-50, 99))
    #新视频标题
    biaotiweizhi=draw_text_m_30(title_text, 175, 255, 255, 255,1)
    texttt = font30.render(str(ttt), True, (0, 0, 0))
    screen.blit(bofangp,(biaotiweizhi[0]+texttt.get_rect().width,163))
    if (lplaya>0):
        draw_text_m_30("+"+str(lplaya),200,0,255,0)
    if (lplaya<0):
        draw_text_m_30(str(lplaya), 200, 255, 0, 0)
    #新视频封面
    screen.blit(cover_png, (300, 220))
    #新视频各项数据图标
    screen.blit(likep, (10, 240))
    screen.blit(yinbip, (100, 240))
    screen.blit(shoucangp, (190, 240))

    screen.blit(pinglunp, (10, 310))
    screen.blit(danmup, (100, 310))
    screen.blit(zhuanfap, (190, 310))
    #新视频各项数据
    draw_text_20(str(likea),35,240,255,255,255)
    draw_text_20(str(coina),125,240,255,255,255)
    draw_text_20(str(favoritea),215,240,255,255,255)

    draw_text_20(str(replya),35,310,255,255,255)
    draw_text_20(str(danmakua),125,310,255,255,255)
    draw_text_20(str(sharea),215,310,255,255,255)
    #新视频数据变化
    if (llikea>0):
        draw_text_20("+"+str(llikea),35,260,0,255,0)
    if (llikea<0):
        draw_text_20(str(llikea), 35, 260, 255, 0, 0)
    if (lcoina>0):
        draw_text_20("+"+str(lcoina),125,260,0,255,0)
    if (lcoina<0):
        draw_text_20(str(lcoina), 125, 260, 255, 0, 0)
    if (lfavoritea>0):
        draw_text_20("+"+str(lfavoritea),215,260,0,255,0)
    if (lfavoritea<0):
        draw_text_20(str(lfavoritea), 215, 260, 255, 0, 0)
    if (lreplya>0):
        draw_text_20("+"+str(lreplya),35,330,0,255,0)
    if (lreplya<0):
        draw_text_20(str(lreplya), 35, 330, 255, 0, 0)
    if (ldanmakua>0):
        draw_text_20("+"+str(ldanmakua),125,330,0,255,0)
    if (ldanmakua<0):
        draw_text_20(str(ldanmakua), 125, 330, 255, 0, 0)
    if (lsharea>0):
        draw_text_20("+"+str(lsharea),215,330,0,255,0)
    if (lsharea<0):
        draw_text_20(str(lsharea), 215, 330, 255, 0, 0)
    #右上角按钮（切换是否有边框）
    if (yidonga==True):
        pygame.draw.rect(screen, (255,0,0), (580, 0, 20, 20), 0)
        mouse = pygame.mouse.get_pressed()
        if (mouse[0]==1) and (x>580) and (y<20) and (time.time()-shangciqiehuan1>1):
            shangciqiehuan1 = time.time()
            screen = pygame.display.set_mode((600, 400), pygame.NOFRAME)
            yidonga=False
            mouse[0]==0
    else:
        pygame.draw.rect(screen, (0,0,255), (580, 0, 20, 20), 0)
        mouse = pygame.mouse.get_pressed()
        hwnd = pygame.display.get_wm_info()["window"]
        if (zhidinga==True):
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,  win32gui.GetWindowRect(hwnd)[0],  win32gui.GetWindowRect(hwnd)[1], 0, 0, win32con.SWP_NOSIZE)
        else:
            win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, win32gui.GetWindowRect(hwnd)[0],win32gui.GetWindowRect(hwnd)[1], 0, 0, win32con.SWP_NOSIZE)
        if (mouse[0]==1) and (x>580) and (y<20) and (time.time()-shangciqiehuan1>1):
            shangciqiehuan1 = time.time()
            screen = pygame.display.set_mode((600, 400))
            yidonga=True
            mouse[0]==0
    screen.blit(yidongp,(580,0))
    #左上角按钮
    if (zhidinga==True):
        pygame.draw.rect(screen, (0,0,255), (0, 0, 20, 20), 0)
        if (mouse[0]==1) and (x<20) and (y<20) and (time.time()-shangciqiehuan2>1):
            shangciqiehuan2 = time.time()
            zhidinga=False
            mouse[0]==0
    else:
        pygame.draw.rect(screen, (255,0,0), (0, 0, 20, 20), 0)
        if (mouse[0]==1) and (x<20) and (y<20) and (time.time()-shangciqiehuan2>1):
            shangciqiehuan2 = time.time()
            zhidinga=True
            mouse[0]==0
    screen.blit(zhidingp,(0,0))
    #刷新画面
    #screen = pygame.display.set_mode((600, 400))
    fcclock.tick(fps)
    pygame.display.update()