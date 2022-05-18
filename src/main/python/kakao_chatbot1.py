import time, win32con, win32api, win32gui

# # 카톡창 이름 (열려있는 상태, 최소화 X, 창뒤에 숨어있는 비활성화 상태 가능)
kakao_opentalk_name = '주식방'  #채팅 방 이름

def kakao_sendtext(text):
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# # 핸들
#FindWindow를 이용해 캡션(이름)이 '주식방' 이라는 창을 찾아서 핸들을 hwndMain 에 저장
hwndMain = win32gui.FindWindow( None, kakao_opentalk_name)

#FindWindowEx를 이용해 hwndMain(주식방) 의 자식인 RichEdit50W(텍스트박스) 의 핸들을 hwndEdit 에 저장
hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)

#글이 올라오는 대화창의 핸들을 가져온 건데, 나중에 채팅내용 인식 (명령어) 할 때 쓸 거예요
hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

# # 채팅 전송
text = "C:\stockauto>c:/python38-32/python.exe c:/stockauto/test.py" #입력할 메세지
kakao_sendtext(text)
