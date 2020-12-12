import json
input_file=open('input.json', 'r')
output_file=open('new1.json', 'w')
json_decode=json.load(input_file)
print(type(json_decode))
result = []
output_list = []
my_dict={}
option = []

inerr_dict = {}
iner_dict2 = {}

id1 = 0
for key,val in json_decode.items():
  
    # print("key",key)
    # print("value :===",type(val))
    if key == 'optionLists' :
        for dtkey in val:

            my_dict['id']= dtkey['id']
            my_dict['quantity']= 1
            # print(my_dict)
            if dtkey['options'] != None:
                i = 0
                for dt in dtkey['options']:
                    my_dict['id']= dt['id']
                    print(my_dict)

                    if i == 1 :
                        break
                    id1 = dt['id']
                    k = 0
                    for dtt in dt["optionLists"]:
                        if k == 1:
                            break
                        k = k +1
                        j = 0
                        for dttt in dtt["options"]:
                
                            inerr_dict['id'] = dttt["id"]
                            inerr_dict['option'] = "[]"
                            # itemExtraOption
                            iner_dict2['id'] = dttt["id"]
                            iner_dict2['name'] = dttt["name"]

                            inerr_dict["itemExtraOption"] = iner_dict2
                            # my_dict.update(inerr_dict)
                            print("the data in to the inner_dict",inerr_dict)
                            my_dict["options"] = option.append(inerr_dict)
                            # j = j + 1 
                            # if  j == 1 :
                            #     break


                    i = i +1
            output_list.append(my_dict)


result.append(my_dict)

back_json=json.dumps(result)

output_file.write(back_json)
output_file.close() 