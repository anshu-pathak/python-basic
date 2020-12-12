import json
input_file=open('input.json', 'r')
output_file=open('outdatatest.json', 'w')
json_decode=json.load(input_file)
result = []
out_put_list =[]
output_dict= {}
option_list = []
for key,val in json_decode.items():
    if key == 'optionLists' :
        for dtkey in val:

            for index,dtop in enumerate(dtkey['options']):
                output_dict['id'] = dtop['id']
                output_dict['quntity'] = 1
                if index == 0:
                    if dtop['optionLists']:
                        for dtop2 in dtop['optionLists']:
                            # print("----------------------",dtop2['options'])
                            for op_data in dtop2['options']:
                                # print("op datat",op_data)
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
                            output_dict['options'] = option_dict
                out_put_list.append(output_dict)
# print("out_put_list",out_put_list)
            # print("===",output_dict)
    # print(my_dict)
result.append(out_put_list)
back_json=json.dumps(result)
output_file.write(back_json)
output_file.close()