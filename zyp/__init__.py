import os
import logging
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 待分词，生成词云的句子列表
    sentence_list = []
    path = os.path.join('data','info.txt')
    file = open(path, 'rb')

    lines = file.read().splitlines()
    data_index = 1
    i = 0
    while i < len(lines):
        time_stamp = ''
        user_name = ''
        head = []
        try:
            head = lines[i].decode("utf-8").split(' ')
            time_stamp = head[0] + ' ' + head[1]
            user_name = head[2]
        except IndexError:
            # 如果不是头部消息 抛出异常 不处理
            logging.error('error: '+ lines[i].decode("utf-8"))

        # 下一行不为空，则都是消息内容，进行拼接
        message = ''
        message_list = []
        # 读取下一行数据
        i = i + 1
        next_line = lines[i].decode("utf-8")
        # 读取消息数据直到遇到空行
        while i < len(lines) and len(next_line) != 0:
            message_list.append(next_line)
            message_list.append('\r\n')
            i = i + 1
            next_line = lines[i].decode("utf-8")
        message = message.join(message_list)
        log_msg = '%d time:%s user:%s msg:%s' % (data_index, time_stamp, user_name, message)
        logging.info(log_msg)
        sentence_list.append(message)
        data_index = data_index + 1
        # 跳过空行
        i = i + 1
        if i < len(lines):
            next_line = lines[i].decode("utf-8")
        while i < len(lines) and len(next_line) == 0:
            i = i + 1
            next_line = lines[i].decode("utf-8")

    # 进行分词展示 去除一些词汇
    jieba.del_word('图片')
    jieba.del_word('表情')
    jieba.del_word('哈哈哈哈')
    jieba.del_word('哈哈哈')
    jieba.del_word('哈哈')
    jieba.del_word('哈哈哈哈哈哈')
    jieba.del_word('哈哈哈哈哈')
    jieba.del_word('哈哈哈哈哈哈哈哈哈哈')
    jieba.del_word('哈哈哈哈哈哈哈哈哈哈哈')
    jieba.del_word('哈哈哈哈哈哈哈哈哈哈哈哈')
    seg_list = jieba.cut(''.join(sentence_list))
    wc = WordCloud(font_path='simsun.ttc',width=1000,
                    height=800,
                   background_color="white")
    wc.generate(' '.join(seg_list))
    wc.to_file(os.path.join('data', 'temp.jpg'))
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

