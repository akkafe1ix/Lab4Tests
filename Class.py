#python_lab01_B_PIN_RIS_2106_Leonov_Alexei

import sys,os,time

#метод шейкерной сортировки
def shaker_sort(array):
    length = len(array)
    swapped= True
    start_index=0
    end_index=length-1

    while (swapped==True):

        swapped=False

        #Проход слева на право
        for i in range(start_index, end_index):
            if(array[i]>array[i+1]):
                #обмен элементов
                array[i], array[i+1] = array[i+1],array[i]
                swapped=True
        
        #Если не было обменов прерываем цикл
        if(not(swapped)):
            return array

        swapped=False

        end_index= end_index-1

         #Проход права на лево
        for i in range(end_index-1, start_index-1,-1):
            if(array[i]>array[i+1]):
                #обмен элементов
                array[i], array[i+1] = array[i+1],array[i]
                swapped=True
        
        start_index=start_index+1
        


print("Шейкерная сортировка целочисленного массива:")
