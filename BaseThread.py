import threading


class BaseThread(threading.Thread):
    '''
    BaseThread 的說明
    BaseThread https://gist.github.com/fogdingding/40f5093a505c42f0db0fc1758e1e38c8 參考他人寫法，所使用的多執行續。
    Attributes(相關函數說明)
    ----------
    __init__                        : 初始化
    target_with_callback            : 用來執行my_thread_job完成後將要執行的事情
    my_thread_job                   : 執行完成後，將會callback (cb function)
    cb                              : callback function 執行my_thread_job完成後將要執行的事情
    Methods(如何使用說明)
    ----------
    EX:
        BaseThread(
            target=my_thread_job,
            callback=cb,
            callback_args=(line)
            ).start()
    '''
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self):
        self.method()
        if self.callback is not None:
            self.callback(*self.callback_args)