
        #desired_caps['automationName']='selendroid'#自动化测试的引擎appium 大于4.2或selendroid小于4.2
        #desired_caps['app']=PATH('') #ipa或apk文件的本地路径或远程路径 appium会在每次运行用例时卸载安装应用
        #desired_caps['newCommandTimeout']=190 #设置命令超时时间，达到超时时间仍未接到新命令 appium会认为客户端退出，session关闭
        #desired_caps['udid']='' #连接的物理设备的唯一标示 adb devices或instruments -w devices的值
        #desired_caps['orientation']=''  #'LANDSCAPE'横向和'PORTRAIT'纵向  在一个设定的方向模式中开始测试
        #desired_caps['autoWebview']='' #true或false  直接切换到webview上下文
        #desired_caps['noReset']=true #true或false 不要在会话前重置应用状态 杀死应用
        #desried_caps['fullReset']=true  #true或false 会话结束后卸载应用 重新安装

        #Android特有关键字
        #desired_caps['appActivity']='' #测试的activity名
        #desired_caps['appPackage']='' #测试的package包名
        #activity名和包名 首先启动应用，再执行： adb shell dumpsys activity top|findstr ACTIVITY命令获取。
        #ACTIVITY com.ss.android.article.lite/.activity.MainActivity 332fa8fe pid=28411
        #比如上边，"/"前边就是包名，后边就是activity名
        #desired_caps['autoWebviewTimeout']=2000 #毫秒，等待webview上下文激活时间
        #desired_caps['unicodeKeyboard']=true #使用unicode输入法
        #desried_caps['resetKeyboard']=true  #unicode测试结束，重置输入法到原来状态