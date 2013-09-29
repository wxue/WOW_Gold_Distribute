#!/usr/bin/python2.7 -tt
# -*- coding: utf-8 -*-
# version: 1.0

import os
import sys
import binascii

def GetData(filename):
  global data
  # open the raw txt and get ride off \n
  with open (filename, "r") as raw_txt:
    data = raw_txt.read()

def FormData(filename, data):
  id_counter = 0;
  point_area_beg = data.find("<point>", 0)
  point_area_end = data.find("<items>", 0)  - 83
  punish_flag = 0;
  end_flag = 0;
  # "失誤事件標記"
  mark = u'\u5931\u8aa4\u4e8b\u4ef6\u6a19\u8a18'

  # loop boundary： record members' point
  while (point_area_beg < point_area_end):
    print "loop boundary: ", point_area_beg, "-->", point_area_end 
    member_name_beg = data.find("<member>", point_area_beg) + 8
    member_name_end = data.find("</member>", point_area_beg)
    member_name_len = member_name_end - member_name_beg
    
    # check mark, skip the mark
    with open (filename, "r") as raw_txt:
      data = raw_txt.read()
      raw_txt.seek(member_name_beg)
      member_name = raw_txt.read(member_name_len)
      if member_name.decode('gbk') == mark:
        point_area_beg = member_name_end + 1
        if point_area_beg < point_area_end:
          member_name_beg = data.find("<member>", point_area_beg) + 8
          member_name_end = data.find("</member>", point_area_beg)
          member_name_len = member_name_end - member_name_beg
        else:
          end_flag = 1
      raw_txt.close()
    if end_flag == 1:
      break

    print "name", member_name_beg, member_name_end
    point_amount_beg = data.find("<point>", member_name_end) + 7
    point_amount_end = data.find("</point>", member_name_end)
    point_amount_len = point_amount_end - point_amount_beg

    # check punish
    event_end = data.find("</event>", point_amount_end)
    if data.find("<punish>", point_amount_end) != 0:
      if data.find("<punish>", point_amount_end) < event_end:
        punish_flag = 1
  
    print "point", point_amount_beg, point_amount_end
    # record data in the dictionary: member_dict_name and member_dict_point
    with open (filename, "r") as raw_txt:
      data = raw_txt.read()
      raw_txt.seek(member_name_beg)
      member_name = raw_txt.read(member_name_len)
      raw_txt.seek(point_amount_beg)
      point_amount = float(raw_txt.read(point_amount_len))
      print point_amount

      # in case this member is already in the dictionary
      # member_dict_name[1] = member_name.decode('gbk')
      # member_dict_point[1] = point_amount
      member_list = member_dict_name.values()
      if member_name.decode('gbk') in member_list:
        print "in the repeat check"
        # check member member_id in member_dict_name
        for key, value in member_dict_name.items():
          if value == member_name.decode('gbk'):
            member_id = key
        # re-calculate his/her point in member_dict_name
        for key, value in member_dict_point.items():
          if key == member_id:
            if punish_flag == 0:
              member_dict_point[key] = value + point_amount
            else:
              member_dict_point[key] = value - point_amount
        print member_dict_name.get(member_id), member_dict_point.get(member_id)
      else:
        member_dict_name[id_counter] = member_name.decode('gbk')
        if punish_flag == 0:
          member_dict_point[id_counter] = point_amount
        else:
          member_dict_point[id_counter] = -point_amount
        print member_dict_name.get(id_counter), member_dict_point.get(id_counter)
        id_counter = id_counter +1
      # member_dict[member_name.decode('gbk')] = point_amount
      raw_txt.close()
      
    # shrink the point area
    punish_flag = 0;
    point_area_beg = member_name_end + 1
    print id_counter, point_area_beg
    print "--------------------"
    # for c in range(member_name_len):
  #
  # id_counter is counted from 0, end by plus one more.
  # So, id_counter is the nature number that present total amount of members.
  return id_counter


def CalculateGold(filename, data):
  global gold_total
  gold_setion_beg = data.find("<items>", 0)
  gold_setion_end = data.find("</items>", 0) - 16
  while gold_setion_beg < gold_setion_end:
    gold_amount_beg = data.find("<point>", gold_setion_beg) + 7
    gold_amount_end = data.find("</point>", gold_setion_beg)
    gold_amount_len = gold_amount_end - gold_amount_beg
    # print "gold", gold_amount_beg, gold_amount_end

    with open (filename, "r") as raw_txt:
      data = raw_txt.read()
      raw_txt.seek(gold_amount_beg)
      gold_amount = int(raw_txt.read(gold_amount_len))
      # print gold_amount
      gold_total =  gold_total + gold_amount
      # print gold_total
      raw_txt.close()

    gold_setion_beg = gold_amount_end + 1


def DistributeGold(total_member):
  member_id = 0
  total_points = 0
  total_points = float(total_points)

  print "Gold Total:", gold_total, "total_member:", total_member
  for c in range(total_member):
    total_points = total_points + member_dict_point.get(c)
    # print member_dict_point.get(member_id)
    # member_id = member_id + 1
  print "total_points:", total_points

  member_id = 0
  for c in range(total_member):
    for key, value in member_dict_point.items():
      if key == member_id:
        member_dict_point[key] = value/total_points * gold_total
    print "member_id", member_id, "member_point", member_dict_point.get(member_id)
    member_id = member_id + 1
    
    # print member_dict_point.get(member_id)
  # for c in range(total_member):

    # member_id = member_id + 1

def main():
  global data, member_dict_name, member_dict_point, gold_total
  data = 'null'
  member_dict_name = dict()
  member_dict_point = dict()
  gold_total = 0

  total_member = 0;

  GetData(sys.argv[1])
  total_member = FormData(sys.argv[1], data)
  # print member_dict_name
  CalculateGold(sys.argv[1], data)
  print "total_member", total_member
  DistributeGold(total_member)

  output = open('result.txt', 'w+')
  result = ('Total Gold: '+str(gold_total)+'    '+'Members: '+str(total_member)+'\n')
  print result
  output.write(result)
  for c in range(total_member):
    result = ('\n' 'NO.'+str(c+1)+'   Name: '+member_dict_name.get(c)+
              '\n        Gold: '+str(member_dict_point.get(c))+'\n')
    print result
    output.write(result.encode('gbk'))
    
  output.close()

if __name__ == '__main__':
  main()

