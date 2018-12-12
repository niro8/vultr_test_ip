# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen
import re
from multiprocessing import Pool, Manager

def get_r(domain, n):
    cmd = 'ping '+domain[-1]
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    r = p.communicate()[0].decode('gbk')
    time = int(re.search(r'平均 = (\d+)',r).group(1))
    lost = int(re.search(r'丢失 = (\d+)',r).group(1))
    domain.append(time)
    domain.append(lost)
    n.append(domain)


if __name__ == '__main__':
    domain_list = [
        ['(Asia)Tokyo, Japan[日本 东京]', 'hnd-jp-ping.vultr.com'],
        ['Singapore[新加坡]', 'sgp-ping.vultr.com'],
        ['(AU) Sydney, Australia[悉尼]', 'syd-au-ping.vultr.com'],
        ['(EU) Frankfurt, DE[德国 法兰克福]', 'fra-de-ping.vultr.com'],
        ['(EU) Amsterdam, NL[荷兰 阿姆斯特丹]', 'ams-nl-ping.vultr.com'],
        ['(EU) London, UK[英国 伦敦]', 'lon-gb-ping.vultr.com'],
        ['(EU) Paris, France[法国 巴黎]', 'par-fr-ping.vultr.com'],
        ['Seattle, Washington[美东 华盛顿州 西雅图]', 'wa-us-ping.vultr.com'],
        ['Silicon Valley, Ca[美西 加州 硅谷]', 'sjo-ca-us-ping.vultr.com'],
        ['Los Angeles, Ca[美西 加州 洛杉矶(推荐)]', 'lax-ca-us-ping.vultr.com'],
        ['Chicago, Illinois[美东 芝加哥]', 'il-us-ping.vultr.com'],
        ['Dallas, Texas[美中 德克萨斯州 达拉斯]', 'tx-us-ping.vultr.com'],
        ['New York / New Jersey[美东 新泽西]', 'nj-us-ping.vultr.com'],
        ['Atlanta, Georgiaa[美东 乔治亚州 亚特兰大]', 'ga-us-ping.vultr.com'],
        ['Miami, Florida[美东 佛罗里达州 迈阿密]', 'fl-us-ping.vultr.com']
    ]
    p = Pool()
    ns = Manager().list()
    for domain in domain_list:
        p.apply_async(get_r, (domain, ns))
    p.close()
    p.join()
    r_list = eval(ns.__str__())
    r_list.sort(key=lambda k:k[2])
    for i in r_list[:5]:
        print(i)
