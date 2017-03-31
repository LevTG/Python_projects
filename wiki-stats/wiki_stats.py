#!/usr/bin/python3

import os
import sys
import math
import array
import statistics
from matplotlib import rc

rc('font', family = 'Droid Sans', weight = 'normal', size = 14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = [int(x) for x in f.readline().rstrip().split()]
            self._n = n
            self._nlinks = _nlinks
            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n + 1))

            cur = 0
            for i in range(self._n):
                label = f.readline().rstrip()
                size, flag, n_i = [int(x) for x in f.readline().rstrip().split()]
                self._titles.append(label)
                self._sizes[i] = size
                self._offset[i + 1] = (self._offset[i] + n_i)
                self._redirect[i] = bool(flag)

                for j in range(n_i):
                    numb = int(f.readline().rstrip())
                    self._links[cur + j] = numb

                cur += n_i

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[_offset[_id]:_offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id, title):
        return self._sizes[_id]

    def get_exlinks(self, _id, title):
        return self._links.count(_id)

    def print_wg(self):
        print(self._offset[self._n])
        #print(self._links)
        print(self._offset)
        #print(self._titles)
        #print(self._redirect)

def hist(fname, data, bins, xlabel, ylabel, title, facecolor = 'green', alpha = 0.5, transparent = True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл

def get_numb_of_redir_pages(graph):
    count = 0

    for i in range(graph.get_number_of_pages()):
        if graph.is_redirect(i):
            count += 1

    return count

def mcnt_links_from(graph, kind):
    if kind == 'min':
        min_cnt = float('+inf')

        for i in range(graph.get_number_of_pages()):
            min_cnt = min(min_cnt, graph.get_number_of_links_from(i))

        return min_cnt
    
    if kind == 'max':
        max_cnt = 0

        for i in range(graph.get_number_of_pages()):
            max_cnt = max(max_cnt, graph.get_number_of_links_from(i))

        return max_cnt
    
def num_of_pages_with_mclf(graph, kind):
    count = 0
    cnt = mcnt_links_from(graph, kind)

    for i in range(graph.get_number_of_pages()):
        if graph.get_number_of_links_from(i) == cnt:
            count += 1

    return count

def pages_with_maxmin_links(graph, kind):
    cnt = mcnt_links_from(graph, kind)
    titles = []

    for i in range(graph.get_number_of_pages()):
        if graph.get_number_of_links_from(i) == cnt:
            label = graph.get_title(i)
            titles.append(label)

    return titles

def mid_cnt_links(graph):
    mid_cnt = []
    n = graph.get_number_of_pages()

    for i in range(n):
        mid_cnt.append(graph.get_number_of_links_from(i))

    return statistics.mean(mid_cnt), statistics.stdev(mid_cnt)

def mcnt_exlinks(graph, kind):
    if kind == 'min':
        min_cnt = 10**9

        for i in range(graph.get_number_of_pages()):
            min_cnt = min(min_cnt, graph.get_exlinks(i))

        return min_cnt

    if kind == 'max':
        max_cnt = 0

        for i in range(graph.get_number_of_pages()):
            max_cnt = max(max_cnt, graph.get_exlinks(i))

        return max_cnt

def num_of_pages_with_mclf(graph, kind):
    count = 0
    cnt = mcnt_exlinks(graph, kind)

    for i in range(graph.get_number_of_pages()):
        if graph.get_exlinks(i) == cnt:
            count += 1

    return count

def pages_with_maxmin_exlinks(graph, kind):
    cnt = mcnt_exlinks(graph, kind)
    titles = []

    for i in range(graph.get_number_of_pages()):
        if graph.get_exlinks(i) == cnt:
            label = graph.get_title(i)
            titles.append(label)

    return titles

def mid_cnt_exlinks(graph):
    mid_cnt = []
    n = graph.get_number_of_pages()

    for i in range(n):
        mid_cnt.append(graph.get_exlinks(i))

    return statistics.mean(mid_cnt), statistics.stdev(mid_cnt)

def get_path(_id_1, _id_2):
    path = []
    return path

def dfs(graph, start, used = None):
    time = {start: 0}
    if used == None:
        used = set()
    used.add(start)
    Q = [start]
    while Q:
        curr = Q.pop(0)
        for near in graph[curr]:
            if near not in used:
                used.add(near)
                Q.append(near)
                print(curr, near)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

#   wg.print_wg()

    print('Количество статей с перенаправлением:', get_numb_of_redir_pages(wg))
    print('Минимальное количество ссылок из статьи:',mcnt_links_from(wg, 'min'))
    print('Количество статей с минимальным количеством ссылок:', num_of_pages_with_mclf(wg, 'min'))
    #print('', ' '.join(pages_with_maxmin_links(wg, 'min')))
    print('Максимальное количество ссылок из статьи:', mcnt_links_from(wg, 'max'))
    print('Количество статей с максимальным количеством ссылок:', num_of_pages_with_mclf(wg, 'max'))
    print('Статья с наибольшим количеством ссылок:', ' '.join(pages_with_maxmin_links(wg, 'max')))
    print('Среднее количество ссылок в статье:', '%0.2f ст.откл. %0.2f' %mid_cnt_links(wg))
    print('Минимальное количество ссылок на статью:', mcnt_exlinks(wg, 'min'))
    print('Количество статей с минимальным количеством внешних ссылок:', num_of_pages_with_mclf(wg, 'min'))
    #print('', ' '.join(pages_with_maxmin_exlinks(wg, 'min')))
    print('Максимальное количество ссылок на статью:', mcnt_exlinks(wg, 'max'))
    print('Количество статей с максимальным количеством внешних ссылок:', num_of_pages_with_mclf(wg, 'max'))
    print('Статья с наибольшим количеством внешних ссылок:', ' '.join(pages_with_maxmin_exlinks(wg, 'max')))
    print('Среднее количество внешних ссылок на статью:', '%0.2f ст.откл. %0.2f' %mid_cnt_exlinks(wg))



    # TODO: статистика и гистограммы
