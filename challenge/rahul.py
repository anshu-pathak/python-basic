import json
input_file=open('input.json', 'r')
output_file=open('outdata.json', 'w')
json_decode=json.load(input_file)
result = []
out_put_list =[]
output_dict= {}
option_list = []
option2_list = []
for key,val in json_decode.items():
    if key == 'optionLists' :
        for dtkey in val:
            for index,dtop in enumerate(dtkey['options']):
                item_extra_dict = {
                        "id" : dtop['id'],
                        "name" : dtop['name'],
                }
                if index == 0:
                    if dtop['optionLists']:
                        for dtop2 in dtop['optionLists']:
                            # print("----------------------",dtop2['options'])
                            for idx,op_data in enumerate(dtop2['options']):
                                # print("=== index",idx,"data :==",op_data)
                                if op_data['id'] == '2332496975':
                                # print("-----------------------------------------------------------------------------")
                                    item_extra_opt_dict = {
                                        "id" : op_data['id'],
                                        "name" : op_data['name'],
                                    }
                                    option_dict = {
                                        "id" : op_data['id'],
                                        "quantity" : 1,
                                        "options" : [],
                                        "itemExtraOption" :item_extra_opt_dict,
                                    }
                                    option_list.append(option_dict)
                                    print("options dict :==",option_dict)
                                if op_data['id'] == '2332497174':
                                    item_extra_opt_dict = {
                                        "id" : op_data['id'],
                                        "name" : op_data['name'],
                                    }
                                    option_dict = {
                                        "id" : op_data['id'],
                                        "quantity" : 1,
                                        "options" :option2_list,
                                        "itemExtraOption" :item_extra_opt_dict,
                                    }
                                    option_list.append(option_dict)
                                    for op in op_data['optionLists']:
                                        for index2,op2 in enumerate(op['options']):
                                            if index2 == 0:
                                                item_extra_opt_dict = {
                                                    "id" : op2['id'],
                                                    "name" : op2['name'],
                                                }
                                                option_dict = {
                                                    "id" : op2['id'],
                                                    "quantity" : 1,
                                                    "options" : [],
                                                    "itemExtraOption" :item_extra_opt_dict,
                                                }
                                                option2_list.append(option_dict)
                                                print("options dict :========",option2_list)
                            # break
                        final_dict = {
                            "id" : dtop['id'],
                            "quntity" : 1,
                            "options" : option_list,
                            "itemExtraOption" :item_extra_dict
                        }
out_put_list.append(final_dict)
# print("out_put_list",out_put_list)
            # print("===",output_dict)
    # print(my_dict)
result.append(out_put_list)
back_json=json.dumps(result)
output_file.write(back_json)
output_file.close()